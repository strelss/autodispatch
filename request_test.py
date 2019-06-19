import requests
import json

req = {
       "jsonrpc":"2.0",
       "method":"order.state",
       "params":{
          "order_id": '509',
          "state": '6'
       },
       "id":100500
    }
req = json.dumps(req)
print(req)

###################################################################

req2 = {
       "jsonrpc":"2.0",
       "method":"order.list",
       "params":{},
       'id': 100500
    }
req2 = json.dumps(req2)
# print(req2)

req3 = {
       "jsonrpc":"2.0",
       "method":"order.autodispatch.restart",
       "params":{
              "order_id":'387'
       },
       'id': 100500
    }
req2 = json.dumps(req2)
# print(req3)

# This is connect json
# result = requests.post('https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc', req2)
# result = result.json()
# print(result)


# result = requests.post('https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc', req)
# result = result.json()
# print(result)


result = requests.post('https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc', req)
result = result.json()
print(result)