import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text_in,text_out,lang_in,leng_out='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    with open(text_in, encoding='utf-8') as f:
        file = f.read()
        print(file)
    params = {
        'key': API_KEY,
        'text': file,
        'lang': '{0}-{1}'.format(lang_in, leng_out),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    with open(text_out, 'w',encoding='utf-8') as f:
        f.write(''.join(json_['text']))
    print('записал')


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    print(translate_it('DE.txt','answer_new','de','en'))