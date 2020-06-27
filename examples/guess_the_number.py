from random import randint

print("Hi! Welcome to Guess the Number Game!")
r_no = 0

play = True
while play:
    max_no = 500
    min_no = -500
    r_no = randint(-500, 500)
    g_no = -501
    c = 0
    while g_no != r_no:
        g_no = int(input(f"start guessing in the range: {min_no}  and {max_no}: "))
        if r_no > g_no > min_no:
            min_no = g_no
        elif r_no < g_no < max_no:
            max_no = g_no
        c = c + 1
    print(f"Voila! you guessed the number {g_no} in {c} trials!")
    condition = True
    res = ''
    while condition:
        allowedChars = ['Y', 'y', 'N', 'n']
        res = input("Want to play again? (y/n)")
        if len(res) == 1 and res in allowedChars:
            condition = False
    if res == 'N' or res == 'n':
        print("Have a Nice day! Goodbye!")
        play = False
