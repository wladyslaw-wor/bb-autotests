import requests
import json

def authorization():
  url = "https://bboncyp-intdev-35.bb-online-stage.com/api/auth/login"

  payload = json.dumps({
    "phone": "79061112233",
    "password": "12345678",
    "is_wrong_data_auth_support": True,
    "fingerprint": "adgffasdf-asdfasdf",
    "ga_id": "123.456",
    "ym_id": "789.101",
    "captcha_key": "",
    "g-recaptcha-response": ""
  })
  headers = {
    'x-access-token': '',
    'Content-Type': 'application/json',
    'Cookie': 'session=j%3A%7B%22token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJnYW1ibGVySWQiOjEsInNlc3Npb25faWQiOiJhZmJkMmNiOC0zM2RhLTQ5M2UtODI4Yi1jNjZhZGYwZDE0MDQiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTE1NTc3NX0.6ceErbAim4aDCknXcEtX5I44l5RmkeXhZcgWOLy76BI%22%2C%22refresh_token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJzZXNzaW9uX2lkIjoiYWZiZDJjYjgtMzNkYS00OTNlLTgyOGItYzY2YWRmMGQxNDA0IiwiZmluZ2VycHJpbnQiOiJhZGdmZmFzZGYtYXNkZmFzZGYiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTczODk3NX0.CxNyLQ4g9K7KVqehKZImM1ALAJkdi8W1t6q1tOHDYR0%22%7D'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  token = json.loads(response.text)['token']
  return token

# print(authorization())