from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards = []

    @property
    def count(self):
        return len(self.cards)

    def add(self, card):
        if self.find(card.name):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        card_to_remove = self.find(card)
        self.cards.remove(card_to_remove)

    def find(self, name):
        for card in self.cards:
            if card.name == name:
                return card