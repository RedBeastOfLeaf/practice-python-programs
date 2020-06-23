import itertools, random
n = int(input("How many cards to shuffle? : "))
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)
print("\nYou got: ")
for i in range(n):
    print(deck[i][0], "of", deck[i][1])
