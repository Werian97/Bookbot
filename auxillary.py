from Variabili_globali import articoli, preposizioni_semplici, preposizioni_articolate, congiunzioni, other
import sys

def word_counter(text_file):
    words = text_file.split()
    words_number = len(words)
    return words_number

def sort_on(word_sheet):
    return word_sheet["num"]

def occurrancy_counter(text_file):
    dizio = {}
    text_file = text_file.lower()
    words = text_file.split()
    for word in words:
        if word in dizio.keys():
            dizio[word] += 1
        else:
            dizio[word] = 1
    word_sheet = []
    for elm in dizio:
        word_sheet.append({
            "parola": elm,
            "num": dizio[elm]
        })
    word_sheet.sort(reverse=False, key=sort_on)
    return word_sheet

def occurrancy_counter_noconjunction(word_sheet):
    indesiderati = articoli
    indesiderati.extend(preposizioni_semplici)
    indesiderati.extend(preposizioni_articolate)
    indesiderati.extend(congiunzioni)
    indesiderati.extend(other)
    for k in range(len(word_sheet)-1,-1,-1):
        if word_sheet[k]["parola"] in indesiderati:
            del word_sheet[k]
    return word_sheet

def occurrancy_counter_onlyconjunction(word_sheet):
    indesiderati = articoli
    indesiderati.extend(preposizioni_semplici)
    indesiderati.extend(preposizioni_articolate)
    indesiderati.extend(congiunzioni)
    indesiderati.extend(other)
    for k in range(len(word_sheet)-1,-1,-1):
        if word_sheet[k]["parola"] not in indesiderati:
            del word_sheet[k]
    return word_sheet

def occurrancy_counter_nolatex(text_file):
    text_file = text_file.lower()
    h = 0
    second_occurrance = False
    for k in range(len(text_file)-1,-1,-1):
        if text_file[k] == "$" and second_occurrance == False:
            h = k+1
            second_occurrance = True
        elif text_file[k] == "$" and second_occurrance == True:
            text_file = text_file[0:k] + text_file[h:len(text_file)]
            #cancello la parte indesiderata
            second_occurrance = False
    words = text_file.split()
    for k in range(len(words)-1,-1,-1):
        if words[k] == r"\]":
            h=k+1
        elif words[k] == r"\[":
            del words[k:h]
    for k in range(len(words)-1,-1,-1):
        if words[k] == r"\end{equation}":
            h=k+1
        elif words[k] == r"\begin{equation}":
            del words[k:h]
    for k in range(len(words)-1,-1,-1):
        if words[k] == r"\end{tikz}":
            h=k+1
        elif words[k] == r"\begin{tikz}":
            del words[k:h]
    for k in range(len(words)-1,-1,-1):
        if words[k] == r"\end{tikzpicture}":
            h=k+1
        elif words[k] == r"\begin{tikzpicture}":
            del words[k:h]
    for k in range(len(words)-1,-1,-1):
        if words[k] == r"\end{figure}":
            h=k+1
        elif words[k] == r"\begin{figure}":
            del words[k:h]
    for k in range(len(words)-1,-1,-1):
        if words[k] == r".\newline" or words[k] == r"," or words[k] == r".":
            del words[k]
    text_file = " ".join(words)
    return text_file

def sheet_counter (word_sheet):
    words_number = 0
    for item in word_sheet:
        words_number += item["num"]
    return words_number