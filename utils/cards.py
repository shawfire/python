# pylint: disable=line-too-long
"""utils.cards package

>>> new_deck()
['2♣', '2♥', '2♦', '2♠', '3♣', '3♥', '3♦', '3♠', '4♣', '4♥', '4♦', '4♠', '5♣', '5♥', '5♦', '5♠', '6♣', '6♥', '6♦', '6♠', '7♣', '7♥', '7♦', '7♠', '8♣', '8♥', '8♦', '8♠', '9♣', '9♥', '9♦', '9♠', '10♣', '10♥', '10♦', '10♠', 'J♣', 'J♥', 'J♦', 'J♠', 'Q♣', 'Q♥', 'Q♦', 'Q♠', 'K♣', 'K♥', 'K♦', 'K♠', 'A♣', 'A♥', 'A♦', 'A♠']
"""
# pylint: enable=line-too-long



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
