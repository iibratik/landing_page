import requests
from .models import TeleSettings

token = '6088654827:AAG6_AKNzuybcuXub0EKkjjNQHv4eQPjEi4'
chat_id = '-968190460'
text = 'i`ll be back'

def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'


        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            first_l = text.find('{')
            first_r = text.find('}')
            last_l = text.rfind('{')
            last_r = text.rfind('}')

            part_1 = text[0:first_l]
            part_2 = text[first_r+1:last_l]
            part_3 = text[last_r:-1]

            text_slice = part_1 + tg_name+ part_2 + tg_phone + part_3
        else:
            text_slice = text
        try:
            req = requests.post(method, data={
            'chat_id': chat_id,
            'text': text_slice

        })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Все окей, сообщение отправлено!')
    else:
         pass
