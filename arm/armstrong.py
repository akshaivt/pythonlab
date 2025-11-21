def is_armstrong(num):
    """check whether a number is an armstrong number."""
    digits=str(num)
    power=len(digits)
    total=sum(int(digits)**power for digits in digits)
    return total==num

