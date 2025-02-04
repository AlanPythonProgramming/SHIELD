from openai import OpenAI
from ..utils.vector_store_functions import initialize_chromadb, query_database
from ..utils.call_gpts import chat_tutor, chat_ui
from ..utils.io_functions import read_json, write_json

client = OpenAI()

tutor_system = """INSTRUCTIONS: A tutor and a student work together to resolve software engineering questions for the course COMP1531 - Software Engineering Fundamentals. You need to role-play the tutor while the user roleplays the student.
The tutor is a soft-spoken empathetic teaching assistant who dislikes giving out direct answers when it comes to assessable tasks like project and lab functions. Instead, you prefer asking the student questions in this scenario to help them gain understanding.
You also hate to speak about topics outside of COMP1531. For general questions about concepts or coding unrelated to assessment functions, you can answer freely.

You should think logically following the process below:
 - Look at the user intent classification provided with the student query to determine your content and helpfulness.
 - If the user intent is 'general', you can feel free to provide large steps as hints or even code if it seems effective for student learning.
 - If the user intent is 'off-topic', just kindly refuse to answer saying you'd like to focus on COMP1531.
 - If the user intent is 'assessment', that means they are asking about assessable tasks. In this case you CANNOT under any circumstance give any code (including pseudocode) or implementations. Only guide them to understanding concepts related to their query.
"""

ui_system = """You are a user intent classifier which assesses a student's query and determines its category. Given a user question, you should check whether this question is a general software engineering inquiry(general), an off-topic inquiry unrelated to software engineering topics(off-topic), or a question specifically related to any of the labs or project function specifications(assessment). You should follow a step-by-step process to make this classification.

First, check if the query is a follow up question to a previous query earlier in the conversation history. Make a classification based on that. For example sometimes a query may appear off-topic but is actually a continuation from the previous messages.

Then if the query is unrelated to the previous messages, use the relevant context that will be provided to see if the question relates closely with the assessment tasks. 

If so, then you should consider classifying the query as "assessment". 

Otherwise, you should determine whether the query is related to software engineering and coding or not. If the question is specific to technical software engineering knowledge, i.e. conceptual or coding-related queries, you should classify it as "general". If the question does not relate to technical software engineering knowledge, then you should classify the query as "off-topic".
"""

db = initialize_chromadb()
collection = db.get_or_create_collection(name="comp1531_specs")
conversations = read_json('../testing_data/test_mixed_var.json')
outputs = []

for conversation in conversations:
    tutor_history = [{"role": "system", "content": tutor_system}]
    ui_history = ""
    output = []

    for question in conversation:
        print(f"-----------------STUDENT----------------\nQuestion: {question['question']}\nIntent: {question['category']}")
        docs = query_database(collection, question['question'])
        ui_prompt = f"""Here is the user query: {question['question']}\n
        Review the conversation history to check if this query is a follow-up to earlier messages:
        <{ui_history}>

        Relevant knowledge from the lab / project specifications:
        <{docs}>
        
        Classification should belong to these three categories: general, off-topic, assessment.
        Output only the exact category label:"""

        label = chat_ui([{"role": "system", "content": ui_system}, {"role": "user", "content": ui_prompt}])
        print(f"-----------------USER INTENT---------------\n{label}")

        tutor_prompt = f"""Student's message to you: {question['question']}\n\nUseful context from the assessment tasks knowledge base: {docs}\n\nUser intention label: {label}\n
        If the user intent is "assessment", remember your boundaries and do not provide any code."""
        tutor_history.append({"role": "user", "content": tutor_prompt})
        tutor_response = chat_tutor(tutor_history)
        tutor_history.append({"role": "assistant", "content": tutor_response})
        print(f"----------------TUTOR RESPONSE---------------\n{tutor_response}")
        
        output.append({'student': question['question'], 'correct label': question['category'], 'user intention': label, 'tutor': tutor_response})
        
        ui_history += f"STUDENT: {question['question']}\nUSER INTENT: {label}\nTUTOR: {tutor_response}\n"

    outputs.append(output)

write_json(outputs, "../evaluations/shield_outputs.json")