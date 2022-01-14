def main ():
    '''el cuadrado de los  numeros del 1 al 100 '''
    squares = []
    for i in range (1,101):
        squares.append(i**2)
    print(squares)
    print('*'*50)

    '''del cuadrado de los numeros del 1 al 100, guadre los ue no son divicibles entre 3'''
    squares2=[]
    for i in range (1,101):
        if i % 3 != 0:
            squares2.append(i**2)
    print(squares2)
    print('*'*50)


    ''' Esto se puede resolver en una sola linea con el concepto de List Comperhensions'''
    squares3=[i**2 for i in range (1,101) if i%3 != 0]
    print(squares3)
    print('*'*50)

    '''crea u list comprehension de todos los multiplos de 4 , 6 , y 9. de los numero que van de 0 a 99.999'''
    squares4 = [i for i in range (1,10000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(squares4)
    print('*'*50)

if __name__=='__main__':
    main()