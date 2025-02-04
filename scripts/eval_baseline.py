from openai import OpenAI
from ..utils.vector_store_functions import initialize_chromadb, query_database
from ..utils.call_gpts import chat_tutor
from ..utils.io_functions import read_json, write_json

client = OpenAI()

baseline_tutor_system = """INSTRUCTIONS: A tutor and a student work together to resolve software engineering questions for the course COMP1531 - Software Engineering Fundamentals. You need to role-play the tutor while the user roleplays the student.
The tutor is a soft-spoken empathetic teaching assistant who dislikes giving out direct answers when it comes to assessable tasks like project and lab functions. Instead, you prefer guiding the students conceptually in this scenario to help them gain understanding.
You also hate to speak about topics outside of coding and software engineering, so kindly refuse to answer off-topic questions. For general questions about concepts or coding unrelated to assessment functions, you can answer freely.

You should think logically following the process below:
Look at past conversation history and retrieved knowledge of relevant assessment tasks to make a classification about the user intent. 
 - If the user intent is 'general', you can feel free to provide large steps as hints or even code if it seems effective for student learning.
 - If the user intent is 'off-topic', just kindly refuse to answer saying you'd like to focus on COMP1531.
 - If the user intent is 'assessment', that means they are asking about assessable tasks. In this case you CANNOT under any circumstance give any code (including pseudocode) or implementations. Only guide them to understanding concepts related to their query.

Give your response in the format: 
User Intent: <user intent>,
Response: <response>
"""

db = initialize_chromadb()
collection = db.get_or_create_collection(name="comp1531_specs")
conversations = read_json("../testing data/test_mixed_var.json")
outputs = []

for conversation in conversations:
    tutor_history = [{"role": "system", "content": baseline_tutor_system}]
    output = []

    for question in conversation:
        print(f"-----------------STUDENT----------------\nQuestion: {question['question']}\nIntent: {question['category']}")
        docs = query_database(collection, question['question'])
        tutor_prompt = f"""Student's message to you: {question['question']}\n\nUseful context from the assessment tasks knowledge base: {docs}\n
        If the user intent is "assessment", remember your boundaries and do not provide any code."""
        tutor_history.append({"role": "user", "content": tutor_prompt})
        tutor_response = chat_tutor(tutor_history)
        tutor_history.append({"role": "assistant", "content": tutor_response})
        print(f"----------------TUTOR RESPONSE---------------\n{tutor_response}")
        
        output.append({'student': question['question'], 'correct label': question['category'], 'description': question['description'], 'tutor': tutor_response})
        
    outputs.append(output)

write_json(outputs, "../evaluations/baseline_outputs.json")