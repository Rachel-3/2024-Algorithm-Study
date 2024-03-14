import fractions
def solution(numer1, denom1, numer2, denom2):
    answer = []
    down = denom1 * denom2
    up = int(numer1 * (down / denom1)) + int(numer2 * (down / denom2))
    print(up, down)
    Irr = fractions.Fraction(up, down)
    answer = [Irr.numerator, Irr.denominator]
    return answer