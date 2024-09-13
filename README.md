# README

## Overview

This project uses the Gemini API to generate sentences in Taiwanese Mandarin, extracts distinct words from those sentences, and provides their English translations. It also features an interactive flashcard tool to help users learn and practice vocabulary.

## Prerequisites

- Python 3.8+ (tested in Python 3.10)
- A Gemini API key

## Setup Instructions

1. Generate API Key

Go to Gemini API Key Generation and generate a new API key.

2. Create `.env` File

In the root directory, create a file named `.env`. Add the following line, replacing <your-api-key> with the API key you generated:

```
API_KEY=<your-api-key>
```

3. Install Dependencies

```
python -m pip install -r requirements.txt
```

4. Run the Application

```
python play.py
```

## How It Works

The program uses Gemini to prompt the creation of a sentence in Taiwanese Mandarin, extracts the distinct words, and provides translations into English. These translations are used in a flashcard-style quiz for learning purposes.

### Prompt Details

The program sends the following prompt to Gemini:

```
Please make a sentence in {language}, then extract relevant distinct words from that sentence and provide the translation in {target_language}. {prompt_context}. Please provide a response in a structured JSON format that matches the following model:
{
  "sentence_language": "english",
  "output_language": "indonesian",
  "sentence": "quick brown fox",
  "words": [
    {"word": "the", "translate": "itu"},
    {"word": "quick", "translate": "cepat"},
    {"word": "fox", "translate": "rubah"}
  ]
}
```


### Example Response

The output from Gemini will look like this:

```
{
  "sentence_language": "taiwanese mandarin",
  "output_language": "english",
  "sentence": "你今天要去哪裡？",
  "words": [
    {"word": "你", "translate": "you"},
    {"word": "今天", "translate": "today"},
    {"word": "要", "translate": "want to"},
    {"word": "去", "translate": "go"},
    {"word": "哪裡", "translate": "where"}
  ]
}
```

### Flashcard Feature

The extracted words and the respective sounds are displayed as flashcards to help the user practice and reinforce vocabulary learning.

