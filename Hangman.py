import random
words = ["apple", "banana", "computer", "dog", "elephant",
    "flower", "grape", "house", "ice", "jacket",
    "kite", "lemon", "mountain", "notebook", "orange",
    "pencil", "quilt", "river", "sun", "tree",
    "umbrella", "violin", "water", "xylophone", "yacht",
    "zebra", "airplane", "book", "car", "dance",
    "envelope", "furniture", "giraffe", "hat", "island",
    "jungle", "key", "lamp", "moon", "night",
    "ocean", "penguin", "question", "rocket", "star",
    "tiger", "unicorn", "vase", "window", "xylophone"]

w=[]
p=[]
c=[]
lives=5

x=random.choice(words)
for i in x:
    w.append(i.lower())
for i in w:
    p.append("_")
print("Welcome to Hangman!")

while lives>0:
    chk=0
    for i in p:
        print(i, end=' ')
    print("\n\n")

    print("Number of Lives remaining:",lives)
    z=input("Enter the letter you'd like to check for in the word:").lower()
    print('\n\n')
    if len(z)>1 and z.isalpha()==False:
        print("Give me just a single letter of the alphabet")
    elif z in c:
        print("That letter has been chosen already.")

    else:
        chk=1
        c.append(z)
    
    if chk==1:
        if z in w:
            print("Yes! That letter is present in the word.")
            for i in range(len(w)):
                if w[i]==z:
                    del p[i]
                    p.insert(i,z)
                    

        else:
            print("Whoops! The letter is not present in the word. You just lost a life!")
            lives-=1

    if w==p:
        print("CONGRATULATIONS! YOU WIN!The word was, indeed,",x)
        print("You had",lives,"lives remaining.")
        break

else:
    print("Oh no! You just lost the Hangman game. You've lost all your lives.")
    print("The word was",x)

#Made by Piyush Varman, Github- @PiyushVarman
