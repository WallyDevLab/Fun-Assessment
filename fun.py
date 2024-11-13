import math

def dog_years():
    
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """
    calculated_age = 0
    dog_age = int(input("Input a dog's age in human years: "))
    for i in range(1, dog_age + 1):
        if i > 0 and i <=2: 
            calculated_age += 10.5
        elif i > 2:
            calculated_age += 4
        else:
            pass
    #enter your code here
    print(f"The dog's age in dog's years is {int(calculated_age)}")

def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """
    #enter your code here
    _str = ""
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            _str += "FizzBuzz "
        elif i % 3 == 0:
            print("Fizz")
            _str += "Fizz "
        elif i % 5 == 0:
            print("Buzz")
            _str += "Buzz "
        else:
            print(i)
            _str += f"{i} "    

    return _str.strip()
def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:    for word in sentence.split():
            _dict[word] = len(word)
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    #enter your code here
    _dict = {}
    if isinstance(sentence, str): 
        for word in sentence.split():
            _dict[word] = len(word)
    else: 
        raise ValueError
    return _dict

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    #enter your code here
    _sum = 0
    str_num = str(number)
    for num in str_num:
        _sum += math.pow(int(num), 3)
    return int(_sum)

cube_sum(-123)