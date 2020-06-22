# to check whether the provided word is palindrome or not

string_1 = input("Enter the word to be checked: ")
string_2 = string_1 [::-1]
if(string_1 == string_2):
    print("\nThe provided word is a palindrome!!!!!")
else:
    print("\nThe provided word is not a palindrome!!!")    
