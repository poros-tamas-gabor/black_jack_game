kartya_szinek = ["Pikk", "Káró", "Treff", "Kőr"]
kartya_dict = {"Kettő": 2, "Három": 3, "Négy": 4, "Öt": 5, "Hat": 6, "Hét": 7, "Nyolc": 8, "Kilenc": 9, "Tíz": 10, "Bubi": 10, "Dáma": 10, "Király": 10, "Ász": 11}
kartya_magassag = list(kartya_dict.keys())
import random

class Card():
    def __init__(self, szin, magassag):
        self.szin = szin
        self.magassag = magassag
        self.value = kartya_dict[magassag]
    
    def __str__(self):
        return str(self.szin) + " " + str(self.magassag)

class Deck():
    def __init__(self):
        self.cards = []
        for szin in kartya_szinek:
            for magassag in kartya_magassag:
                self.cards.append(Card(szin, magassag))
    
    def __str__(self):
        string = ""
        for element in self.cards:
            string += element.__str__() + "\n"
        return string
    
    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        """
        Shuffle the deck
        """
        return random.shuffle(self.cards)

    def deal(self):
        """
        Return the last card from the deck
        """
        dealed_card = self.cards.pop()
        return dealed_card

class Hand():
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        string = ""
        for element in self.cards:
            string += element.__str__() + "\n"
        return string

    def add_card(self,card):
        self.cards.append(card)
    
    def value(self):
        value = 0
        for element in self.cards:
            value += element.value
        return value

    

    def print_dealer(self):
        string = ""
        for i in range(len(self.cards)):
            if i == 0:
                string += self.cards[0].__str__() + "\n"
            else:
                string += "<Hidden Card>" + "\n"
        return string

class Money():
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0
    
    def take_bet(self, bet):
        self.bet = bet
    
    def loose_bet(self):
        self.total -= self.bet
        self.bet = 0
     
    def win_bet(self):
        self.total += self.bet
        self.bet = 0

def player_wins(player_hand,dealer_hand,money):
    print("YOU WIN! ")
    print("Your hand was: ")
    print(player_hand)
    print("Dealer hand was: ")
    print(dealer_hand)
    money.win_bet()

def dealer_wins(player_hand,dealer_hand,money):
    print("YOU LOOSE! ")
    print("Your hand was: ")
    print(player_hand)
    print("Dealer hand was: ")
    print(dealer_hand)
    money.loose_bet()

if __name__ == "__main__":
    deck = Deck()
    proba_hand = Hand()
    proba_hand.add_card(deck.deal())
    print(deck.deal().value)
    print(proba_hand)
    print(proba_hand.value())