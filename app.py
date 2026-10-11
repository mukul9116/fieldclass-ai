import streamlit as st

from fieldclass.experiments import get_experiment
from fieldclass.feedback import evaluate_report
from fieldclass.grading import expected_answer
from fieldclass.llm import LLMOutputError, LLMUnavailable
from fieldclass.mission import generate_mission
from fieldclass.schemas import MissionRequest, Report

TOPIC_LABELS = {
    "trig_height": "Maths: height of a tree (trigonometry)",
    "statistics_counts": "Statistics: count and classify objects",
    "plant_leaves": "Biology: compare leaves",
    "average_velocity": "Physics: average velocity",
}

ANSWER_HELP = {
    "trig_height": "height of the tree in metres",
    "statistics_counts": "share of the most common type, as a fraction such as 0.25",
    "plant_leaves": "length divided by width of leaf A",
    "average_velocity": "average velocity in metres per second, using the mean of your times",
}

st.set_page_config(page_title="FieldClass AI", page_icon="🌿")

if "step" not in st.session_state:
    st.session_state.step = "start"


def show_start():
    st.title("FieldClass AI")
    st.caption("Your textbook becomes a field experiment.")
    st.write("Turn what you study into something you can experience.")
    topic = st.selectbox("What are you studying?", list(TOPIC_LABELS), format_func=TOPIC_LABELS.get)
    difficulty = st.radio("Difficulty", ["easy", "medium", "hard"], index=1, horizontal=True)
    minutes = st.slider("Minutes available", 10, 120, 30, step=5)
    notes = st.text_area("Anything we should know? (optional)", max_chars=500)
    if st.button("Create my mission", type="primary"):
        request = MissionRequest(topic=topic, difficulty=difficulty, minutes=minutes, notes=notes or None)
        try:
            with st.spinner("Writing your mission. This takes about 10 seconds..."):
                st.session_state.mission = generate_mission(request)
        except LLMUnavailable as e:
            st.error(str(e))
            return
        except LLMOutputError:
            st.error("The model could not write a good mission. Please try again.")
            return
        st.session_state.step = "mission"
        st.rerun()


def show_mission():
    mission = st.session_state.mission
    st.title(mission.title)
    st.write(mission.objective)
    st.info("Read this. Then put your phone away.")
    st.write(f"About {mission.minutes} minutes · {mission.difficulty}")
    st.subheader("Bring")
    for item in mission.materials:
        st.write("- " + item)
    st.subheader("Do")
    for number, step in enumerate(mission.steps, start=1):
        st.write(f"{number}. {step}")
    st.subheader("Write down")
    for item in mission.record:
        st.write("- " + item)
    st.warning("Safety: " + mission.safety)
    st.caption("Tip: " + mission.tip)
    if st.button("I'm back with my results"):
        st.session_state.step = "report"
        st.rerun()

def show_feedback(feedback):
    st.divider()
    st.subheader("Your feedback")
    if feedback.verdict == "correct":
        st.success("Correct")
    elif feedback.verdict == "partial":
        st.warning("Close")
    elif feedback.verdict == "incorrect":
        st.error("Not quite")
    else:
        st.info("Something is missing")
    st.write(feedback.went_well)
    st.write("**Hint:** " + feedback.hint)
    if feedback.verdict == "correct":
        st.write("**Why it works:** " + feedback.concept)
    elif feedback.verdict in ("partial", "incorrect"):
        if st.button("Show me the answer"):
            st.session_state.revealed = True
        if st.session_state.get("revealed"):
            report = st.session_state.report
            st.write(f"Using your own measurements, the answer is about {expected_answer(report.topic, report.values):.2f}.")
            st.write("**Why it works:** " + feedback.concept)
    st.write("**Next challenge:** " + feedback.next_challenge)
    if st.button("Start a new mission"):
        for key in ("mission", "report", "feedback", "revealed"):
            st.session_state.pop(key, None)
        st.session_state.step = "start"
        st.rerun()

def show_report():
    mission = st.session_state.mission
    experiment = get_experiment(mission.topic)
    st.title("Welcome back")
    st.write("Enter what you measured. Leave a box empty if you did not measure it.")
    values = {}
    for field in experiment.report_fields:
        number = st.number_input(f"{field.label} ({field.unit})", value=None, step=0.1)
        if number is not None:
            values[field.name] = number
    answer = st.number_input("Your calculated answer: " + ANSWER_HELP[mission.topic], value=None, step=0.01)
    observations = st.text_area("What did you notice?", max_chars=600)
    reflection = st.text_area("What was hard or surprising?", max_chars=600)
    if st.button("Check my work", type="primary"):
        report = Report(topic=mission.topic, values=values, answer=answer,
                        observations=observations, reflection=reflection)
        try:
            with st.spinner("Checking your work..."):
                st.session_state.feedback = evaluate_report(report)
        except LLMUnavailable as e:
            st.error(str(e))
            return
        except LLMOutputError:
            st.error("Could not write the feedback. Please try again.")
            return
        st.session_state.report = report
        st.session_state.revealed = False
    if "feedback" in st.session_state:
        show_feedback(st.session_state.feedback)

if st.session_state.step == "start":
    show_start()
elif st.session_state.step == "mission":
    show_mission()
elif st.session_state.step == "report":
    show_report()