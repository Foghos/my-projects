cocktails = {
    "negroni": {
       "spirits": ["gin", "vermouth", "campari"],
       "ml": [25, 25, 25],
    },
    "aperol_spritz": {
        "spirits": ["aperol", "prosecco", "soda"],
        "ml": [50, 50, "top"]
    }
}
cocktail = "Negroni"
print(cocktail)
stop_quiz = True
while stop_quiz:
    guess = int(input(cocktails["negroni"]["spirits"][0] + ": "))
    if guess != cocktails["negroni"]["ml"][0]:
        continue
    else:
        guess = int(input(cocktails["negroni"]["spirits"][1] + ": "))
        if guess != cocktails["negroni"]["ml"][1]:
            continue
        else:
            guess = int(input(cocktails["negroni"]["spirits"][2] + ": "))
            if guess != cocktails["negroni"]["ml"][2]:
                continue
            else:
                print("You know how to make a " + cocktail + "!")
                answer = input("Do you want to play again? ")
                if answer == "yes":
                    continue
                elif answer == "no":
                    print("See you soon!")
                    stop_quiz = False
