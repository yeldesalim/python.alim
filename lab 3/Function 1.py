#Python Function 1

from itertools import permutations
import random

#Ex.1
def recipe(grams):
      ounces = grams / 28.3495231
      print(ounces)

recipe(230)

#Ex.2
import math

def fahrenheit(celsius):
      formula_conversion = (celsius * 9/5) + 32
      print(formula_conversion)

fahrenheit(math.trunc(40))

#Ex.3
def solve(numheads, numlegs):
  legs = 2 * numheads
  extra_legs = numlegs - legs
  rabbits = extra_legs/2
  chickens = numheads - rabbits
  print("rabbits:", rabbits, "chickens:", chickens)

user_input=int(input())
solve(user_input)

#Ex.4
some_list = list(map(int, input().split()))
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

result = [num for num in some_list if is_prime(num)]
print(result)

#Ex.5
def permut(some_str):
  print(list(permutations(some_str)))
user_input = input()
permut(user_input)

#Ex.6
def reverse(list):
  print(*list[::-1])
user_input = input()
list = user_input.split()
reverse(list)

#Ex.7
nums=input().split()
some_list=[int(num) for num in nums]

def has_33(n):
    for i in range(1, len(n)):
        if n[i]==3 and n[i-1]==3:
            return True
    return False

if has_33(some_list):
    print("True")
else:
    print("False")

#Ex.8
nums = input().split()
some_list = [int(num) for num in nums]
def spy_game(n):
    for i in range(1, len(n)):
        if n[i] == 0:
            for j in range(i + 1, len(n)):
                if n[j] == 7:
                    break
                elif n[j] == 0:
                    for k in range(j + 1, len(n)):
                        if n[k] == 7:
                            return True
    return False
if spy_game(some_list):
    print("True")
else:
    print("False")

#Ex.9
def the_volume(radius):
    print(4/3*3.14*radius**3)
user_input = int(input())
the_volume(user_input)

#Ex.10
nums = input().split()
some_list = [int(num) for num in nums]

def unique_list(n):
    for i in range(0, len(n)):
        if n[i] == n[i-1]:
            pass
        else:
            print(n[i], end=' ')
unique_list(some_list)

#Ex.11
user_input = input()
my_list = user_input.split()
def is_palindrome(list):
    if list == list[::-1]:
        print("It is palindrome")
    else:
        print("It is not")
is_palindrome(my_list)

#Ex.12
nums = input().split()
my_list=(int(num) for num in nums)

def histogram(n):
  for i in n:
    print("*" * i)
histogram(my_list)

#Ex.13
userName=input("Hello! What is your name? \n")
guessNumber = random.randint(1, 20)
print("Well,", userName, ", I am thinking of a number between 1 and 20. \nTake a guess.")
userInput=int(input())

def is_answer(num, numOfg):

  numOfg+=1

  if num>guessNumber:
        print("Your guess is too great \nTake a guess")
        inp=int(input())
        is_answer(inp, numOfg)

  elif num<guessNumber:
        print("Your guess is too low \nTake a guess")
        inp=int(input())
        is_answer(inp, numOfg)

  else:
        print("Good job,", userName+"!", "You guessed my number in", numOfg, "guesses!")
        
is_answer(userInput, 0)