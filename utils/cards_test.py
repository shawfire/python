"""cards_test package

To invoke pytest with double verbose flag to ensure that the expected value 
is printed in full when there is an error:
pytest -vv
"""

from utils.cards import new_deck


def test_new_deck():
    """ Test new_deck() """
    assert new_deck() == [
        '2♣', '2♥', '2♦', '2♠', '3♣', '3♥', '3♦', '3♠', '4♣', '4♥', '4♦', '4♠',
        '5♣', '5♥', '5♦', '5♠', '6♣', '6♥', '6♦', '6♠', '7♣', '7♥', '7♦', '7♠',
        '8♣', '8♥', '8♦', '8♠', '9♣', '9♥', '9♦', '9♠', '10♣', '10♥', '10♦',
        '10♠', 'J♣', 'J♥', 'J♦', 'J♠', 'Q♣', 'Q♥', 'Q♦', 'Q♠', 'K♣', 'K♥',
        'K♦', 'K♠', 'A♣', 'A♥', 'A♦', 'A♠']
