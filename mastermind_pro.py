import random

COLORS = ["G","B","R","O","Y"]
CODE_LENGHT = 4
TRIES = 5

def generate_code_color():
    code = []
    for _ in range(CODE_LENGHT):
        code.append(random.choice(COLORS))
    return code


def guessing():
    while True:
        guess = input("Guess: ").upper().split(" ")
    
        if len(guess) != CODE_LENGHT:
            print(f"too short.guess {CODE_LENGHT} colors.")
            continue
        for color in guess:
            if color not in COLORS:
                print(f"invalid color.{color} change it")
                break
        else:
            break
    return guess


def check_code(guess,real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] +=1
    
    for guess_color , real_color in zip(guess,real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess,real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1 

    return correct_pos, incorrect_pos


def game():
    print(f"welcome to the game you have {TRIES} tries to win this game.")
    print("valid colors are", *COLORS)
    print("**IMPORTANT: put a space between your guesses!GOOD LUCK.")
    code = generate_code_color()
    for try_ in range(1, TRIES + 1):
        guess = guessing()
        cor_pos, inc_pos = check_code(guess,code)

        if cor_pos == CODE_LENGHT:
            print(f"you guess the code in {try_} tries.")
            break
        print(f"correct_possitions: {cor_pos} | incorrect_possitions: {inc_pos}")
    else:
        print("you don't have any tries.the real code was", *code)

if __name__ == "__main__":
    game()