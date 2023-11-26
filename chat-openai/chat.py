import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

with open('./prompt.md',encoding='utf-8',mode='r') as prompt_file:
    system_prompt = prompt_file.read()

def chat(model = 'gpt-3.5-turbo', temperature = 0, max_tokens = 200):
    query = input('ENTER YOUR QUERY: \n')

    messages = [
        {   'role' : 'system',
            'content': system_prompt},
        {
            'role' : 'user',
            'content': query
        }
    ]

    response = openai.ChatCompletion.create(model=model, messages=messages, temperature= temperature, max_tokens= max_tokens)

    response_text = response['choices'][0]['message']['content']

    return response_text, response


if __name__ == "__main__":
    text, _ = chat(temperature = 1)
    print(text)