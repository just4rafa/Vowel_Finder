
#Aplicatie de gasit vocale in cuvinte

nrVocale = 0
#Scrie cuvantul pe care il doresti
exe = input("Write the word/sentence you want: ")

for cuv in exe:
    if cuv == "a":
        print("I found the vowel", cuv)
        nrVocale += 1
    elif cuv == "e":
        print("I found the vowel", cuv)
        nrVocale += 1
    elif cuv == "i":
        print("I found the vowel", cuv)
        nrVocale += 1
    elif cuv == "o":
        print("I found the vowel", cuv)
        nrVocale += 1
    elif cuv == "u":
        print("I found the vowel", cuv)
        nrVocale += 1
    else:
        print("The word/sentence is not containing a vowel")

print("The total number of vowels is", nrVocale)
    
        
    
