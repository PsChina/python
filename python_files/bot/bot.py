# BotToken 2104778875:AAHEHCZmR4TutSaoRWHR216V0u5dx9giZOI
import re
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json
import random

TASK_GROUP_ID = '-762260539'


def resolveJson(path):
    with open(path, 'r', encoding='utf8') as fp:
        return json.load(fp)


def saveJson(path, data):
    with open(path, "w") as f:
        json.dump(data, f)


jsonData = resolveJson('./data.json')


humanMap = {}

textArray = [
    "Can you calculate what {0} plus {1} equals?",
    "Can you calculate what {0} minus {1} equals?",
    "Can you calculate what {0} multiplied by {1} equals?",
    "Can you calculate what {0} divided by {1} equals?"
]

oprationArray = ['+', '-', '*', '/']


def generative_math_problem(user_id):

    num1 = random.randint(0, 99)
    num2 = random.randint(1, 99)

    opration = random.randint(0, 3)

    result = 0

    if opration == 3:
        while num1 % num2 != 0:
            num1 = random.randint(0, 99)
            num2 = random.randint(1, 99)

    if opration == 0:
        result = num1 + num2
    elif opration == 1:
        result = num1 - num2
    elif opration == 2:
        result = num1 * num2
    elif opration == 3:
        result = int(num1 / num2)

    humanMap[user_id] = {
        "num1": num1,
        "num2": num2,
        "operation": oprationArray[opration],
        "text": textArray[opration].format(num1, num2),
        "answer": str(result),
        "user_id": user_id,
        "is_ok": False,
        "step": 0
    }

    return humanMap[user_id]


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text' and chat_type == 'private':
        user_id = str(msg['from']['id'])
        text = msg['text']
        if text == '/start':
            bot.sendMessage(
                chat_id, '1.Welcome to Waykichain Family! The WaykiChain is focused on developing its own technology, bottom public chain layer and as well corresponding to that an ecosystem which will foster technology research and development, as well as project operation. We also have strong community support. In 2022, we will hold football matches all over the world, and we will continue to report. There will also be a lot of rewards issued during the event, don\'t miss it! Please answer the question carefully. Make sure you fill in the information after completing all tasks, otherwise it will be invalid information.\
                    Twitter：https://twitter.com/wayki_chain\
                    Telegram：https://t.me/WICCWorldCupOfficial\
                    Whitepaper：https://www.waykichain.com/Whitepaper-en.pdf\
                    Website：https://www.waykichain.com/\
                    \
                    New airdrop: Waykichain (WICC)\
                    Reward: 5000 WICC for 1000 participants\
                    Rate: ⭐️⭐️⭐️⭐️⭐️\
                    \
                    End date: 20th December, 2021 UTC 2am\
                    Distribution: within 14 days after airdrop ends\
                    \
                    Join Telegram group https://t.me/WICCWorldCupOfficial\
                    Follow Twitter https://twitter.com/wayki_chain\
                    Reweet the pin message\
                    Fill the airdrop link\
                    ', reply_markup=ReplyKeyboardMarkup(keyboard=[
                    [KeyboardButton(text='/start')]
                ]))
        res = bot.getChatMember(TASK_GROUP_ID, user_id)
        status = res['status']
        if status != 'left':
            if user_id in humanMap:
                dialogue = humanMap[user_id]
                if dialogue['is_ok']:
                    if dialogue['step'] == 0:
                        bot.sendMessage(
                            chat_id, 'What is your Twitter username?', reply_markup=ReplyKeyboardMarkup(keyboard=[
                                [KeyboardButton(text='/start')],
                            ]))
                        dialogue['step'] = 1
                    elif dialogue['step'] == 1:
                        try:
                            data = jsonData[user_id]
                        except:
                            jsonData[user_id] = {'telegramName': '', 'twitterName': text, 'isFollowedWaykichainTwitte': False, 'isRetweetedTwitte': False, 'address': '',
                                                 'address': '', 'email': '', 'country': ''}
                            bot.sendMessage(
                                chat_id, 'Where are you from? (Country here)')
                        else:
                            data['twitterName'] = text
                            data['telegramName'] = msg['from']['username']
                            bot.sendMessage(
                                chat_id, 'Where are you from? (Country here)')
                        dialogue['step'] = 2
                    elif dialogue['step'] == 2:
                        data = jsonData[user_id]
                        data['country'] = text
                        bot.sendMessage(
                            chat_id, 'What is your email address?')
                        dialogue['step'] = 3
                    elif dialogue['step'] == 3:
                        data = jsonData[user_id]
                        if re.search(r'^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_\-]+)+$', text, re.M | re.I) or re.search(r'^[A-Za-z0-9\u4e00-\u9fa5\.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', text, re.M | re.I):
                            data['email'] = text
                            bot.sendMessage(
                                chat_id, 'Have you followed Waykichain Twitter？(Yes or No)', reply_markup=ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='YES'),
                                     KeyboardButton(text='NO')]
                                ]))
                            dialogue['step'] = 4
                        else:
                            bot.sendMessage(
                                chat_id, 'Wrong email address, and fill it again!')
                    elif dialogue['step'] == 4:
                        data = jsonData[user_id]
                        if text == 'YES':
                            data['isFollowedWaykichainTwitte'] = True
                            bot.sendMessage(
                                chat_id, 'Have you retweeted the waykichain’s pin message in Twitter? (Yes or No)', reply_markup=ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='YES'),
                                     KeyboardButton(text='NO')]
                                ]))
                            dialogue['step'] = 5
                        else:
                            bot.sendMessage(
                                chat_id, 'Failed, Please follow the Twitter (https://twitter.com/wayki_chain) , and fill in again! ', reply_markup=ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='/start')],
                                ]))
                            dialogue['step'] = 0
                    elif dialogue['step'] == 5:
                        data = jsonData[user_id]
                        if text == 'YES':
                            data['isRetweetedTwitte'] = True
                            bot.sendMessage(
                                chat_id, 'Please give me you Waykichain wallet address.', reply_markup=ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='/start')],
                                ]))
                            dialogue['step'] = 6
                        else:
                            bot.sendMessage(
                                chat_id, 'Failed, Please retweet the pin message in Twitter (https://twitter.com/wayki_chain) , and fill in again! ', reply_markup=ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='/start')],
                                ]))
                            dialogue['step'] = 0
                    elif dialogue['step'] == 6:
                        data = jsonData[user_id]
                        if re.search(r'^W[a-zA-Z\d]{33}$', text, re.M):
                            data['address'] = text
                            saveJson('./data.json', jsonData)
                            bot.sendMessage(
                                chat_id, 'Thank you for your participation, the airdrop will be end on 20TH December, 2021 UTC 2am. And reward will be sent within 14 days after airdrop closed.', reply_markup=ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='/start')],
                                ]))
                            dialogue['step'] = 7
                        else:
                            bot.sendMessage(
                                chat_id, 'Wrong Waykichain wallet address, and fill it again!', reply_markup=ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='/start')],
                                ]))
                else:
                    dialogue['is_ok'] = text == dialogue['answer']
                    if dialogue['is_ok']:
                        bot.sendMessage(
                            chat_id, 'What is your Twitter username?', reply_markup=ReplyKeyboardMarkup(keyboard=[
                                [KeyboardButton(text='/start')],
                            ]))
                        dialogue['step'] = 1
                    else:
                        bot.sendMessage(chat_id, 'error')
                        dialogue = generative_math_problem(user_id)
                        bot.sendMessage(
                            chat_id, dialogue['text'], reply_markup=ReplyKeyboardMarkup(keyboard=[
                                [KeyboardButton(text='/start')],
                            ]))
            else:
                dialogue = generative_math_problem(user_id)
                bot.sendMessage(chat_id, dialogue['text'], reply_markup=ReplyKeyboardMarkup(keyboard=[
                                [KeyboardButton(text='/start')],
                                ]))
        else:
            bot.sendMessage(
                chat_id, 'Sorry you can\'t participate because you didn\'t join https://t.me/+mUY-bGOuhOxlN2U9.\nIf you have any questions, you can follow the link below.\ntwitter link ：https://twitter.com/wayki_chain\nwebsite link：https://www.waykichain.com/\ntelegram link：https://t.me/WICCWorldCupOfficial\nwhitepaper link：https://www.waykichain.com/Whitepaper-en.pdf')


TOKEN = '2104778875:AAHEHCZmR4TutSaoRWHR216V0u5dx9giZOI'


bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)


# Welcome to Waykichain! If you have any questions, you can follow the link below.
# twitter link ：https://twitter.com/wayki_chain
# website link：https://www.waykichain.com/
# telegram link：https://t.me/WICCWorldCupOfficial
# whitepaper link：https://www.waykichain.com/Whitepaper-en.pdf
