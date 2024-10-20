import random

def India_bat_first():
    print(" .....India is going to bat!")
    balls = 20
    India_runs = 0
    Pak_wicket = False
    
    while balls > 0 and not Pak_wicket:
        try:
            India_runs_input = int(input("Enter a number between 1 and 6: "))
            
            if India_runs_input < 1 or India_runs_input > 6:
                print("Invalid number. Please enter a valid number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer between 1 and 6.")
            continue
        
        pak_bowls = random.randint(1, 6)
        
        if India_runs_input != pak_bowls:
            India_runs += India_runs_input
            balls -= 1
            print(f"India scored: {India_runs}, Remaining balls: {balls}")
        else:
            print("Both picked the same number. It's a wicket.")
            Pak_wicket = True
    print(f"India scored {India_runs}")
    return India_runs

def Pak_bat_first():
    print("....Pakistan is going to bat!")
    balls = 20
    Pakistan_runs = 0
    India_wicket = False
    
    while balls > 0 and not India_wicket:
        try:
            Pakistan_runs_input = int(input("Enter a number between 1 and 6: "))
            if Pakistan_runs_input < 1 or Pakistan_runs_input > 6:
                print("Invalid number. Please enter a valid number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer between 1 and 6.")
            continue
        
        Ind_bowls = random.randint(1, 6)
        
        if Pakistan_runs_input != Ind_bowls:
            Pakistan_runs += Pakistan_runs_input
            balls -= 1
            print(f"Pakistan scored: {Pakistan_runs}, Remaining balls: {balls}")
        else:
            print("Both picked the same number. It's a wicket.")
            India_wicket = True
    print(f"Pakistan scored {Pakistan_runs}")
    return Pakistan_runs

def toss():

    toss = input("Choose odd or even: type 'e' or 'o': ").strip().lower()
    if toss not in ['e', 'o']:
        raise ValueError("Invalid choice. Please type 'e' for even or 'o' for odd.")
    
    pak_toss = random.randint(1, 10)
    print(f"Computer's number: {pak_toss}")

    while True:
        try:
            ind_toss = int(input("Enter a number between 1 and 10: "))
            if ind_toss < 1 or ind_toss > 10:
                print("Invalid number. Please enter a valid number between 1 and 10.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer between 1 and 10.")

    total = pak_toss + ind_toss

    temp = 'e' if total % 2 == 0 else 'o'
    print(f"Total is {'even' if temp == 'e' else 'odd'}.")

    if toss == temp:
        print("India won the toss!")
        I_choice = input("Enter 'a' if you want to bat first or 'b' to bowl first: ").strip().lower()
        
        if I_choice == 'a':
            India_score = India_bat_first()
            Pakistan_score = Pak_bat_first()
        else:
            Pakistan_score = Pak_bat_first()
            India_score = India_bat_first()
    else:
        print("Pakistan won the toss.")
        P_choice = random.choice(['a', 'b'])
        if P_choice == 'a':
            Pakistan_score = Pak_bat_first()
            India_score = India_bat_first()
        else:
            India_score = India_bat_first()
            Pakistan_score = Pak_bat_first()

    
    if India_score > Pakistan_score:
        print("Congratulations Team India! India wins!")
    elif Pakistan_score > India_score:
        print("Congratulations Team Pakistan! Pakistan wins!")
    else:
        print("It's a tie! Better luck next time!")
try:
    toss()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    toss()