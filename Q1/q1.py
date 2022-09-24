import math

def find_median(seq):
    seq.sort()
    n = len(seq)
    
    if n % 2 == 1:
        median = seq[math.floor(n/2)]
        return median
    else:
        x1 = seq[math.floor(n/2) - 1]
        x2 = seq[math.floor(n/2)]
        median = (x1 + x2)/2
        return median
    
input_list = list(input("Enter a set of numbers seprated by a comma(,): ").split(","))
setOfNumbers = [int(i) for i in input_list]

print(find_median(setOfNumbers))