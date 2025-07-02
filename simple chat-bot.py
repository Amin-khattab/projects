responses = {
"hello":" hello there how are you doing BTW ?",
"how are you doing ?":" iam doing alright, thanks for asking.",
"i have a question": "",
"bye":"",
"":""
}

def chatbot():

    print("if you want to exit type 'exit'")
    while True:
        user_input = input("Chatbot: lets a have a little chat shall we ?")
        if user_input.lower() == 'exit':
            print("this chat is over ")
            break

        for key in responses:
            if key in user_input or user_input in key:
                print(f"chatbot:{responses[key]}")
                break

        else:
            print("didnt get that sorry.")

chatbot()
