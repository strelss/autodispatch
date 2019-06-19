import aiohttp
import asyncio                                                          #импорт библиотек
from aiohttp import web
from aiohttp import ClientSession
import json
from urllib.parse  import parse_qs
from urllib.parse  import urlparse

async def hello(request):                                                   #функция приема и обработки запроса
    print("Incoming request")
    print(request)
    r = await request.read()                                                #чтение запроса
    r = r.decode("utf-8")                                                   #перекодировка запроса
    r1 = urlparse(r)
    # print(r1)
    r1 = parse_qs(r)
    # print(r1)

    if "order_id" in r1:                                                     #условие на создание заказа

        url = 'https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc'

        or_id = r1['order_id'][0]
        stat_id = int(r1['status_id'][0])                                                     # вытягиваем id заказа
        print(stat_id)
        print(or_id)


        if stat_id == 6:                                                                    #условие по stat_id заказа (запуск, если =6)
            restart = {
                'jsonrpc': '2.0',
                'method': 'order.broadcast.send',                                                  # метод для отправки в свободный эфир
                'params': {
                    'order_id': or_id,
                },
                'id': 100500
            }
            print(restart)
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
            print('Нет заказов для восстановления.')
    else:
        pass

    return web.Response(text='ok')

app = web.Application()
app.add_routes([web.post('/', hello)])

if __name__ == '__main__':
    web.run_app(app)
