# input fractions
fraction1, fraction2 = input("Enter the fractions(eg: '2/6+2/6' -no spaces) : ").split("+")

# Seprate Fractions into Numerators and Denomenators
num1, den1 = map(int, list(fraction1.split("/")))

num2, den2 = map(int, list(fraction2.split("/")))

# Function for finding the Highest Common Factor of two numbers

def findHCF(n1, n2):
    hcf = 0
    for i in range(1, int(min(n1, n2)) + 1):
        if n1 % i == 0 and n2 % i == 0:
            hcf = i
    return hcf

# Add Fractions

lcm = (den1 * den2) // findHCF(den1, den2)

sum = (num1 * (lcm // den1)) + (num2 * (lcm // den2))

# Reduce the sum to the lowest indivisible state

ansNum = sum // findHCF(sum, lcm)

ansLCM = lcm // findHCF(sum, lcm)

print(num1, "/", den1, " + ", num2, "/", den2, " = ", ansNum, "/", ansLCM)
