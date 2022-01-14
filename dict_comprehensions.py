from math import sqrt

def main():
    
    my_dict={}
    for i in range (1,101):
        my_dict[i] = i**3
    print (my_dict)
    print('*'*50)


    '''numero que no son divisibles en 3 '''
    
    my_dict2={}
    for i in range (1,101):
        if i%3 != 0:
            my_dict2[i] = i**3
    print (my_dict2)
    print('*'*50)


    ''' Esto se puede realizar en una sola linea, con los dict comprehensions'''
    my_dict3={i: i**3 for i in range (1, 101) if i%3 != 0}
    print(my_dict3)
    print('*'*50)

    '''crear un dic cullas llaves sean los numeros del 1 al 1000, y los valores la raiz cudadra de esas llaves'''
    my_dict4={i: sqrt(i) for i in range (1, 1001)}
    print(my_dict4)
    print('*'*50)


if __name__=='__main__':
    main()