import nltk
import random
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Sample responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bunch of code, but I'm doing great!", "All systems go!", "Feeling chatty today!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure I understand.", "Can you rephrase that?", "Interesting... tell me more."]
}

lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

def get_response(user_input):
    tokens = preprocess(user_input)
    for word in tokens:
        if word in responses:
            return random.choice(responses[word])
    return random.choice(responses["default"])

# Chat loop
print(" Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if 'bye' in user_input.lower():
        print("🤖 Chatbot:", random.choice(responses["bye"]))
        break
    response = get_response(user_input)
    print("🤖 Chatbot:", response)



