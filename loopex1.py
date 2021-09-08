import random
colors=["white","orange","black","red","blue","yellow"]

while True:
    color=colors[random.randint(0,len(colors)-1)]
    guess=input("I'm thinking about a color, can you guess it? ")
    while True:
        if (color== guess.lower()):
            break
        else:
            guess = input("Nope. Try Again: ")
    print("You guessed it!")

    play_again=input("Let's play again? Type 'no' to quit:  ")
    if play_again.lower()=='no':
        break
    print("Thanks for playing")
