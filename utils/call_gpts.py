from openai import OpenAI

client = OpenAI()

def chat_tutor(messages):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )
    return completion.choices[0].message.content

def chat_ui(messages):
    completion = client.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:loch:ai-tutor-ui-classifier:AmbSdfCs",
        messages=messages,
        temperature=0
    )
    return completion.choices[0].message.content