# LLM Prompt Evaluation Toolkit

This project provides a structured pipeline for evaluating responses from large language models (LLMs) across custom prompts. It enables the generation of responses, scoring of outputs, and analysis of basic performance metrics.

## Features:
- Custom prompt input (CSV)
- Automatic LLM querying (Hugging Face or OpenAI API)
- Response logging
- Output scoring (length check, keyword match, basic toxicity filter)
- Results CSV export

## Usage:
- Place your prompts in `prompts.csv`.
- Configure API keys if using OpenAI.
- Run:
python evaluate.py
- Results are saved in `results.csv`.



