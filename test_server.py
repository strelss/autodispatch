import aiohttp
import asyncio                                                          #импорт библиотек
from aiohttp import web
from aiohttp import ClientSession
import json

async def hello(request):                                                   #функция приема и обработки запроса
    print("Incoming request")
    print(request)
    r = await request.read()                                                #чтение запроса
    r = r.decode("utf-8")                                                   #перекодировка запроса
    print(r)

    if r == 'create_new_order':                                             #условие на создание заказа

        url = 'https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc'

        resrart = {                                                         #параметры с ключами на получение order.list
           "jsonrpc":"2.0",
           "method":"order.list",
           "params":{},
           'id': 100500
        }
        print(resrart)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=resrart) as response:             #отправка запроса и получение ответа
                data = await response.read()                                    #чтение ответа
                data = json.loads(data.decode('utf-8'))                         #декодировка ответа в utf-8, парсинг json
                print(data)                                                     #вывод в консоль ответа

        or_id = data['result'][0]['order_id']
        type_id = data['result'][0]['type_id']                                  # вытягиваем id заказа
        print(type_id)
        print(or_id)
        restart = {
            'jsonrpc': '2.0',
            'method': 'order.autodispatch.restart',                                      # метод для перезапуска автораспределения
            'params': {
                'order_id': or_id,
            },
            'id': 100500
        }

        if type_id == 6:                                                                    #условие по type_id заказа (запуск, если =6)
            async with ClientSession() as session:
                async with session.post(url, json=restart) as res:
                    res = await res.read()
                    res = json.loads(res.decode('utf-8'))
                    print(res)
                    if 'error' in res:
                        print('Произошла ошибка: ' + str(res['error']))
                    elif 'result' in res:
                        print('Статус заказа: ' + str(res['result']))
                    else:
                        pass
        else:
            print('Нет заказов для перераспределения.')

    elif r == 'pass':                                                                       #Условие по отмене заказа
        print('Заказ был отменен.')

    else:
        pass

    return web.Response(text='ok')

app = web.Application()
app.add_routes([web.post('/', hello)])

if __name__ == '__main__':
    web.run_app(app)
