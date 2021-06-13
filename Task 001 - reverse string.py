#V1 I Tried to make it on my own from zero with little to none Googling after glancing through functions/loops chapter in Python on how to write functions and loops in it
def reverse_string(normal_string):
    """Reverse a string, doesn't return anything"""
    index_reversed_string = 0
    index_normal_string = len(normal_string)-1
    reversed_string = ""
    while index_normal_string >= 0:
        new_character = normal_string[index_normal_string]
        reversed_string = reversed_string[:index_reversed_string] + new_character 
        index_reversed_string = index_reversed_string + 1
        index_normal_string = index_normal_string - 1
    print("Wyraz normalny to: " + normal_string)
    print("Wyraz odwrocony to: " + reversed_string)

#V2 I checked how to do better what I did above (https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/).
#Adds characters from one string, one by one, to the beginning of the new string, creating a reversed string
#with given value of "abc"(normal_string) to the function, code {reversed_string = current_character + reversed_string} becomes: "a" +""; "b" + "a"; "c" + "ba"; 
def reverse_string2(normal_string):
    """Reverse a string, doesn't return anything"""
    reversed_string = ""
    for current_character in normal_string:
        reversed_string = current_character + reversed_string
    print("Wyraz odwrocony to: " + reversed_string)

#V3 Googled how to do it the best. Great and easy explanation how it works here https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
#[start stop step]. [::] without given values means start at 0, stop at the string's length. -1 as a step means starting from the end 1 index at a time and stopping at the start
#Starts from character at string(length-1) putting it as first character in a new string. Then takes string(length-2) and puts it as a second character... continues till it reaches index of 0
#abc
#cba
def reverse_string3(string_to_reverse):
    """Reverse a string, doesn't return anything"""
    string_to_reverse = string_to_reverse[::-1]
    print("Wyraz odwrocony to: " + string_to_reverse)

   


