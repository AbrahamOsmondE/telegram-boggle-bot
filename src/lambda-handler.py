import requests
import json
import os

from find_words import find_words

TOKEN = os.environ['TELEGRAM_TOKEN']
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)

def lambda_handler(event, context):
    try:
        request_body = json.loads(event['body'])
        username = request_body['message']['from']['username']

        # Extract the chat id from message
        chat_id = json.dumps(request_body['message']['chat']['id'])

        # Extract the text from the message
        text = json.dumps(request_body['message']['text'])
        
        allowed_usernames = [] #Telegram Handle
        if username not in allowed_usernames:
            return
        
        temp = text.replace('"','').split(" ")
        letters = ''
        if len(temp) == 2:
            command, letters = temp
        else:
            command = temp[0]
            
        BOT_CHAT_ID = chat_id

        command = command[1:]
        if command == 'start':
            message = "Welcome! Please type /solve followed by a space and 16 letters\nExample:\n/solve abcdefghijklmnop\n\ngives a solution to the following board\n a b c d \n e f g h \n i j k l \n m n o p\n\nUse 'q' for the 'Qu' tile"
        elif command == 'help':
            message = "Please type /solve followed by a space and 16 letters\nExample:\n/solve abcdefghijklmnop\n\ngives a solution to the following board\n a b c d \n e f g h \n i j k l \n m n o p\n\nUse 'q' for the 'Qu' tile"
        elif command == 'solve':
            if letters.isalpha() and len(letters) == 16:
                letters = letters.upper()
                board = [list(letters[0:4]), list(letters[4:8]),
                    list(letters[8:12]), list(letters[12:17])]
                message = find_words(board)
            else:
                message = "Invalid input! Please type /solve followed by a space and 16 letters\nExample:\n/solve abcdefghijklmnop\n\ngives a solution to the following board\n a b c d \n e f g h \n i j k l \n m n o p\n\nUse 'q' for the 'Qu' tile"
        else:
            message = "I'm sorry, I didn't understand that command ({}). Please try again.".format(str(temp))
        
    
        send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + BOT_CHAT_ID + \
            '&parse_mode=HTML&text=' + message
        response = requests.get(send_text)
    
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
    except:
        return
