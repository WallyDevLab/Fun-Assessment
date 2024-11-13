def dog_years(age):
    
    """Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """
    x = 10.5
    y = 4
    age = age-2
    new_age = age*y
    first_two = 2*x
    last_age = new_age + first_two
    print(f"The dog's age in dog's years is {int(last_age)}") 

dog_years(15)

    #enter your code here

def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """
    num_list = []
    new_list = []
    
    for nums in range(1,num+1):
        #print(nums)
        num_list.append(nums)
        for num in num_list:
            if num % 3 == 0 and num % 5 == 0:
                num = "FizzBuzz"       
            elif num % 3 == 0:
                num = "Fizz"       
            elif num % 5 == 0:
                num = "Buzz"
            else:
                num == num 
        
        new_list.append(num)
        my_string = str(new_list)
        

    
        
    
    print(my_string)
        

    #enter your code here
fizzbuzz(15)
    

def word_lengths(sentence):

    """Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```

    """
    words = sentence.split(' ')
    my_dict = {for word in words : }
    
        
        
#word_lengths("Aunty Yankho is amazing")
    
    #enter your code here

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """

    if number // 10 != 0:
        x = number%10       #remainder%
        y = number//10           #\\remove remainder
        x = y % 10

        
    
    
    
cube_sum(123)