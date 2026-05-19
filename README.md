# AI News Email Summarizer

This project fetches the latest business news using NewsAPI, analyzes it using Google Gemini via LangChain, and sends a summarized report by email.

## Features

- Fetches top business news headlines
- Extracts title, description, content, and source
- Uses AI to generate:
  - 1 paragraph news summary
  - 1 paragraph stock market impact analysis
- Sends results via email
- Uses environment variables for API keys

## Tech Stack

- Python
- Requests
- LangChain (Google Gemini)
- NewsAPI
- SMTP Email
- python-dotenv

