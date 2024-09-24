import os
import random

os.system("cls")

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck: 
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards 
    
    @staticmethod
    def create_deck():
        cards = []
        suits = ["♠", "♥", "♣", "♦"] 
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

        for suit in suits:
            for value in values:
                cards.append(Card(suit, value))
        random.shuffle(cards)  
        return cards
    
    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()  
        else:
            return None  


deck = Deck(Deck.create_deck())


while True:
    user_input = input("Tryck enter för att dra ett kort eller 'q' för att avsluta: ").lower()

    if user_input == 'q':  
        print("Du har avslutat spelet.")
        break

    drawn_card = deck.draw_card()

    if drawn_card:
        print(f"Draget kort: {drawn_card}")
    else:
        print("Kortleken slut.")
        break
