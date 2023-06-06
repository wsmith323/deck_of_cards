from __future__ import annotations

from unittest import TestCase

from poker_cards import Card


class TestCard(TestCase):
    """Test the Card class."""

    def test_build_all(self):
        """Verify content and ordering of .build_all() results."""

        card_iterator = iter(Card.build_all())

        #
        # Intentionally avoid re-use of code from the code under test in
        # order to avoid "self-fulfilling prophecy" behavior.
        #
        for expected_suites, ordering_func in [
            ((Card.Suite.SPADE, Card.Suite.DIAMOND), lambda sequence: sequence),
            (
                (Card.Suite.CLUB, Card.Suite.HEART),
                lambda sequence: sorted(sequence, key=lambda item: item.value, reverse=True),
            ),
        ]:
            for expected_suite in expected_suites:
                for expected_face_value in ordering_func(Card.FaceValue):
                    card: Card = next(card_iterator)

                    self.assertEqual(card.suite, expected_suite)
                    self.assertEqual(card.face_value, expected_face_value)

        # Make sure there are no more cards
        with self.assertRaises(StopIteration):
            next(card_iterator)
