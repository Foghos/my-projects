cocktail = "Negroni"
gin = str(25)
vermouth = str(25)
campari = str(25)
print('Specs for ' + cocktail + ":")
while True:
    guess = str(input("Gin: "))
    if guess != gin:
        print("Try again.")
        continue
    else:
        guess2 = str(input("Vermouth: "))
        if guess2 != vermouth:
            print("Try again")
            continue
        else:
            guess3 = str(input("Campari: "))
            if guess3 == campari:
                print("Congratulations, you know how to make a " + cocktail + "!")
                break
            else:
                print("You were almost there.")
                continue



