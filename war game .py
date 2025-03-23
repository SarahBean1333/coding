import random

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
suits = ["D", "H", "C", "S"]
weights = { "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "10" : 10,
            "J" : 11,
            "Q" : 12,
            "K" : 13,
            "A" : 14}
PlayingCardWeight = 1
PlayingCardFace = 0

def createDecks(shuffle_count):
    global cards
    global suits
    global weights
    global PlayingCardFace
    global PlayingCardWeight

    deck = []
    for suit in suits:
        for card in cards:
            deck.append(["{}{}".format(card, suit), weights[card]])

    for i in range(shuffle_count):
        random.shuffle(deck)

    players = [[],[]]
    for i in range(len(deck)):
        players[i % 2].append(deck[i]) 
    return players   
def doWar(player_deck1, player_deck2, war_count):
    player1_flip = None
    player2_flip = None
    risk_cards = []
 if len(player_deck1) < war_count + 1:
    risk_cards.extend(player_deck1.copy())
    player_deck1.clear()
    player2_flip = player_deck2[-1]
elif len(player_deck2) < war_count + 1:
    risk_cards.extend(player_deck2.copy())
    player_deck2.clear()
    player1_flip = player_deck1[-1]
if len(player_deck1) and len(player_deck2):
for i in range(war_count):
            risk_cards.append(player_deck1.pop())
            risk_cards.append(player_deck2.pop())
 player1_flip = player_deck1.pop()
        player2_flip = player_deck2.pop()
        risk_cards.extend([player1_flip, player2_flip])
 while player1_flip and player2_flip and (player1_flip[PlayingCardWeight] == player2_flip[PlayingCardWeight]):
        print("Continuation War")
        player1_flip, player2_flip, risk = doWar(player_deck1, player_deck2, war_count)
        risk_cards.extend(risk)
return player1_flip, player2_flip, risk_cards

def prependCards(deck, cards):
cards.reverse()
    for card in cards:
        deck.insert(0,card)
# Create the player decks
players = createDecks(7)
# Track number of turns
turns = 0
# Artificial limit in case there are no winners by this number
max_turns = 4000
while len(players[0]) and len(players[1]):
    turns += 1
    if turns >= max_turns:
        break

    p1Card = players[0].pop()
    p2Card = players[1].pop()

    current_cards = [p1Card, p2Card]
    print("P1 = {}, P2 = {}".format(p1Card[PlayingCardFace],p2Card[PlayingCardFace]))
    if p1Card[PlayingCardWeight] > p2Card[PlayingCardWeight]:
        prependCards(players[0], current_cards) 
    elif p2Card[PlayingCardWeight] > p1Card[PlayingCardWeight]:
        prependCards(players[1], current_cards) 
    else:
        print("War")
        # Cards are equal, doWar() and see who wins
        p1, p2, risk = doWar(players[0], players[1], 3)

        winner_list = None
        if not p1 or (p2 and p1[PlayingCardWeight] < p2[PlayingCardWeight]) :
            winner_list = players[1]
        elif not p2 or (p1 and p1[PlayingCardWeight] > p2[PlayingCardWeight]) : 
            winner_list = players[0]

        # Winner gets risk cards and current cards
        prependCards(winner_list, risk) 
        prependCards(winner_list, current_cards) 
winner = None
if len(players[0]) and len(players[1]):
    if len(players[0]) > len(players[1]):
        winner = "Player 1"
    else: 
        winner = "Player 2"
else:
    winner = "Player 1" if len(players[0]) > 0 else "Player 2"

print("{} won the game in {} turns".format(winner, turns))
print(len(players[0]), len(players[1]))