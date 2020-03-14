"""
Basic chatbot implement using chatterbot. And using wxpy create a api for wechat.

- Auto reply assigned users
- Comunicate in a low level understanding.

"""

from wxpy import Bot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot("Lynn")
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.chinese')
trainer.export_for_training('./my_export.json')
# chatbot.set_trainer(ChatterBotCorpusTrainer)
# chatbot.train("chatterbot.corpus.chinese")
bot = Bot(cache_path=True,console_qr=True)

# assign to reply single user
# my_friend = ensure_one(bot.search('Guivre'))

# watch all friends and reply
friends = bot.friends()

# group_2 = bot.groups("友谊是")[0]
# group_2.send("大家好,我是人工智障")


@bot.register(friends)
def reply_my_friend(msg):
   print(msg)
   return chatbot.get_response(msg.text).text

embed()