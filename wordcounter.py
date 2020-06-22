# To count the words in a file
# The file should be in the same folder or directory
# enter the file name with extension

file_name = input("Enter file name with it's extension: ")
num_words = 0
with open(file_name, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)
