import sys
import math

class Player:
    def __init__(self, p_id):
        self.p_id = p_id
        self.card_his = []
        self.infection_his = []

    def use_card(self, Card):
        self.card_his.append(Card.name)


class Card:
    def __init__(self, data):
        self.name = data["name"]
        self.condense = data["condense"]
        self.turn = data["turn"]



def main():
    pass


if __name__ == "__main__":
    main()