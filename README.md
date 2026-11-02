# Datheon Python Programming Internship

A collection of four command-line Python projects for the Datheon Python Programming Internship.

## Projects

| Task | Project | What it does |
| --- | --- | --- |
| 1 | Hangman Word Guessing Game | Six-mistake word game with ASCII gallows, input validation, and duplicate-guess handling. |
| 2 | Stock Portfolio Performance Tracker | Fetches available stock quotes, calculates investment values and returns, and writes CSV reports. |
| 3 | Automated File Organizer | Sorts files by extension, avoids duplicate filename overwrites, and logs operations. |
| 4 | Rule-Based Chatbot | Answers sample internship FAQs from JSON using regular-expression rules, including greetings, help, fallback and exit. |

## Requirements

- Python 3 (tested locally with Python 3.14 on Windows).
- Task 2 requires internet access and the third-party `yfinance` package.
- Tasks 1, 3, and 4 use the Python standard library.

Install Task 2's dependency:

```powershell
py -m pip install yfinance
```

## How to Run

Open PowerShell at the repository root and run any of these commands.

### Task 1 — Hangman

```powershell
py "Task 1 Hangman\hangman.py"
```

Guess a single letter at a time. The game shows the hidden word and ASCII gallows and allows six incorrect guesses.

### Task 2 — Stock Portfolio Tracker

```powershell
py "Task 2 Stock Tracker\portfolio.py"
```

Enter a stock ticker, purchase price per share, and number of shares. Type `done` when finished. The program calculates each holding and the overall portfolio, then appends the results to `Task 2 Stock Tracker/portfolio_summary.csv`.

`SP500 Tickers.csv` provides company and symbol information, not market prices. The script obtains available quotes through `yfinance`; they may be delayed or unavailable. The committed CSV contains **illustrative test investments**, not a real brokerage account or verified historical transactions.

### Task 3 — Automated File Organizer

```powershell
py "Task 3 File Organizer\organizer.py"
```

This version organizes files directly inside `Task 3 File Organizer/Test Files`, placing them in category folders: Documents, Images, Videos, Audio, Archives, Code, or Other. Existing subfolders are not processed recursively. Duplicate filenames are assigned a numbered suffix. Activities and errors are written to `Task 3 File Organizer/Organization Log.txt`.

**Test-data note:** The repository includes empty files named with `.pdf`, `.jpg`, `.mp3`, `.mp4`, `.zip` and other extensions to demonstrate extension-based sorting. They are not valid media or document examples. Test on copies before using this program on important files.

### Task 4 — Rule-Based Chatbot

```powershell
py "Task 4 Chatbot\chatbot.py"
```

The chatbot loads `Task 4 Chatbot/sample_faq.json`, recognizes greetings and common FAQ keywords, answers known questions, provides a fallback for unsupported questions, and exits on `exit`, `quit`, `bye`, or `goodbye`.

The FAQ answers come from a **sample dataset**. Their claims about operating hours or certificate timelines are not independently verified provider policies.

## Testing and Screenshots

The `Screenshots` folder contains terminal evidence for the four tasks.

- **Hangman:** Startup, correct/duplicate/invalid guesses, and winning result. The losing condition can be confirmed in the final audit.
- **Stock tracker:** Stock quotes, numeric validation, duplicate ticker rejection, portfolio calculations, and CSV history.
- **File organizer:** Initial sorting, unknown extensions, duplicate-name handling, folder structure, and execution log.
- **Chatbot:** Greeting, FAQ responses, unknown question, help, and exit.

## Project Notes

These are educational command-line projects. The stock tracker is not financial advice. File organization should be tested using sample copies before being adapted to personal directories.

Repository: https://github.com/tharunsasanka/Datheon_Python_Programming_Internship
