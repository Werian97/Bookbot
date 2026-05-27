#BookVariantBot

# Bookbot
This program takes as input a text file and count how many words are in the file. Then count the occurrancies of the words and sort the list by increasing order. Prints the result in the stdout. It is a variant of the project on [Boot.dev](https://www.boot.dev). This variant is a simple attempt to count the words that really matter in a latex file

SYNTAX
python3 main.py <file_path> [options]

BASIC USAGE
python3 main.py <file_path>
If no option is selected the program counts the number of words in the file and print on stdout the number

OPTIONS
whichwords - ignore all other options and print the list of words sorted by increasing order

nolatex - count the words excluding all the parts between \[ and \], or $ and $, or \begin{something} and \end{something}. The choice of what "something" was worth to exclude is based completely on my master thesys, which is totally arbitrary.

noconjunction - count the words excluding all the articles, prepositions and conjunctions

onlyconjunctions - count only the part excluded with the "noconjunction" option

All those options can be combined (no more than 2. It would be nonsensical)
