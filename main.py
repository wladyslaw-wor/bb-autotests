import authorization as auth
import create as c

# Parameters for new test action
startDate = "2023-10-16 10:10:10"
endDate = "2023-10-22 10:10:10"
minSum = 1000
teamsCount = 19
matchTree = ['1', '2', '3-4', '5-7', '8-9', '10-13', '14-17']
game = 'dota'
# game = 'cs'


token = auth.authorization()
actionId = c.createAction(startDate, endDate, minSum)
teams = c.createTeam(actionId, teamsCount)
