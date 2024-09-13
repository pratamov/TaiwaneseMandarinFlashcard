import json
import random
import playsound
import os.path

from prompter_gemini import generate_content
from gtts import gTTS

def play_sound(text, language="zh-TW"):
    filepath = f"data/audio/{text}.mp3"
    if not os.path.isfile(filepath):
        tts = gTTS(text=text, lang='zh-TW')
        tts.save(filepath)
    playsound.playsound(filepath)


def play_flashcard(filepath="data/taiwanese mandarin/english/1726244351.json", max_attempts=5):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        scores = {w["word"]: 0 for w in data["words"]}
        words = data["words"] * min(max_attempts, len(data["words"]))
        random.shuffle(words)

        for item in words:
            play_sound(item["word"])
            answer = input(f"{item['word']} : ")
            if answer.lower() == item["translate"].lower():
                scores[item["word"]] += 1
            else:
                print("WRONG!", f"{item['word']} : {item['translate']}")

        with open(f"{filepath}.score", "w", encoding="utf-8") as ff:
            json.dump(scores, ff, ensure_ascii=False) 
    print(scores)

from dotenv import load_dotenv
if __name__ == "__main__":
    load_dotenv()
    filepath = generate_content(os.getenv("API_KEY"))
    play_flashcard(filepath=filepath)