from collections import Counter
print("")
first_string = input("Enter the main String: ".upper())
second_string = input("Enter the String to be checked: ".upper())
if(Counter(first_string) == Counter(second_string)):
    print("\nThis is an Anagram")
else:
    print("\nNot An Anagram")    
