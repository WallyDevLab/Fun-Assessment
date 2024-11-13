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

    #enter your code here

    human_years = int(input("Input a dog's age in human years: "))

    if human_years <= 2:
        dog_year = human_years * 10.5
    if human_years > 2:
        dog_year = (10.5 * 2) + ((human_years - 2) * 4)
    
    return f"The dog's age in dog's years is {int(dog_year)}"

print(dog_years())

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

    output = ""

    for i in range(1, num + 1):
        if i % 3 != 0 and i % 5 != 0:
            output += str(i) + " "
        if i % 3 == 0 and i % 5 == 0:
            output += "FizzBuzz"
        elif i % 3 == 0:
            output += "Fizz" + " "
        elif i % 5 == 0:
            output += "Buzz" + " "
    
    return print(output)

fizzbuzz(15)

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    
    #enter your code here

    word_length_dict = {}
    sentence = input("Input a sentence: ")
    for word in sentence.split():
        # word_length_dict.values()
        word_length_dict.update(word)

    return f"Output: {word_length_dict}"

print(word_lengths("sentence"))

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    
    #enter your code here

    nums = []
    
    for i in str(number):
        nums.append(int(i)**3)
    
    return sum(nums)

print(cube_sum(123))

