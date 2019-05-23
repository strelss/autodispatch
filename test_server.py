import aiohttp
import asyncio                                                          #импорт библиотек
from aiohttp import web
from aiohttp import ClientSession
import json


async def read_resp(url, session):                                      #функция создания запроса и обработки ответа
    resrart = {                                                         #параметры с ключами на получение order.list
       "jsonrpc":"2.0",
       "method":"order.list",
       "params":{},
       'id': 100500
    }
    print(resrart)

    async with session.post(url, json=resrart) as response:             #отправка запроса и получение ответа
        data = await response.read()                                    #чтение ответа
        data = json.loads(data.decode('utf-8'))                         #декодировка ответа в utf-8, парсинг json
        print(data)                                                     #вывод в консоль ответа
        await refunc(data)

async def refunc(data):
    or_id = data['result'][0]['order_id']
    type_id = data['result'][0]['type_id']                              # вытягиваем id заказа
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
    url = 'https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc'
    if type_id == 6:                                                                    #условие по type_id заказа (запуск, если =6)
        await autodisp(url, restart)                                                    #запуск функции для запроса на перераспределение заказа
    else:
        print('Нет заказов для перераспределения.')

async def autodisp(url, restart):                                                       #функция перераспределения заказа

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


async def main():
    url = 'https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc'  # урл с апи ключем
    async with aiohttp.ClientSession() as session:                                      #открытие сессии

        task = asyncio.create_task(read_resp(url, session))                             #создание таска
        await asyncio.gather(task)                                                      #кидаем в очередь read_resp(url, session)

app = web.Application()
app.add_routes([web.post('/', refunc)])


if __name__ == '__main__':
    # web.run_app(app)
    asyncio.run(main())                                                                 #запуск исполнения программы

