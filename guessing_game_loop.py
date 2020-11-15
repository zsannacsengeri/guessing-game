import random

colors = ["yellow", "black", "white", "red"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("I'm thinking about color, could you guess it?")
    
    while True:
        
       if(color == guess.lower()):
          break
       else:
           guess = input("Nope, would you like to try it again? ")
           
    print("You gussed it. I was thinking about", color)

    play_again = input("Let's play again? Type 'no' to quit.")

    if play_again.lower() == 'no':
      break
print("It was fun, thank you for playing.")

    
