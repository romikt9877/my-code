import random

class Human:
    name = ""
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

class Player(Human):
    pass
    team = ""
    def setTeam(self, team_name):
        self.team = team_name

    def getTeam(self):
        return self.team

names = [
    "حسین",
    "مازیار",
    "اکبر",
    "نیما",
    "مهدی",
    "فرهاد",
    "محمد",
    "خشایار",
    "میلاد",
    "مصطفی",
    "امین",
    "سعید",
    "پویا",
    "پوریا",
    "رضا",
    "علی",
    "بهزاد",
    "سهیل",
    "بهروز",
    "شهروز",
    "سامان",
    "محسن",
]

players = []

team = "A"
for i in range(0, 22):
    if i > 10:
        team = "B"
    
    player = Player()
    random_index = random.randint(0, len(names) - 1)
    player.setName(names[random_index])
    player.setTeam(team)
    names.pop(random_index)

    players.append(player)

for player in players:
    print(player.getName(), "team:", player.getTeam())
