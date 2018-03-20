import random
class Deck(object):
    def __init__(self, arrD):
        self.arrD = arrD
        random.shuffle(self.arrD)
    def deal(self):
        return self.arrD.pop(0)

class Player(Deck):
    def __init__(self, name):
        arrD =[]
        super(Player,self).__init__(arrD)
        self.points = 0
        self.name = name
    def collect(self,deck):
        self.arrD.append(deck.deal())
        return self
    def show(self):
        return super(Player,self).deal()
temp = []
game = 1
hand1,hand2 =0,0
for i in range(4):
    for j in range(2,15):
        temp.append(j)
deck = Deck(temp)
player1 = Player("player1")
player2= Player("player2")
for i in range(26):
    player1.collect(deck)
    player2.collect(deck)
while(game <27):
    hand1 = player1.show()
    hand2 = player2.show()
    print "Game",game,":"
    if(hand1 > hand2):
        print "Player1 Has won the round. Player1 Hand:", hand1,"Player2 Hand:",hand2
        player1.points+=1
        print "Score: Player1:", player1.points, "player2:",player2.points
    elif(hand1 < hand2):
        print "Player2 Has won the round. Player1 Hand:", hand1,"Player2 Hand:",hand2
        player2.points+=1
        print "Score: Player1:", player1.points, "player2:",player2.points
    elif(hand1==hand2):
        print "It is a tie. Player1 Hand:", hand1,"Player2 Hand:",hand2
    game+=1
if player1.points > player2.points:
    print "Player 1 has won with ",player1.points," !"
elif player1.points < player2.points:
    print "Player 2 has won with ",player2.points ," !"
elif player1.points == player2.points:
    print "It is a tie!"