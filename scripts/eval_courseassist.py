from openai import OpenAI
from ..utils.vector_store_functions import initialize_chromadb, query_database
from ..utils.io_functions import read_json, write_json

tutor_system = """You are a university tutor helping students with their inquiries. Provide responses that are factual and reference your vector store of course materials when producing answers."""

ui_system = """You are a user intent classifier which assesses a student's query and determines its category. Given a user question, you should check whether this question is a general software engineering inquiry(general), an off-topic inquiry unrelated to software engineering topics(off-topic), or a question specifically related to any of the labs or project function specifications(assessment). You should follow a step-by-step process to make this classification.

First, check if the query is a follow up question to a previous query earlier in the conversation history. Make a classification based on that. For example sometimes a query may appear off-topic but is actually a continuation from the previous messages.

Then if the query is unrelated to the previous messages, use the relevant context that will be provided to see if the question relates closely with the assessment tasks. 

If so, then you should consider classifying the query as "assessment". 

Otherwise, you should determine whether the query is related to software engineering and coding or not. If the question is specific to technical software engineering knowledge, i.e. conceptual or coding-related queries, you should classify it as "general". If the question does not relate to technical software engineering knowledge, then you should classify the query as "off-topic"."""

moderator_system = """You are a detector for bad AI generations in a tutoring app.
Your job is to detect whether the AI generated response is appropriate for students. 
You should ensure that the AI is only giving hints and not full solutions to help students learn. 
If the AI generated response in the following conversation has too much direct solution, rewrite the response to give only helpful hints but not the full solution. 
Otherwise, you can return the original AI response."""

client = OpenAI()

def chat_tutor(messages):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )
    return completion.choices[0].message.content

def chat_moderator(messages):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )
    return completion.choices[0].message.content

def chat_ui(messages):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )
    return completion.choices[0].message.content

db = initialize_chromadb()
collection = db.get_or_create_collection(name="comp1531_specs")
conversations = read_json('../testing_data/test.json')
outputs = []

def courseassist(conversation):
    ui_history = ""
    tutor_history = [{"role": "system", "content": tutor_system}]
    moderator_history = [{"role": "system", "content": moderator_system}]
    output = []
    for question in conversation:
        docs = query_database(collection, question)

        ui_prompt = f"""Here is the user query: {question}\n
        Review the conversation history to check if this query is a follow-up to earlier messages:
        <{ui_history}>

        Relevant knowledge from the lab / project specifications:
        <{docs}>
        
        Classification should belong to these three categories: general, off-topic, assessment.
        Output only the exact category label:"""
        label = chat_ui([{"role": "system", "content": ui_system}, {"role": "user", "content": ui_prompt}])

        tutor_history.append({"role": "user", "content": question})
        tutor_response = chat_tutor(tutor_history)
        tutor_history.append({"role": "assistant", "content": tutor_response})

        moderator_response = tutor_response
        if label == 'assessment':
            moderator_prompt = f"""Student Question: {question}\nAI generated response: {tutor_response}\nIf the previous response has any code solutions, rewrite
the previous response here to only give helpful hints, but
not the full solution. If the previous response does not
have any code solutions, simply return the previous response."""
            moderator_history.append({"role": "user", "content": moderator_prompt})
            moderator_response = chat_moderator(moderator_history)
            moderator_history.append({"role": "assistant", "content": moderator_response})

        ui_history += f"STUDENT: {question}\nUSER INTENT: {label}\nTUTOR: {moderator_response}\n"
        output.append({'student': question['question'], 'correct label': question['category'], 'user intention': label, 'tutor': moderator_response})

conversations = read_json('../testing_data/test.json')
for conversation in conversations:
    outputs.append(courseassist(conversation))

write_json("../evaluations/courseassist_outputs.json", outputs)