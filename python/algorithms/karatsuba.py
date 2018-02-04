from math import floor

def karatsuba(num1, num2,min_recur=10):
    """Multiplies two numbers recursively using the
    karatsuba Algorithm

    Optional argument: nim_recur (int)
                    minimum value below which to stop recursing
    """
    if num1 < min_recur or num2 < min_recur:
        return num1 * num2
    n1=len(str(num1))
    n2=len(str(num2))
    n=min(n1,n2)
    a=int(floor(num1/(2 ** (n/2+1))))
    b=int(num1-a*(2 ** (n/2+1)))
    c=int(floor(num2/(2 ** (n/2+1))))
    d=int(num2-c*(2 ** (n/2+1)))
    z0=int(karatsuba(b,d))
    z2=int(karatsuba(a,c))
    z1=int(karatsuba(a+b,c+d)-z2-z0) 
    return z0 + z1 * 2 ** (n/2+1) + z2 * 2 ** (2*(n/2+1))
