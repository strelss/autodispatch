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

    if "order_id" in r:                                                     #условие на создание заказа

        url = 'https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc'

        or_id = r[9:12]
        type_id = int(r[21:])                                                     # вытягиваем id заказа
        print(type_id)
        print(or_id)
        restart = {
            'jsonrpc': '2.0',
            'method': 'order.broadcast.send',                                      # метод для перезапуска автораспределения
            'params': {
                'order_id': or_id,
            },
            'id': 100500
        }
        print(restart)

        if type_id == 6:                                                                    #условие по type_id заказа (запуск, если =6)
            async with ClientSession() as session:
                async with session.post(url, json=restart) as res:
                    res = await res.read()
                    res = json.loads(res.decode('utf-8'))
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
