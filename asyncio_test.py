import asyncio                                                          #импорт библиотек
import aiohttp
from aiohttp import ClientSession
import json
from time import time

async def read_resp(url, session):                                      #функция создания запроса и обработки ответа
    resrart = {                                                         #параметры с ключами на получение order.list
       "jsonrpc":"2.0",
       "method":"order.list",
       "params":{
          # "filters":'1',
          # "sort":'id',
          # "limit": 50,
          # "offset": 0
          # "timeout":int(3)
       },
       'id': 100500
    }
    print(resrart)

    async with session.post(url, json=resrart) as response:             #отправка запроса и получение ответа
        data = await response.read()                                    #чтение ответа
        data = json.loads(data.decode('utf-8'))                         #декодировка ответа в utf-8, парсинг json
        print(data['result'][0]['type_id'])                            #вытягиваем type_id

async def main():
    url = 'https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc'  # урл с апи ключем
    async with aiohttp.ClientSession() as session:                                      #открытие сессии

        task = asyncio.create_task(read_resp(url, session))                             #создание таска
        await asyncio.gather(task)                                                      #кидаем в очередь read_resp(url, session)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())                                                                 #запуск исполнения программы
    t = time() - t0
    print('Прошло ' + str(t) + ' секунд.')
