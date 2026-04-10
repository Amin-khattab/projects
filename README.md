# projects

A mix of small Python projects I've built while learning — mostly chatbots, some ML, and a few random things like regression from scratch and a library manager. Each file is its own self-contained project, numbered roughly in the order I worked on them.

## What's in here

| # | File | What it is |
|---|------|------------|
| 01 | `01_simple-Ai-chatbot-using(py).py` | A basic chatbot written in plain Python — no ML, just logic and responses |
| 02 | `02_simple-Ai-using(NLP).py` | A smarter chatbot using NLP techniques for understanding user input |
| 03 | `03_Ai-resume-checker.py` | Takes a resume and checks it against some criteria — my first useful-feeling project |
| 04 | `04_Digit_recognizer_CNN.py` | Classic digit recognizer built with a CNN |
| 05 | `05_Library.py` | A small library management system — add books, borrow, return, etc. |
| 06 | `06_regression_by_numpy.py` | Linear regression implemented from scratch with just NumPy, no ML libraries |
| 07 | `07_GPT-2-FineTuned.py` | Fine-tuning GPT-2 on custom data |
| 08 | `08_T5-FineTuned.py` | Same idea but with T5 — wanted to see the difference |
| 09 | `09_tiny_shakespear(Transformer)-V1.py` | A tiny transformer trained on Shakespeare text — building one from the ground up |

## Why this repo exists

I wanted a single place to keep all the little experiments I do while learning — chatbots, ML basics, transformers, whatever catches my interest. Some of these are just me trying to understand how something works under the hood (like writing regression with only NumPy), others are closer to actual mini-projects.

## Running any of them

Everything is Python. Depending on which file you're running, you might need different libraries:
pip install numpy pandas scikit-learn torch transformers nltk

Then just run whichever one you want:
python 01_simple-Ai-chatbot-using(py).py

The transformer and fine-tuning scripts (07, 08, 09) will need a GPU if you don't want to wait forever.

## Notes

This is a learning repo, so expect some rough edges and half-finished ideas. I'll keep adding to it as I build more stuff.
