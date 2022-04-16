def function_that_is_too_long(n: int):
    """
    Honestly, who knows why this function exists?
    """
    # let's not bother with zero or negative integers
    if n < 1:
        return 0

    # convert the input to a binary string, because
    pow = 0
    while 2 ** pow < n:  # ** means exponent, for the uninitiated
        pow += 1
    pow -= 1  # go back to the largest power that was smaller than n

    binary_string = ""
    while pow >= 0:
        if 2 ** pow <= n:
            binary_string += "1"
            n -= 2 ** pow
        else:
            binary_string += "0"
        pow -= 1

    # get every other digit of the binary string, for reasons
    every_other = ""
    for i in range(0, len(binary_string), 2):
        every_other += binary_string[i]

    # sum up the resulting string, and return that
    res = sum(
        int(digit) for digit in every_other
    )  # this is some sneaky Python called a "comprehension" - it's basically a condensed for loop
    return res
  
  