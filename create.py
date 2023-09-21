import requests
import json
import random

def createAction (startDate, endDate, minSum):
    url = "https://bboncyp-intdev-35.bb-online-stage.com/api/nats_proxy/v1/request"

    payload = json.dumps({
      "namespace": "bbtop_api",
      "endpoint": "admin/actions/create",
      "meta": {},
      "data": {
        "start_dttm": startDate,
        "end_dttm": endDate,
        "name": "test_" + str(random.randint(1, 1000000)),
        "min_join_sum": minSum
      },
      "request_params": {
        "timeout": 5000
      }
    })
    headers = {
      'Content-Type': 'application/json',
      'Cookie': 'session=j%3A%7B%22token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJnYW1ibGVySWQiOjEsInNlc3Npb25faWQiOiJhZmJkMmNiOC0zM2RhLTQ5M2UtODI4Yi1jNjZhZGYwZDE0MDQiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTE1NTc3NX0.6ceErbAim4aDCknXcEtX5I44l5RmkeXhZcgWOLy76BI%22%2C%22refresh_token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJzZXNzaW9uX2lkIjoiYWZiZDJjYjgtMzNkYS00OTNlLTgyOGItYzY2YWRmMGQxNDA0IiwiZmluZ2VycHJpbnQiOiJhZGdmZmFzZGYtYXNkZmFzZGYiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTczODk3NX0.CxNyLQ4g9K7KVqehKZImM1ALAJkdi8W1t6q1tOHDYR0%22%7D'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    actionId = json.loads(response.text)['action']['action_id']
    return actionId

def createTeam(actionId, teamsCount):
    teams = []
    url = "https://bboncyp-intdev-35.bb-online-stage.com/api/nats_proxy/v1/request"
    i = 1
    while i <= teamsCount:
        payload = json.dumps({
            "namespace": "bbtop_api",
            "endpoint": "admin/actions_teams/create",
            "meta": {},
            "data": {
                "team_name": "Test Team #" + str(random.randint(1, 1000000)),
                "action_id": actionId,
                "logo_url": "/images/actions/top/teams/bb.svg"
            },
            "request_params": {
                "timeout": 5000
            }
        })
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'session=j%3A%7B%22token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJnYW1ibGVySWQiOjEsInNlc3Npb25faWQiOiJhZmJkMmNiOC0zM2RhLTQ5M2UtODI4Yi1jNjZhZGYwZDE0MDQiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTE1NTc3NX0.6ceErbAim4aDCknXcEtX5I44l5RmkeXhZcgWOLy76BI%22%2C%22refresh_token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJzZXNzaW9uX2lkIjoiYWZiZDJjYjgtMzNkYS00OTNlLTgyOGItYzY2YWRmMGQxNDA0IiwiZmluZ2VycHJpbnQiOiJhZGdmZmFzZGYtYXNkZmFzZGYiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTczODk3NX0.CxNyLQ4g9K7KVqehKZImM1ALAJkdi8W1t6q1tOHDYR0%22%7D'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        newTeam = json.loads(response.text)['actions_team']['team_id']
        teams.append(newTeam)
        i += 1

    return teams

# print(createTeam(18, 16))

# matchTree = ['1', '2', '3-4', '5-7', '8-9', '10-13', '14-17']
# actionId = 18
#
# def createTrees(actionId, matchTree):
#     matchTrees = []
#     url = "https://bboncyp-intdev-35.bb-online-stage.com/api/nats_proxy/v1/request"
#     headers = {
#         'Content-Type': 'application/json',
#         'Cookie': 'session=j%3A%7B%22token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJnYW1ibGVySWQiOjEsInNlc3Npb25faWQiOiJhZmJkMmNiOC0zM2RhLTQ5M2UtODI4Yi1jNjZhZGYwZDE0MDQiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTE1NTc3NX0.6ceErbAim4aDCknXcEtX5I44l5RmkeXhZcgWOLy76BI%22%2C%22refresh_token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJzZXNzaW9uX2lkIjoiYWZiZDJjYjgtMzNkYS00OTNlLTgyOGItYzY2YWRmMGQxNDA0IiwiZmluZ2VycHJpbnQiOiJhZGdmZmFzZGYtYXNkZmFzZGYiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTczODk3NX0.CxNyLQ4g9K7KVqehKZImM1ALAJkdi8W1t6q1tOHDYR0%22%7D'
#     }
#     for match in matchTree:
#         if len(match.split('-')) == 1:
#             rangeStart = int(match)
#             rangeEnd = int(match)
#
#             payload = json.dumps({
#                 "namespace": "bbtop_api",
#                 "endpoint": "admin/match_tree/create",
#                 "meta": {},
#                 "data": {
#                     "range_start": rangeStart,
#                     "range_end": rangeEnd,
#                     "action_id": actionId
#                 },
#                 "request_params": {
#                     "timeout": 5000
#                 }
#             })
#
#             response = requests.request("POST", url, headers=headers, data=payload)
#             matchTreeId = json.loads(response.text)['match_tree']['match_tree_id']
#             matchTrees.append(matchTreeId)
#         else:
#             match = match.split('-')
#             rangeStart = match[0]
#             rangeEnd = match[1]
#
#             payload = json.dumps({
#                 "namespace": "bbtop_api",
#                 "endpoint": "admin/match_tree/create",
#                 "meta": {},
#                 "data": {
#                     "range_start": rangeStart,
#                     "range_end": rangeEnd,
#                     "action_id": actionId
#                 },
#                 "request_params": {
#                     "timeout": 5000
#                 }
#             })
#
#             response = requests.request("POST", url, headers=headers, data=payload)
#             matchTreeId = json.loads(response.text)['match_tree']['match_tree_id']
#             matchTrees.append(matchTrees)
#     return matchTrees
#
# print(createTrees(actionId, matchTree))

import json
import requests

matchTree = ['1', '2', '3-4', '5-7', '8-9', '10-13', '14-17']
actionId = 19


def createTrees(actionId, matchTree):
    matchTrees = []
    url = "https://bboncyp-intdev-35.bb-online-stage.com/api/nats_proxy/v1/request"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'session=j%3A%7B%22token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJnYW1ibGVySWQiOjEsInNlc3Npb25faWQiOiJhZmJkMmNiOC0zM2RhLTQ5M2UtODI4Yi1jNjZhZGYwZDE0MDQiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTE1NTc3NX0.6ceErbAim4aDCknXcEtX5I44l5RmkeXhZcgWOLy76BI%22%2C%22refresh_token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJzZXNzaW9uX2lkIjoiYWZiZDJjYjgtMzNkYS00OTNlLTgyOGItYzY2YWRmMGQxNDA4IiwiZmluZ2VycHJpbnQiOiJhZGdmZmFzZGYtYXNkZmFzZGYiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTczODk3NX0.CxNyLQ4g9K7KVqehKZImM1ALAJkdi8W1t6q1tOHDYR0%22%7D'
    }
    for match in matchTree:
        if len(match.split('-')) == 1:
            rangeStart = int(match)
            rangeEnd = int(match)

            payload = json.dumps({
                "namespace": "bbtop_api",
                "endpoint": "admin/match_tree/create",
                "meta": {},
                "data": {
                    "range_start": rangeStart,
                    "range_end": rangeEnd,
                    "action_id": actionId
                },
                "request_params": {
                    "timeout": 5000
                }
            })

            response = requests.request("POST", url, headers=headers, data=payload)
            response_data = json.loads(response.text)

            matchTreeId = response_data.get('match_tree', {}).get('match_tree_id')
            if matchTreeId is not None:
                matchTrees.append(matchTreeId)
        else:
            match = match.split('-')
            rangeStart = match[0]
            rangeEnd = match[1]

            payload = json.dumps({
                "namespace": "bbtop_api",
                "endpoint": "admin/match_tree/create",
                "meta": {},
                "data": {
                    "range_start": rangeStart,
                    "range_end": rangeEnd,
                    "action_id": actionId
                },
                "request_params": {
                    "timeout": 5000
                }
            })

            response = requests.request("POST", url, headers=headers, data=payload)
            response_data = json.loads(response.text)

            matchTreeId = response_data.get('match_tree', {}).get('match_tree_id')
            if matchTreeId is not None:
                matchTrees.append(matchTreeId)
    return matchTrees


print(createTrees(actionId, matchTree))
