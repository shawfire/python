"""util.cards package"""


def new_deck() -> list[str]:
    """Return a new deck of cards

    Returns:
        list[str]: A list of cards in a deck.
    """
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    houses = ['♣', '♥', '♦', '♠']

    # deck = []
    # for card in cards:
    #   for house in houses:
    #     deck.append(card + house)

    # Same as above using List Comprehensions
    deck = [card + house for card in cards for house in houses]
    return deck
