# Trial

This repository demonstrates a small prototype for a personalized love-letter generator using OpenAI reinforcement fine-tuning. The system **does not** include a screenshot feature and **does not** scrape Pinterest.

## Components

- `fine_tune_openai.py`: Example script showing how to setup reinforcement fine-tuning with OpenAI API.
- `data/`: Placeholder directory for user-provided love letters and open-license romantic text.

The approach focuses on training with user permission and publicly available datasets.

## Web Application

The `webapp.py` module provides a minimal FastAPI interface for uploading sample
texts and generating a love letter in that style. Run it with:

```bash
pip install fastapi uvicorn jinja2
uvicorn webapp:app --reload
```

Then visit `http://localhost:8000` to submit your texts and see a generated
letter.

## Features and Planned Features

- Reinforcement fine-tuning workflow (`fine_tune_openai.py`)
- Accepts user-provided romantic texts stored in `data/`
- Placeholder reward function for customizing style and tone
- **No screenshot feature** (explicitly out of scope)
- **No Pinterest scraping** (Pinterest ToS forbids scraping)

Future work includes improved reward heuristics for personalized outputs.
