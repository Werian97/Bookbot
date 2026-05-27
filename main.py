import sys
from auxillary import word_counter
from auxillary import occurrancy_counter
from auxillary import occurrancy_counter_noconjunction
from auxillary import occurrancy_counter_onlyconjunction
from auxillary import occurrancy_counter_nolatex
from auxillary import sheet_counter


def get_book_text(file_path):
    with open(file_path, mode="r", encoding='utf-8-sig') as file:
        return file.read()

def main():
    word_sheet = []
    if len(sys.argv) == 1:
        print("You should give a file path to a text file as input")
        print("Correct syntax is: python3 main.py <file_path> [options]")
        sys.exit(1)
    elif len(sys.argv) > 4:
        print("Too many inputs")
        sys.exit(3)
    file = get_book_text(sys.argv[1])
    if len(sys.argv) == 2:
        words_number = word_counter(file)
    else:
        options = sys.argv[2:len(sys.argv)]
        if "whichwords" not in options:
            if "nolatex" in options:
                file = occurrancy_counter_nolatex(file)
                words_number = word_counter(file)
            word_sheet = occurrancy_counter(file)
            for option in options:
                if option == "noconjunction":
                    word_sheet = occurrancy_counter_noconjunction(word_sheet)
                    words_number = sheet_counter(word_sheet)
                elif option == "onlyconjunction":
                    word_sheet = occurrancy_counter_onlyconjunction(word_sheet)
                    words_number = sheet_counter(word_sheet)
                elif option == "nolatex":
                    continue
                else:
                    print(f"{option} is an invalid option")
                    sys.exit(2)
        else:
            words_number = word_counter(file)
            word_sheet = occurrancy_counter(file)
    print("===============WELCOME================")
    print("========This is BookVariantBot========")
    print(f"In this book there are {words_number} words")
    if len(sys.argv) > 2:
        print("In this book there are the following words, sorted by frequence of appearence")
        for word in word_sheet:
            print(f"{word["parola"]}: {word["num"]}")

main()

import sys
from auxillary import word_counter
from auxillary import occurrancy_counter
from auxillary import occurrancy_counter_noconjunction
from auxillary import occurrancy_counter_onlyconjunction
from auxillary import occurrancy_counter_nolatex
from auxillary import sheet_counter


def get_book_text(file_path):
    with open(file_path, mode="r", encoding='utf-8-sig') as file:
        return file.read()

def main():
    word_sheet = []
    if len(sys.argv) == 1:
        print("You should give a file path to a text file as input")
        print("Correct syntax is: python3 main.py <file_path> [options]")
        sys.exit(1)
    elif len(sys.argv) > 4:
        print("Too many inputs")
        sys.exit(3)
    file = get_book_text(sys.argv[1])
    if len(sys.argv) == 2:
        words_number = word_counter(file)
    else:
        options = sys.argv[2:len(sys.argv)]
        if "nolatex" in options:
            file = occurrancy_counter_nolatex(file)
            words_number = word_counter(file)
        word_sheet = occurrancy_counter(file)
        for option in options:
            if option == "noconjunction":
                word_sheet = occurrancy_counter_noconjunction(word_sheet)
                words_number = sheet_counter(word_sheet)
            elif option == "onlyconjunction":
                word_sheet = occurrancy_counter_onlyconjunction(word_sheet)
                words_number = sheet_counter(word_sheet)
            elif option == "nolatex":
                continue
            else:
                print("Invalid option")
                sys.exit(2)
    print("===============WELCOME================")
    print("========This is BookVariantBot========")
    print(f"In this book there are {words_number} words")
    if len(sys.argv) > 2:
        print("In this book there are the following words, sorted by frequence of appearence")
        for word in word_sheet:
            print(f"{word["parola"]}: {word["num"]}")

main()

