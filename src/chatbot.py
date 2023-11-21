from chatterbot import ChatBot
from chatterbot.trainers import (ListTrainer,ChatterBotCorpusTrainer)

chatbot = ChatBot('DreamCatcher')

eng_trainer = ChatterBotCorpusTrainer(chatbot)
eng_trainer.train('chatterbot.corpus.english')

convo = [
    "Hello",
    "How are you feeling today?",
    "Did you have any dreams last night? Please tell me about them:",
    "Thank you, I'll get right on that...",
    "No problem!"
]

trainer2 = ListTrainer(chatbot)
trainer2.train(convo)

# Get a response from the chatbot
response = chatbot.get_response('Hello, how are you?')

print(response)
