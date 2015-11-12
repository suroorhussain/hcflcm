def gcd(n1, n2) :
    """ Finds the GCD (or HCF) of two numbers using the Euclidean algorithm"""
    if n1 > n2 :
        x, y = n1, n2
        
    elif n1 < n2:
        x, y = n2, n1

    else :
        print "Both numbers are equal : %d" % n1
    while y != 0 :
        x, y = y, x % y
    return x

def lcm(n1, n2) :
    """Uses the formula num1 * num2 = LCM * GCD"""
    return (n1 * n2)/gcd(n1, n2)

num1 = int(raw_input("Enter first number"))
num2 = int(raw_input("Enter second number"))
print "The GCD and LCM of %d and %d are \n \t*GCD: %d \n\t*LCM: %d" % (num1, num2, gcd(num1, num2), lcm(num1, num2))
