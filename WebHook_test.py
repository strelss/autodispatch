import aiohttp
import asyncio
import json
from aiohttp import web
from aiohttp import ClientSession

url = 'https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc'


WH = {                                                         #параметры с ключами на получение order.list
       "jsonrpc":"2.0",
       "method":"webhook.order",
       "params":{
           "order_id":"11",
           "webhook_id":""
       },
       'id': 100500
    }

async def WebHooks_reqest(url, WH):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=WH) as response:             #отправка запроса и получение ответа
            data = await response.read()                                    #чтение ответа
            data = json.loads(data.decode('utf-8'))                         #декодировка ответа в utf-8, парсинг json
            print(data)


if __name__ == '__main__':
    asyncio.run(WebHooks_reqest(url, WH))