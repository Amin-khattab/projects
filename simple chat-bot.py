responses = {
"hello":"Wazup ma nigger ",
"how are you doing ?":"I am doing fine, nigger AYE",
"fick off bitch": "ts accent is so ahh 🥀",
"bye":"SYFM Bitch",
"nigger":"nigger"
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
            print("SHOW ME YOUR WILLY")

chatbot()
