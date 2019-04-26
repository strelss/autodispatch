from aiohttp import web
import json
import requests


async def refunc(request):           #получаем запрос
    res = request.json()             #парсим его
    or_id = res['order_id']          #вытягиваем id заказа
    resrart = {
        'jsonrpc': '2.0',
        'method': 'order.autodispatch.restart',   #метод для перезапуска автораспределения
        'params': {
            'order_id': or_id,
        },
        'id': 100500
    }
    if res['id'] == 6:      #условие по перераспределению заказа между водителями
        result = requests.post('https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc', resrart)
    if result.json()['status'] == 1:  #проверка ответа сервера
        return web.Response(text='Заказ перераспределен.')
    else:
        return web.Response(text='Ошибка ' + result)


app = web.Application()
app.add_routes([web.post('/', refunc)])

web.run_app(app)