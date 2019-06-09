def karatsuba(num1, num2):
    """Multiplies two binary numbers in the form of lists using Karatsuba method.

    Parameters
    ----------
    num1 : list
        List of numbers representing a binary number to multiply.
    num2 : list
        List of numbers representing a binary number to multiply.

    Returns
    -------
    answer : list
        The result of the multiplication. 
    """

    if (len(num1) < 2) or (len(num2) < 2):
        return [x*y for x,y in zip(num1, num2)]

    # split the digit sequences in the middle 
    len1 = len(num1)
    len2 = len(num2)

    high1 = num1[:len1//2]
    low1 = num1[len1//2:]
    high2 = num2[:len2//2]
    low2 = num2[len2//2:]

    # 3 calls made to numbers approximately half the size
    z0 = karatsuba(low1, low2)
    z1 = karatsuba([sum(x) for x in zip(low1, high1)], [sum(x) for x in
    zip(low2, high2)])
    z2 = karatsuba(high1, high2)

    z3 = [x-y for x,y in zip(z1, z2)]
    z = [x-y for x,y in zip(z3, z0)]

    answer = z2 + z + z0

    return answer

def gradeschool(num1, num2):
    """Multiplies two binary numbers in the form of lists using traditional method.

    Parameters
    ----------
    num1 : list
        List of numbers representing a binary number to multiply.
    num2 : list
        List of numbers representing a binary number to multiply.

    Returns
    -------
    answer : list
        The result of the multiplication. 
    """

    if (len(num1) < 2) or (len(num2) < 2):
        return [x*y for x,y in zip(num1, num2)]

    # split the digit sequences in the middle 
    len1 = len(num1)
    len2 = len(num2)

    high1 = num1[:len1//2]
    low1 = num1[len1//2:]
    high2 = num2[:len2//2]
    low2 = num2[len2//2:]

    # 3 calls made to numbers approximately half the size
    z0 = gradeschool(low1, low2)
    z1 = gradeschool(high1, low2)
    z2 = gradeschool(high1, high2)
    z4 = gradeschool(low1, high2)
    
    z = [x+y for x,y in zip(z1, z4)]

    answer = z2 + z + z0

    return answer

def karatsuba_thresh(num1, num2, t):
    """Multiplies two binary numbers in the form of lists using Karatsuba method
    with a threshold.

    Parameters
    ----------
    num1 : list
        List of numbers representing a binary number to multiply.
    num2 : list
        List of numbers representing a binary number to multiply.
    t : integer
        Threshold for when to use gradeschool or karatsuba method.

    Returns
    -------
    answer : list
        The result of the multiplication. 
    """

    if (len(num1) < 2) or (len(num2) < 2):
        return [x*y for x,y in zip(num1, num2)]

    # split the digit sequences in the middle 
    len1 = len(num1)
    len2 = len(num2)

    high1 = num1[:len1//2]
    low1 = num1[len1//2:]
    high2 = num2[:len2//2]
    low2 = num2[len2//2:]

    # 3 calls made to numbers approximately half the size
    z0 = threshold(low1, low2, t)
    z1 = threshold([sum(x) for x in zip(low1, high1)], [sum(x) for x in
    zip(low2, high2)], t)
    z2 = threshold(high1, high2, t)

    z3 = [x-y for x,y in zip(z1, z2)]
    z = [x-y for x,y in zip(z3, z0)]
    answer = z2 + z + z0

    return answer

def threshold(num1, num2, t):
    """Decides whether to use karatsuba or gradeschool multiplciation based on
    threshold.

    Parameters
    ----------
    num1 : list
        List of numbers representing a binary number to multiply.
    num2 : list
        List of numbers representing a binary number to multiply.
    t : integer
        Threshold for when to use gradeschool or karatsuba method.

    Returns
    -------
    answer : list
        The result of the multiplication. 
    """

    if len(num1) < t:
        answer = gradeschool(num1,num2)
    else:
        answer = karatsuba_thresh(num1, num2, t)

    return answer
    
