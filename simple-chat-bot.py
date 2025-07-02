import random

quote = ["Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
        "Do. Or do not. There is no try.",
        "The greatest teacher, failure is.",
        "Train yourself to let go of everything you fear to lose.",
        "In a dark place we find ourselves, and a little more knowledge lights our way."
        ]

responses = {
"hello":" hello there how are you doing BTW ?",
"how are you doing ?":" iam doing alright, thanks for asking.",
"i have a question": "question away i am here to help you",
"bye":"see you later !"
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
        for key in responses:
            if key in user_input or user_input in key:
                print(f"chatbot:{responses[key]}")
                break
        else:
            print("didn't get that sorry.")

chatbot()

