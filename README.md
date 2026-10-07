# FieldClass AI

> **Your textbook becomes a field experiment.**

FieldClass AI turns a topic you are studying into a short outdoor experiment, then helps you make sense of what you found when you come back. It is built around an open-weight model that runs locally on your own machine.

Most AI study tools add screen time. FieldClass does the opposite: it reads what you are learning, hands you a mission you can read in under a minute, and gets out of the way while you go outside, measure something real, and bring the numbers back.

Built for the Hacktoberfest 2026 Open-Source AI Challenge, theme **Touch Grass**.

## Status

In development. The project is not runnable end to end yet. This README describes what exists today and is updated as each part lands.

## How it works

1. Choose a subject, topic, difficulty and the time you have.
2. FieldClass generates a short field mission: objective, materials, steps, what to record, and a safety note.
3. Put your phone away and carry out the mission outdoors.
4. Come back and enter your measurements, observations and a short reflection.
5. FieldClass reviews your attempt, gives hints before answers, and connects what you saw to the concept in your textbook.

The four starting topics are trigonometry (estimating the height of a tree or pole), statistics (counting and classifying objects), plant morphology (comparing leaves) and average velocity (timing a moving object over a measured distance). See [docs/MVP.md](docs/MVP.md) for the full scope.

## Why an open-weight model

- **Local.** The model runs on your machine through Ollama, so it works without sending anything to a third-party server.
- **Private.** Your notes and study material stay on your computer.
- **Swappable.** The model is chosen by a named profile in one configuration module. Moving from a small model on a modest laptop to a larger model on a GPU machine is a configuration change, not a code change.

## Requirements

- Python 3.13
- [Ollama](https://ollama.com), latest version
- Git

## Setup

In PowerShell:

```
git clone https://github.com/mukul9116/fieldclass-ai
cd fieldclass-ai
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
ollama pull gemma3:1b
```

## Model profiles

The active model is selected by the `FIELDCLASS_PROFILE` environment variable. If it is not set, the `lite` profile is used. Profiles are defined in `fieldclass/config.py`.

To check which profile is active:

```
python -c "from fieldclass.config import get_profile; print(get_profile())"
```

To switch profile for the current PowerShell session:

```
$env:FIELDCLASS_PROFILE="lite"
```

## Project layout

```
fieldclass/
  config.py     model profiles and settings
docs/
  MVP.md        product scope and success criteria
requirements.txt
```

More modules are added as they are built.
