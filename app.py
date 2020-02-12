# -*- coding: utf-8 -*-
# File: Alan__Bot
# Author: Alain Nishimwe <nishimwealain6l@gmail.com>
# CreateDate: 05-01-2020

# imports of Libraries

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

# Bot creation

englishBot = ChatBot("Chatterbot",
                     storage_adapter="chatterbot.storage.SQLStorageAdapter",
                     database_uri='postgres://qypsqxybdpchcm:db85da014b5272a205530c236357c98cb6f422623a1aa81d4a747230f1589d57@ec2-35-172-85-250.compute-1.amazonaws.com:5432/d846gbk4k4cot0
',
                     logic_adapters=[
                         {
                             'import_path': 'chatterbot.logic.BestMatch',
                             'default_response': 'I am sorry, but I do not understand.',
                             'maximum_similarity_threshold': 0.60
                         }])

# training the bot for cavendish admission
# trainer.train("chatterBot.corpus.english.greetings")

trainer = ChatterBotCorpusTrainer(englishBot)

trainer.train("./corpus/")

# Now we can export the data to a file
trainer.export_for_training('./conversations/User_Bot_conversations.json')

# define app routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
# function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))


if __name__ == "__main__":
    app.run()
