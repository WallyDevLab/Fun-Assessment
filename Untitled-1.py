
"""#exercise : User input 
#distance coverter to km to meters

#take two inputs from users
name = input('enter your name: ')
distance_km = input('enter distance in kilometers: ')

mile = float(distance_km)/1.609

    
#print 
print(f'Hello {name.capitalize()}! {distance_km} kilometers distance to miles is {round(mile, 1)} miles')"""
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
    sentence = 'I love you'
    dict_string = dict(sentence)
    print(dict_string)