from replit import clear
from art import logo
print(logo)
print("Welcome to the secret action!")
action = False
dictionary = {}
score = 0
x = 0
while not action:
    def my():
        dictionary.update({name: bid})
    name = input("What is your name? ")
    bid = input("What's your bid? $")
    my()
    question = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if question == "yes":
        clear()
        action == False
    if question == "no":
        clear()
        for key in dictionary:
            x = int(dictionary[key])
            if x > score:
                score = x
                name_winner = key
        print(f"The winner is {name_winner} with a bid of ${score}.")
        break