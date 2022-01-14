from functools import reduce

if __name__=='__main__':

    '''uso del filter '''
    my_list=[1,4,5,6,9,13,19,21]
    odd = list(filter(lambda x: x%2 != 0, my_list)) #generamos una funcion anonima lamda que recibe como parametro  a 'x' y retorna true o si el numero es impar. Luego la funcion filer recibe dos parametros, a la funcion lamba, y a una lista (variable iterable). La funcion filter retorna una iterador, colovando a la funcion list por encima de filter, obtenemos la lista.  
    print(odd)
    print('*'*50)
    
    '''uso del map'''
    my_list2=[1,2,3,4,5]
    squares = list(map(lambda x: x**2, my_list)) 
    print(squares)
    print('*'*50)

    ''' uso del reduce '''
    my_list3=[2,2,2,2,2]
    all_mulplied = reduce(lambda a ,b : a*b, my_list3)
    print(all_mulplied)
    print('*'*50)



