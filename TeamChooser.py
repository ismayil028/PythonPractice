from random import choice

teams = []
players = []
file = open('teams.txt', 'r')
teams = file.read().splitlines()
file = open('players.txt', 'r')
players = file.read().splitlines()
print(players)

teamA = []
teamB = []

while len(players) > 0:

    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    if len(players) != 0:
        playerB = choice(players)
        teamB.append(playerB)
        players.remove(playerB)

print(choice(teams), '-', end=' ')
for i in teamA:
    print(i, end=' ')

print('\n')
print(choice(teams), '-', end=' ')
for x in teamB:
    print(x, end=' ')
print('\n')
