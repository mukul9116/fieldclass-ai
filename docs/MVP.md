# FieldClass AI: MVP Scope

> **Your textbook becomes a field experiment.**

## Problem

Most AI tools for students add more screen time: more explanations, more chat, more text to read. But many ideas in physics, math, biology and statistics only become real when you see them happen. A formula for the height of a tree is abstract until you stand in front of one. Students need a reason to look up from the screen, and AI can supply it.

## Target user

A high school or first-year college student studying a STEM subject who finds the material abstract. They have a phone or laptop, a few free minutes, and safe access to a yard, park, campus or quiet street. They are not looking for an answer machine. They want to understand a concept well enough to use it. A teacher who wants a quick fieldwork assignment is a secondary user.

## Value proposition

FieldClass AI turns the topic you are studying into a short outdoor experiment, then helps you make sense of what you found when you come back.

## User journey

1. The student chooses a subject, a topic, a difficulty and the time they have.
2. FieldClass generates a short field mission that can be read in under a minute.
3. The student puts the phone away and carries out the mission outdoors, measuring or observing something real.
4. The student returns and enters their measurements, observations and a short reflection.
5. FieldClass reviews the attempt, gives hints before answers, and connects the experience back to the concept in the textbook.

## MVP features

- [ ] Input form: subject, topic, difficulty, time available, optional notes
- [ ] Mission generator returning a structured, validated field mission (objective, materials, steps, data to collect, safety notes, concept link)
- [ ] Safety rules: no traffic, private property, heights, hazardous materials or risky activity
- [ ] Report form for measurements, observations and reflection
- [ ] Feedback that separates correct, partially correct, incorrect and missing work, and gives hints before revealing answers
- [ ] Concept connection: why the experiment illustrates the idea
- [ ] Four starting topics:
  - Trigonometry: estimate the height of a tree or pole
  - Statistics: count and classify objects to find frequencies
  - Plant morphology: observe and compare leaves
  - Average velocity: time a moving object over a measured distance
- [ ] Open-weight model running locally through Ollama, with the model name set in configuration so it can be swapped

## Non-goals

- Accounts, logins or payments
- Databases, vector search or retrieval over documents
- Autonomous agents or multi-step tool use
- Photo review of student evidence ("Proof Mode"); this is future work
- Maps, GPS or social features
- A native mobile app
- Fine-tuning a model
- Subjects beyond the four starting topics

## Success criteria

1. A generated mission can be read in under 60 seconds and completed without looking at the phone again.
2. Every mission can be done outdoors with common materials and contains no unsafe step.
3. For each of the four topics, the engine returns valid structured output, retrying automatically if the first attempt is malformed.
4. Feedback names what the student did correctly and what is missing, and gives a hint before revealing any answer.
5. Changing a single configuration value switches the model with no code change, and the same test set can be rerun on the new model.
6. The complete loop (mission, outdoor activity, report, feedback) has been carried out for real at least once, outside, and documented.
