import requests
import json

# req = {
#        "jsonrpc":"2.0",
#        "method":"order.state",
#        "params":{
#           "order_id":12344,
#           "state":2
#        },
#        "id":100500
#     }
# req = json.dumps(req)
# print(req)

req2 = {
       "jsonrpc":"2.0",
       "method":"message.send.personal",
       "params":{
          "driver_id":int(11),
          "text":str('test'),
          # "title":str('test'),
          # "message":str('test'),
          # "timeout":int(3)
       },
       "id":100500
    }
req2 = json.dumps(req2)
print(req2)

# This is connect json
result = requests.post('https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc', req2)
# response = json.loads(result)
print(result.json())

# # This is connect API
# result = requests.get('http://api-demo-kiev.ligataxi.com/api/v1/client/company/')
# print(result)


# # This is connect json and API
# result = requests.post('https://vs:191ebefa672a7c8ac21417dcb5319b01@api-demo-kiev.ligataxi.com/rpc', {
#     "jsonrpc": "2.0",
#     "method": "user.session.authorize",
#     "params": {
#         "session_uuid": "f73cc552-f6a6-4db4-aaba-a6ed35310da5",
#     },
#     "id": 1
# })
# # response = json.loads(result)
# print(result.json())

# This is connect json
# result = requests.post('https://http://localhost:8080', req)
#
# print(result)
