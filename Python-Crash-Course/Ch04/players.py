#list slicing
players = ['adam', 'michael', 'john', 'henry', 'tod']
print(players[0:3])
print(players[:4])
print(players[2:])

print("Here are the first three names of my team")
for player in players[:3]:
    print(player.title())