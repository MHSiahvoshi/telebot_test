"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'A':
        return 1
    elif int(card) in numbers:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    elif value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two


def value_of_ace(card_one, card_two):
    ace_card = 0
    if card_one == 'A' or card_two == 'A':
        ace_card = 11
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    summ = value_of_card(card_one) + value_of_card(card_two) + ace_card
    if summ >= 11:
        return 1
    elif summ < 11:
        return 11


def is_blackjack(card_one, card_two):
    ace_card = 0
    card_one_flag = False
    card_two_flag = False
    help_flag = False
    if card_one == 'A':
        ace_card = 11
        card_one_flag = True
    elif card_two == 'A':
        ace_card = 11
        card_two_flag = True
    else:
        help_flag = True
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if card_one_flag or help_flag:
        summ = value_of_card(card_two) + ace_card
        if summ == 21:
            return True
        else:
            return False
    if card_two_flag or help_flag:
        summ = value_of_card(card_one) + ace_card
        if summ == 21:
            return True
        else:
            return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    summ = value_of_card(card_one) + value_of_card(card_two)
    if summ == 9 or summ == 10 or summ == 11:
        return True
    else:
        return False
