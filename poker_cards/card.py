from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, unique


@dataclass(frozen=True)
class Card:
    """
    A poker-style playing card.

    Two arguments are required:
     - suite: a Card.Suite object
     - value: a Card.Value object
    """

    @unique
    class Suite(IntEnum):
        """Poker-style playing card suites."""

        SPADE = 1
        DIAMOND = 2
        CLUB = 3
        HEART = 4

        @property
        def face_values(self):
            """The face values for this suite, in New Deck Order."""
            sorted_kwargs = dict(key=lambda item: item.value)

            if self in {self.CLUB, self.HEART}:
                sorted_kwargs |= dict(reverse=True)

            return sorted(Card.FaceValue, **sorted_kwargs)

    @unique
    class FaceValue(IntEnum):
        """Poker-style playing card face values."""

        ACE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        JACK = 11
        QUEEN = 12
        KING = 13

    suite: Suite
    face_value: FaceValue

    ALL_COUNT = len(Suite) * len(FaceValue)

    @classmethod
    def build_all(cls) -> list[Card]:
        """
        Build all possible cards.

        Return a list of Card objects, one for every unique combination
        of Card.Suite and Card.FaceValue.

        Note: Cards are returned in New Deck Order.
              See: https://ambitiouswithcards.com/new-deck-order/
        """

        return [
            cls(suite=suite, face_value=face_value)
            for suite in sorted(cls.Suite, key=lambda item: item.value)
            for face_value in suite.face_values
        ]

    #
    # TODO: Enhancement idea: Add comparison magic methods.
    #       Note: Depending on the card game, the Ace may be
    #             the lowest or highest card. Consider adding an
    #             additional, optional, Card field that controls
    #             Ace comparison behavior.
    #
