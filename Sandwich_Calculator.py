#Nate Glod
#Demetrios Yackovetsky
#Sandwich_Calculator.py
#Calculates the number of unique bread-only sandwiches within a loaf of bread that has n slices
#A unique sandwich is formed when any ingredients are added or removed from the current sandwich,
#or any inside ingredient is moved outside of the outside-most bread slice (one of the ends change)

import math

#Preliminary non-summation operations for sandwich calculation number
def calculator(n):
    if n<=1:
        return n
    else:
        return n + (math.factorial(n)/(math.factorial(n-2)*2)*Sandwich_Loop(n))

#Summation for sandwich numbers
def Sandwich_Loop(n):
    i = 0
    summation = 0
    while(i<=n-2):
        summation += math.factorial(n-2)/(math.factorial(i)*math.factorial(n-i-2))
        i += 1
    return summation

def main():
    print("Maximum number you can input and still get a useful answer is 1007")
    while(True):
        try:
            n = int(input("Input the number of bread slices in the loaf (Enter non-int number to quit): "))
            print(n, ":", calculator(n))
        except:
            break
    print("Invalid input.")

if __name__ == "__main__":
    main()
