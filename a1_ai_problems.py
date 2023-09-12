# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

def is_palindrome(s):
    # Your code here
    s1 = s.replace(" ", "")
    s2 = s1.upper()
    if (s2 == s2[::-1]):
            return True
    else:
        return False
# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("taco cat"))  # True
print(is_palindrome("hello"))  # False

# Temperature Conversion
def temp_conversion():
    s = input("Choose a starting temperature unit F or C: ")
    i = float(input("What is your starting temperature?: "))
    s = s.upper()
    choice = ""
    if (s == "F"):
        choice = "Celcius"
        i = (i - 32) * (5/9)
    if (s == "C"):
        choice = "Fahrenheit"
        i = (i * 9/5) + 32
    print(f"Your converted temperature is {i} degrees {choice}")
temp_conversion()

def are_anagrams(str1, str2):
    # Your code here
    s1 = str1.replace(" ", "").upper()
    s2 = str2.replace(" ", "").upper()
    anagram = True
    for char in s1:
            if not (char in s2):
                 anagram = False
    return anagram                 




# Test cases
assert are_anagrams("listen", "silent") == True
assert are_anagrams("triangle", "integral") == True
assert are_anagrams("hello", "world") == False

# Additional test cases
assert are_anagrams("Dormitory", "Dirty Room") == True
assert are_anagrams("Astronomer", "Moon starer") == True
assert are_anagrams("abc", "def") == False

print("All assertions passed!")

