def simple_chatbot(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here and ready to assist you!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase or ask something else?"

print("Hello welcome to my Simple ChatBot. It can take only three inputs 'Hello' , 'How are you' , 'Bye' ")
print("You can go out of the program by entering 'exit'")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)