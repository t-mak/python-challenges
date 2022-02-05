lifes = 11
word = list(input("Proszę podać słowo do odgadnięcia: "))
for x in range(35):
    print("\n")

guessed_word = []
for x in range(len(word)):
    guessed_word.append("_")

def draw_hangman(lifes):
    if lifes == 11:
            print("            ")
            print("            ")
            print("            ")
            print("            ")
            print("            ")
            print("            ")
            print("            ")
    elif lifes == 10:
            print("            ")
            print("            ")
            print("            ")
            print("            ")
            print("            ")
            print("            ")
            print("/            ")
    elif lifes == 9:
            print("            ")
            print("            ")
            print("            ")
            print("            ")
            print("            ")
            print("            ")
            print("/\\          ")
    elif lifes == 8:
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print("/\\          ")
    elif lifes == 7:
            print(" |---------  ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print("/\\          ")
    elif lifes == 6:
            print(" |---------  ")
            print(" |        |  ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print("/\\          ")
    elif lifes == 5:
            print(" |---------  ")
            print(" |        |  ")
            print(" |        O  ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print("/\\          ")
    elif lifes == 4:
            print(" |---------  ")
            print(" |        |  ")
            print(" |        O  ")
            print(" |        |  ")
            print(" |           ")
            print(" |           ")
            print("/\\          ")
    elif lifes == 3:
            print(" |---------  ")
            print(" |        |  ")
            print(" |        O  ")
            print(" |        |\\")
            print(" |           ")
            print(" |           ")
            print("/\\          ")
    elif lifes == 2:
            print(" |---------  ")
            print(" |        |  ")
            print(" |        O  ")
            print(" |       /|\\")
            print(" |           ")
            print(" |           ")
            print("/\\          ")
    elif lifes == 1:
            print(" |---------  ")
            print(" |        |  ")
            print(" |        O  ")
            print(" |       /|\\")
            print(" |         \\")
            print(" |           ")
            print("/\\          ")
    elif lifes == 0:
            print(" |---------  ")
            print(" |        |  ")
            print(" |        O  ")
            print(" |       /|\\")
            print(" |       / \\")
            print(" |           ")
            print("/\\          ")

while (lifes > 0):
    print(f"Odgadywane slowo: {guessed_word}")
    char_input = input("Podaj literę: ")
    if (word.count(char_input)): 
        print(f"\nLitera {char_input} jest w słowie!\n")
        i = 0
        for char_check in word:
            if char_check == char_input:
                guessed_word[i] = word[i]
            i = i + 1
        draw_hangman(lifes)
    else: 
        print("\nLitery nie ma w słowie!\n")
        lifes = lifes -1
        draw_hangman(lifes)
    print("\n-----------------------------------------------------\n")
    if guessed_word == word:
        break

print("***** KONIEC GRY *****")
if (lifes == 0):
    print("\nSłowo nieodgadnięte!")
    print(f"Słowo to {word}")
    draw_hangman(lifes)
if (lifes > 0):
    print("\nSłowo odgadnięte!")
    print(f"Słowo to {word}")
    draw_hangman(lifes)

"""
Zmienne:
słowo - do przechowania słowa. Pierwsza osoba je wymysla (input)
zycia - ile mozna bledow popelnic. Spada za kazdym razem jak sie poda literę,
ktorej nie ma
zycia spada do 0 - koniec gry, przegrane

Odgadywanie słowa:
//na poczatku same "_" np dla wybranego słowa Python "_ _ _ _ _ _"
Druga osoba wybiera litere, np "y"
Wyswietla sie, ze "Litera y znaleziona w słowie 1 raz"
Wysietla się "_ y _ _ _ _"
Druga osoba wybiera ponownie litere, np "a"
Wyswietla się "Nie znaleziono litery!"
Wyswietla się rysunek wisielca + 1 (na poczatek sama noga, potem druga itd).
"""
