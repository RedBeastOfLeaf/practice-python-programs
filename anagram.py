from collections import Counter
print("")
first_string = input("Enter the main String: ")
second_string = input("Enter the String to be checked: ")
string_1 = first_string.upper()
string_2 = second_string.upper()
if(Counter(string_1) == Counter(string_2)):
    print("\nThis is an Anagram")
else:
    print("\nNot An Anagram")    
