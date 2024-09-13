import google.generativeai as genai
import re
import json
import time

from pathlib import Path

def generate_content(api_key, language="taiwanese mandarin", target_language="english", contains_word=None):
    prompt_context = """
    Please provide a response in a structured JSON format that matches the following model {"sentence_language": "english", "output_language": "indonesian", "sentence": "quick brown fox", "words": [{"word": "the", "translate": "itu"}, {"word": "quick", "translate": "itu"}, {"word": "fox", "translate": "rubah"}]}
    """
    
    prompt_content = f"Please make a sentence in {language} then extract relevant distinct words on that sentence and provide the translation in {target_language}. {prompt_context}"

    if contains_word:
        prompt_content = f"Please make a sentence in {language} that contains word {contains_word} then extract relevant distinct words on that sentence and provide the translation in {target_language}. {prompt_context}"


    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt_content)
    response_text = response.text
    response_data = response_text.replace("\n", " ")
    matches = re.findall(r"```json(.*?)```", response_data)
    if matches:
        data = json.loads(matches[0])
        data_path = f"data/{language}/{target_language}"
        data_file_path = f"{data_path}/{int(time.time())}.json"
        Path(data_path).mkdir(parents=True, exist_ok=True)

        with open(data_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return data_file_path