# Poker Cards

This package provides classes that represent poker-style playing cards.

### Card

The `Card` class represents a poker-style card.


```python
from poker_cards import Card

# The Card class contains enums for suites and face values.
print(Card.Suite.HEART.name)  # "HEART"
print(Card.FaceValue.KING.value)  # 13

# A Card instance is created by calling the class with Suite and Value arguments.
card = Card(suite=Card.Suite.SPADE, face_value=Card.FaceValue.ACE)

# The suite and value enums are available as attributes on the Card instance.
print(card.suite.name)  # "SPADE"
print(card.face_value.name)  # "ACE"
print(card.face_value.value)  # 1

# A class method is provided to build a list of all possible cards. The list is
# in "New Deck Order" (see https://ambitiouswithcards.com/new-deck-order/).
print(len(Card.build_all()))  # 52
```

### Deck

The `Deck` class represents a deck of `Card` objects.

```python
from poker_cards import Card, Deck

# A Deck instance is created by calling the class without arguments.
deck = Deck()

# Initially, the contents of the deck are in "New Deck Order"
# (see https://ambitiouswithcards.com/new-deck-order/). They are NOT randomized.

# The deck can be randomized by calling:
deck.shuffle()

# Retrieving a card from the top of the deck, or "dealing", is accomplished like
# so:
card = deck.deal_one_card()
assert isinstance(card, Card)

# Repeated calls to `.deal_one_card()` will return unique cards until the deck
# is empty. Once empty, further calls will return None. 

# At any point, the remaining cards in the deck can be retrieved like so:
cards = deck.cards_remaining
assert len(cards) <= 52
if cards:
    assert isinstance(cards[0], Card)

# To rebuild and randomize the deck, just call `.shuffle()` again. After that,
# `.deal_one_card()` can again be repeatedly called until the deck is empty.
```
