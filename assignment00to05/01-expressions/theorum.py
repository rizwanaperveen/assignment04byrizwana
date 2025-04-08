import math

def theorum():
    pq = float(input("Enter the value of pq: "))
    qr = float(input("Enter the value of qr: "))
    rp = math.sqrt(pq**2 + qr**2)

    print("The length of the rp (hypotenuse) is:", rp)

if __name__ == "__main__":
    theorum()