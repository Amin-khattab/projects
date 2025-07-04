import random
import re

quote = ["Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
        "Do. Or do not. There is no try.",
        "The greatest teacher, failure is.",
        "Train yourself to let go of everything you fear to lose.",
        "In a dark place we find ourselves, and a little more knowledge lights our way."
        ]

responses = {
r"\b(hi|hello)\b":" hello there, how are you doing BTW",
r"how\s*are\s*you\s*doing\??":" iam doing alright, thanks for asking.",
r"i\s*have\s*a\s*question\??": "question away i am here to help you",
r"\b(bye|goodbye)\b":"see you later !"
}

def chatbot():

    print("if you want to exit type 'exit'")
    while True:
        user_input = input("Chatbot: lets a have a little chat shall we ?")
        if user_input.lower() == 'exit':
            print("this chat is over ")
            break

        if user_input == "quote":
            rand = random.choice(quote)
            print(f"chatbot: {rand}")
            continue
        for pattern,response in responses.items():
            if re.search(pattern,user_input,re.IGNORECASE):
                print(f"chatbot: {response}")
                break
        else:
            print("didn't get that sorry.")

chatbot()
