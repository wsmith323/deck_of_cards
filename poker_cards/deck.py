from __future__ import annotations

import random

from .card import Card


class Deck:
    """
    A deck of poker-style playing cards.

    Note: Jokers are not yet implemented.
    """

    def __init__(self):
        #
        # Reverse the initial un-shuffled deck so that the more
        # efficient list.pop() (O(1)) can be used instead of list.pop(0)
        # (O(n)) when dealing a card from the "top" of the deck.
        #
        # Notes: The cards could also have been stored in an instance of
        #        collections.deque. The deque.popleft() method could
        #        then be used to efficiently deal from the "top" of the
        #        deck. However, since cards are removed from only one
        #        side of the deck, using deque seems like overkill.
        #
        #        This whole line of thinking is an example of
        #        premature optimization, given the context. The
        #        difference in efficiency between any of these
        #        techniques is so negligible as to be almost completely
        #        irrelevant.
        #
        self._cards_remaining: list[Card] = list(reversed(Card.build_all()))
        self._cards_dealt: list[Card] = []

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: id={id(self)}, remaining={len(self.cards_remaining)}"

    @property
    def cards_remaining(self) -> list[Card]:
        """Cards remaining in the deck."""
        #
        # Return a shallow copy of the internal cards list to isolate it
        # from mutations by external code. Reverse the order so that the
        # "top" of the deck is first.
        #
        return list(reversed(self._cards_remaining))

    def shuffle(self) -> None:
        """
        Shuffle the deck.

        Restore all dealt cards and randomize the deck.
        """
        #
        # TODO: Enhancement idea: Consider a keyword argument that would
        #       enable shuffling a partial deck.
        #

        # Re-seed the pseudo-random number generator to make the shuffle
        # as random as possible.
        random.seed()

        all_cards = self._cards_remaining + self._cards_dealt
        shuffled: list[Card] = []

        #
        # Note: This algorithm isn't super efficient, given the O(n)
        #       behavior of list.pop(card_index). However, given the
        #       limited number of cards, it is simple and efficient
        #       enough in this context.
        #
        #       Obviously, using random.shuffle() would be preferable,
        #       but that is explicitly forbidden by the project
        #       requirements.
        #
        max_index = len(all_cards) - 1
        while all_cards:
            card_index = random.randint(0, max_index)
            card = all_cards.pop(card_index)
            shuffled.append(card)
            max_index -= 1

        self._cards_remaining = shuffled
        self._cards_dealt = []

        return None

    def deal_one_card(self) -> Card | None:
        """
        Deal a card from the top of the deck.

        Return a single Card object, or None if all cards have been
        dealt.
        """
        try:
            #
            # The "top" of the deck is only relevant before the deck
            # has been shuffled. The initial un-shuffled deck has been
            # reversed so that the more efficient list.pop() can be used
            # instead of list.pop(0). See comment in __init__().
            #
            card = self._cards_remaining.pop()
        except IndexError:
            return None
        else:
            self._cards_dealt.append(card)
            return card
