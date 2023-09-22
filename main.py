import authorization as auth
import create as c

# Parameters for new test action
startDate = "2023-10-16 10:10:10"
endDate = "2023-10-22 10:10:10"
minSum = 1000
teamsCount = 19
matchTree = ['1', '2', '3-4', '5-7', '8-9', '10-13', '14-17']
# game = 'dota'
game = 'cs'
minBetSum = 1000
minBetCoeff = 1.9

token = auth.authorization()
actionId = c.createAction(startDate, endDate, minSum)
print('Создана акция ID: ', actionId)
teamsIds = c.createTeam(actionId, teamsCount)
print('В акцию ', actionId, ' добавлены команды ID: ', teamsIds)
treesIds = c.createTrees(actionId, matchTree)
print('В акцию ', actionId, ' добавлены сетки ID: ', treesIds)
prizeId = c.createPrize(actionId)
print('В акцию ', actionId, ' добавлен приз ID: ', prizeId)
settingsId = c.createSettings(actionId, game, minBetSum, minBetCoeff)
print('В акцию ', actionId, ' добавлены настройки ID: ', settingsId)
c.activation(actionId)
print('Акция активирована')


