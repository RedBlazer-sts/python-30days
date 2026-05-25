from groq import Groq
import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
def chat():
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_input,
        }
    ],
    model="llama-3.3-70b-versatile",
    )
    print(chat_completion.choices[0].message.content)


while True:
    user_input=  input("Chat with us (q -> quit) : ")
    
    if user_input == "q":
        break
    chat()



