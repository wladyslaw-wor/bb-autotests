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
def createTrees(actionId, matchTree):
    matchTrees = []
    url = "https://bboncyp-intdev-35.bb-online-stage.com/api/nats_proxy/v1/request"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'session=j%3A%7B%22token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJnYW1ibGVySWQiOjEsInNlc3Npb25faWQiOiJhZmJkMmNiOC0zM2RhLTQ5M2UtODI4Yi1jNjZhZGYwZDE0MDQiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTE1NTc3NX0.6ceErbAim4aDCknXcEtX5I44l5RmkeXhZcgWOLy76BI%22%2C%22refresh_token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxLCJzZXNzaW9uX2lkIjoiYWZiZDJjYjgtMzNkYS00OTNlLTgyOGItYzY2YWRmMGQxNDA0IiwiZmluZ2VycHJpbnQiOiJhZGdmZmFzZGYtYXNkZmFzZGYiLCJpYXQiOjE2OTUxMzQxNzUsImV4cCI6MTY5NTczODk3NX0.CxNyLQ4g9K7KVqehKZImM1ALAJkdi8W1t6q1tOHDYR0%22%7D'
    }
    for match in matchTree:
        if len(match.split('-')) == 1:
            payload = json.dumps({
                "namespace": "bbtop_api",
                "endpoint": "admin/match_tree/create",
                "meta": {},
                "data": {
                    "range_start": int(match),
                    "range_end": int(match),
                    "action_id": actionId
                },
                "request_params": {
                    "timeout": 5000
                }
            })

            response = requests.request("POST", url, headers=headers, data=payload)
            matchTreeId = json.loads(response.text)['match_tree']['match_tree_id']
            matchTrees.append(matchTreeId)
        else:
            match = match.split('-')
            rangeStart = int(match[0])
            rangeEnd = int(match[1])

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
            matchTreeId = json.loads(response.text)['match_tree']['match_tree_id']
            matchTrees.append(matchTreeId)
    return matchTrees
def createPrize(actionId):
    url = "https://bboncyp-intdev-35.bb-online-stage.com/api/nats_proxy/v1/request"
    payload = json.dumps({
        "namespace": "bbtop_api",
        "endpoint": "admin/prizes/create",
        "meta": {},
        "data": {
            "action_id": actionId,
            "match_count": 1,
            "reward_amount": 300,
            "name": str("Tractor drivers dick sucker #"+str(random.randint(1,1000000)))
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
    prizeId = json.loads(response.text)['prize']['prize_id']
    return prizeId
def createSettings(actionId, game, minBetSum, minBetCoeff):
    if game == 'dota':
        sportId = 1
    else:
        sportId = 2
    url = "https://bboncyp-intdev-35.bb-online-stage.com/api/nats_proxy/v1/request"

    payload = json.dumps({
        "namespace": "bbtop_api",
        "endpoint": "admin/actions_bets_settings/create",
        "meta": {},
        "data": {
            "action_id": actionId,
            "provider": "oddin",
            "sport_ids": [
                sportId,
                "*"
            ],
            "tournament_ids": [
                str(sportId),
                "uuid-format"
            ],
            "min_bet_sum": minBetSum,
            "min_bet_coeff": minBetCoeff
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
    settingsId = json.loads(response.text)['actions_bets_settings']['actions_bets_settings_id']
    return settingsId
def activation(actionId):
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
    return response.text
