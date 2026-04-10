from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import random
import re

quote = ["Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
        "Do. Or do not. There is no try.",
        "The greatest teacher, failure is.",
        "Train yourself to let go of everything you fear to lose.",
        "In a dark place we find ourselves, and a little more knowledge lights our way."
        ]

responses_intent = {
"greeting":" hello there, how are you doing BTW",
"asking_status":" i am doing alright, thanks for asking.",
"asking_question": "question away i am here to help you",
"goodbye":"see you later !",
"fall_back":"didn't get that sorry."
}

corpus = ["Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening", "What's up", "How's it going", "Nice to see you", "Greetings",
          "How are you", "How are you doing", "How's it going", "What's up", "How do you feel", "How are things", "How's everything", "Are you okay", "How have you been", "What's your status",
          "I have a question", "Can I ask something", "I want to ask", "May I ask", "I need to ask you something", "Can you help me", "I'm wondering", "Could you tell me", "I'd like to know", "Can you answer this",
          "Bye", "Goodbye", "See you later", "See you", "Take care", "Catch you later", "Until next time", "Farewell", "See ya", "Talk to you later",
          "asdfgh", "123456", "xyzabc", "qwerty", "blahblah", "random stuff", "!!!???", "hfjdksl", "999", "typing gibberish"]

labels = ["greeting", "greeting", "greeting", "greeting", "greeting", "greeting", "greeting", "greeting", "greeting", "greeting"
    ,"asking_status", "asking_status", "asking_status", "asking_status", "asking_status", "asking_status", "asking_status", "asking_status", "asking_status", "asking_status"
    ,"asking_question", "asking_question", "asking_question", "asking_question", "asking_question", "asking_question", "asking_question", "asking_question", "asking_question", "asking_question"
    ,"goodbye", "goodbye", "goodbye", "goodbye", "goodbye", "goodbye", "goodbye", "goodbye", "goodbye", "goodbye"
    ,"fall_back", "fall_back", "fall_back", "fall_back", "fall_back", "fall_back", "fall_back", "fall_back", "fall_back", "fall_back"]

CV = CountVectorizer()
x_train = CV.fit_transform(corpus)
classifeir = LogisticRegression(random_state=0)
classifeir.fit(x_train,labels)

def chatbot():

    print("if you want to exit type 'exit'")
    while True:
        user_input = input("Chatbot: lets a have a little chat shall we ?")
        if user_input.lower() == 'exit':
            print("this chat is over ")
            break

        if user_input.lower() == "quote":
            rand = random.choice(quote)
            print(f"chatbot: {rand}")
            continue

        user_vec = CV.transform([user_input])
        intent = classifeir.predict(user_vec)[0]
        response = responses_intent.get(intent)

        if response:
            print(f"chatbot: {response}")
        else:
            print(f"chatbot: {responses_intent['fall_back']}")

chatbot()
