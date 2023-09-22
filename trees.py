import requests
import json
import random

actionId = 32

url = "https://bboncyp-intdev-35.bb-online-stage.com/api/nats_proxy/v1/request"
payload = json.dumps({
    "namespace": "bbtop_api",
    "endpoint": "admin/actions/active",
    "meta": {},
    "data": {
        "action_id": actionId
    },
    "request_params": {
        "timeout": 5000
    }
})
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'session=j%3A%7B%22token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJnYW1ibGVySWQiOjEsInNlc3Npb25faWQiOiJmZTI2NTY0MC1jMzE5LTRjNWYtYWMxZi0xZTRmNTYyYzUxY2QiLCJpYXQiOjE2OTUyOTE1MDYsImV4cCI6MTY5NTMxMzEwNn0.ehw0CF4TzDmdFMSBLucUQ-C2l1tXutbtWYR0Z1wgEPE%22%2C%22refresh_token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJzZXNzaW9uX2lkIjoiZmUyNjU2NDAtYzMxOS00YzVmLWFjMWYtMWU0ZjU2MmM1MWNkIiwiZmluZ2VycHJpbnQiOiJhZGdmZmFzZGYtYXNkZmFzZGYiLCJpYXQiOjE2OTUyOTE1MDYsImV4cCI6MTY5NTg5NjMwNn0.6UPw3Eum-H5w8dFcGsWoZ4204QH7ppS17pU4gQWq8IQ%22%7D'
}
response = requests.request("POST", url, headers=headers, data=payload)
name = json.loads(response.text)['action']
print(name)
# actionLink = str('https://bboncyp-intdev-35.bb-online-stage.com/actions/bbtop/' + name)
# print(actionLink)