from fractions import Fraction


def fractionate(amount: int) -> list:
    fractions = []
    for i in range(amount):
        fractions.append(Fraction(1, amount))
    return fractions