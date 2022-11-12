import csv
import random

#Program that takes a csv file of players and a csv file teams to create a sweepstake

# Import teams from CSV file
file = open("list.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()

teamlist =[]

for i in range(0, len(data)):
    teamlist.append(data[i][0])

teamlist.sort()
random.shuffle(teamlist)

#Import players from csv files
file = open("players.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()

playerlist =[]
for i in range(0, len(data)):
    playerlist.append(data[i][0])
playerlist.sort()

#create a dictionary to hold teams and players
drawsheet = {}
for i in teamlist:
    drawsheet[i] = None

for i in range(0, 2):
    playerlist.extend(playerlist)

for key in drawsheet:
    if len(drawsheet) > 0:
        drawsheet[key] = playerlist.pop(0)

#write the draw to a csv file
with open('mycsvfile.csv', 'w') as f:
    for key in drawsheet.keys():
        f.write("%s, %s\n" % (key, drawsheet[key]))

print(drawsheet)
