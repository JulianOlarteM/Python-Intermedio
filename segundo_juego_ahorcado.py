import random 

def read_words():
    data=[]
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(str(line))
    return data

def choose_word ():
    data=read_words()
    word = random.choice(data)
    size_word= len(word)

    list_word=[]
    list_word_empty=[]
    for letter in word:
        list_word.append(letter)
        list_word_empty.append("_")
    
    list_word.pop(size_word-1)   
    list_word_empty.pop(size_word-1)
     
    return(list_word , list_word_empty)

def type_letter_in():
    good_letter = False
    
    while good_letter == False:
        letter=str(input('Ingresa una letra minuscula: '))
        if letter.isalpha()   and len(letter)==1 and letter.isupper() == False: 
            good_letter = True  
        else: 
            print('¡ Ingresa una sola letra en minuscula, o no repitas letras !')
            good_letter = False  
         
    return letter

def linear_search (list, objetive):
    match = False
    for i in list:
        if i == objetive:
            match= True
    return match  

def play():
    
    word =  choose_word()
    list_word = word[0]
    list_word_empyty = word[1]
    success = 0              
    faults = 0

    print(f'palabra de juego: {list_word}       lista que se va llenando:  {list_word_empyty}')

    hanged_man = False
    while hanged_man == False:
        
        letter= type_letter_in() 
        data=  [] 
        for indice, caracter in enumerate(list_word):
            if  letter == caracter:
                list_word_empyty[indice] = letter
                hanged_man = False
            else:
                faults += 1
                hanged_man = False
     
 
        print(data)
        print(list_word,list_word_empyty)
        print(f'aciertos: {success} desaciertos:{faults}')           
      
if __name__=='__main__':
   play()