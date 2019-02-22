
number_to_guess = 55

user_number = int(input("Adivina el numero: "))

if user_number == number_to_guess:
    print("Has ganado")
else:
    user_number  = int(input("Vuelve a intentarlo: "))
    if user_number == number_to_guess:
        print("Has ganado")
    else:
        user_number  = int(input("Vuelve a intentarlo: "))
        if user_number == number_to_guess:
            print("Has ganado")
        else:
            user_number  = int(input("Vuelve a intentarlo: "))
            if user_number == number_to_guess:
                print("Has ganado")
            else:
                user_number  = int(input("Vuelve a intentarlo: "))
                if user_number == number_to_guess:
                    print("Has ganado")
                else:
                    print("Has gastado tus 5 intentos")
