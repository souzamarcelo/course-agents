import random

class Agent:
    def __init__(self, _cards):
        self.cards = _cards

    def step(self, environment):
        number, suit = self.sense(environment)
        return self.act(number, suit)

    def sense(self, environment):
        number = environment.split('_')[0]
        suit = environment.split('_')[1]
        return number, suit

    def act(self, number, suit):
        for card in self.cards:
            if self.disposable(card, number, suit):
                return self.dispose(card)
        return None

    def disposable(self, card, number, suit):
        c_number = card.split('_')[0]
        c_suit = card.split('_')[1]
        return (number == c_number or suit == c_suit)

    def dispose(self, card):
        self.cards.remove(card)
        return card


agent = None
shown_card = None
stack = None

def setup():
    global agent, shown_card, stack
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['P', 'C', 'E', 'O']
    all_cards = []
    for number in numbers:
        for suit in suits:
            all_cards.append(number + '_' + suit)
    
    random.shuffle(all_cards)
    agent = Agent(all_cards[:5])
    shown_card = all_cards[5]
    stack = all_cards[6:]

def step():
    global agent, shown_card, stack
    environment = shown_card
    action = agent.step(environment)
    print(shown_card, '-->', agent.cards, ' --> ', action)
    if action is not None:
        shown_card = action
    else:
        agent.cards.append(stack.pop())

setup()
while len(agent.cards) > 0 and len(stack) > 0:
    step()

if len(agent.cards) == 0:
    print('AGENT WINS:', len(stack), 'POINTS!')
else:
    print('AGENT LOSES', len(agent.cards), 'NEGATIVE POINTS!')