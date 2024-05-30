import nltk
from nltk.chat.util import Chat, reflections
from textblob import TextBlob  # for sentiment analysis
import random

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ["I'm good, thank you!", "I'm doing well, thanks for asking!"]),
    (r'what is your name?', ["I'm a chatbot created with NLTK!", "You can call me Chatbot."]),
    (r'(.*) your name(.*)', ["You can call me Chatbot.", "I'm a chatbot created with NLTK!"]),
    (r'(.*) (love|like) (you|me)', ["I'm just a chatbot, but I appreciate the sentiment!"]),
    (r'(.*) (weather|forecast)(.*)', ['Sorry, I am not programmed to check the weather.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
    (r'what can you do\?', ["I can answer your questions, engage in conversation, and provide information."]),
    (r'(.*) (age|old) (are|you)', ["I don't have an age as I'm just a program.", "I'm ageless!"]),
    (r'(.*) (thank you|thanks)(.*)', ["You're welcome!", "No problem.", "My pleasure!"]),
    (r'(.*) (help|assistance)(.*)', ["Sure, how can I assist you?", "I'm here to help!"]),
    (r'how (can|do) I contact you\?', ["You can reach out to my developer for assistance."]),
    # Additional patterns for common questions
    (r'what (can|do) you know\?', ["I have knowledge about various topics such as technology, science, and entertainment."]),
    (r'(.*) (good|great)(.*)', ["I'm glad to hear that!", "That's fantastic!"]),
    (r'(.*) (bad|not good)(.*)', ["I'm sorry to hear that. How can I help you feel better?"]),
    (r'(.*) (sad|upset)(.*)', ["I'm sorry to hear that. Would you like to talk about it?"]),
    (r'(.*) (funny|joke)(.*)', ["Sure! Why couldn't the bicycle stand up by itself? Because it was two-tired!"]),
    (r'(.*) (music|song)(.*)', ["Music is great for relaxation and inspiration. Do you have a favorite genre?"]),
    (r'(.*) (movie|film)(.*)', ["Movies are a fantastic form of entertainment. Do you have a favorite genre or movie?"]),
    (r'(.*) (book|novel)(.*)', ["Books can take you on amazing adventures. Do you have a favorite book or author?"]),
    (r'(.*) (food|eat)(.*)', ["Food is one of life's pleasures. What's your favorite cuisine?"]),
    (r'(.*) (game|play)(.*)', ["Games are a fun way to pass the time. Do you have a favorite game?"]),
    # New additional patterns
    (r'how do you do\?', ["I'm just a chatbot, so I don't 'do' in the same way humans do, but I'm here to help!"]),
    (r'(.*) (dream|dreams)(.*)', ["Dreams are fascinating! They often reflect our subconscious thoughts and emotions."]),
    (r'(.*) (hobby|hobbies)(.*)', ["Hobbies are a great way to relax and express yourself. Do you have any hobbies?"]),
    (r'(.*) (vacation|holiday)(.*)', ["Vacations are a wonderful opportunity to unwind and explore new places. Where would you like to go on your next vacation?"]),
    (r'(.*) (pets?|animals?)(.*)', ["Pets can bring so much joy into our lives. Do you have any pets?"]),
    (r'(.*) (sports?|exercise)(.*)', ["Staying active is important for both physical and mental health. Do you enjoy any sports or exercise?"]),
    (r'(.*) (technology|tech)(.*)', ["Technology is constantly evolving and shaping our world. What aspect of technology are you interested in?"]),
    (r'(.*) (education|learning)(.*)', ["Education is key to personal and professional growth. What subjects are you interested in learning more about?"]),
    (r'(.*) (history)(.*)', ["History provides valuable insights into the past and helps us understand the present. Do you have a favorite historical period or event?"]),
    (r'(.*) (art|artist)(.*)', ["Art is a beautiful form of expression. Do you have a favorite artist or art style?"]),
    (r'(.*) (health|wellness)(.*)', ["Taking care of your health is important for overall well-being. What do you do to stay healthy?"]),
]

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Determine sentiment polarity
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    else:
        return "negative"

# Custom functions
def get_random_fact():
    facts = [
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
        "The unicorn is the national animal of Scotland.",
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the metal.",
        "Bananas are berries, but strawberries are not.",
        "The Great Wall of China is not visible from space without aid."
    ]
    return random.choice(facts)

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Welcome to the Enhanced NLTK Chatbot. Type 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    else:
        # Perform sentiment analysis
        sentiment = analyze_sentiment(user_input)
        # Get the response from the chatbot
        response = chatbot.respond(user_input)
        if sentiment == "positive":
            print("Chatbot:", random.choice(["That's great to hear!", "I'm glad you're feeling positive!"]))
        elif sentiment == "negative":
            print("Chatbot:", random.choice(["I'm sorry you're feeling this way.", "I'm here to listen if you want to talk."]))
        else:
            print("Chatbot:", random.choice(["Hmm, I see.", "Interesting."]))
        print("Chatbot:", response)

