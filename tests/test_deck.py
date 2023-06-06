from __future__ import annotations

from unittest import TestCase

from poker_cards import Card, Deck


class TestDeck(TestCase):
    """Test the Deck class."""

    @classmethod
    def setUpClass(cls: TestDeck) -> None:
        cls.all_cards = Card.build_all()

    def setUp(self) -> None:
        self.deck = Deck()

    def test_deck_init(self):
        """Verify deck initialization."""
        self.assertEqual(len(self.all_cards), Card.ALL_COUNT)
        self.assertEqual(self.deck.cards_remaining, self.all_cards)

    def test_shuffle_order(self):
        """Verify that shuffle() re-orders cards with each call."""
        cards_1 = self.deck.cards_remaining

        self.deck.shuffle()

        cards_2 = self.deck.cards_remaining

        self.assertEqual(len(cards_2), Card.ALL_COUNT)
        self.assertNotEqual(cards_2, cards_1)

        self.deck.shuffle()

        cards_3 = self.deck.cards_remaining

        self.assertEqual(len(cards_3), Card.ALL_COUNT)
        self.assertNotEqual(cards_3, cards_2)
        self.assertNotEqual(cards_3, cards_1)

    def test_deal_one_card(self):
        """Verify all cards are dealt properly."""

        #
        # Verify all cards are dealt in ORIGINAL order if deck is not
        # shuffled.
        #
        dealt_list_original = []

        for _ in range(Card.ALL_COUNT):
            card = self.deck.deal_one_card()

            self.assertIsInstance(card, Card)
            self.assertIsInstance(card.suite, Card.Suite)
            self.assertIsInstance(card.face_value, Card.FaceValue)

            dealt_list_original.append(card)

        self.assertEqual(dealt_list_original, self.all_cards)

        for _ in range(3):
            # Verify any further calls return None.
            self.assertIsNone(self.deck.deal_one_card())

        #
        # Verify all cards are dealt in some other order after deck is
        # shuffled.
        #
        self.deck.shuffle()

        dealt_list_other = []

        for _ in range(Card.ALL_COUNT):
            card = self.deck.deal_one_card()

            self.assertIsInstance(card, Card)
            self.assertIsInstance(card.suite, Card.Suite)
            self.assertIsInstance(card.face_value, Card.FaceValue)

            dealt_list_other.append(card)

        self.assertEqual(len(dealt_list_other), Card.ALL_COUNT)
        self.assertNotEqual(dealt_list_other, dealt_list_original)

        for _ in range(3):
            # Verify any further calls return None.
            self.assertIsNone(self.deck.deal_one_card())
