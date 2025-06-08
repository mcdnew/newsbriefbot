import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "Summarize the following article:"},
                {"role": "user", "content": text}
            ],
            max_tokens=300,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("Summarization failed:", e)
        return ""

