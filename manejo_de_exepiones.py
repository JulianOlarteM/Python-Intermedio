def palindromo(string):
    try:
        if len(string) == 0:
            raise ValueError("no se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


if __name__=='__main__':

    palindromo(1)

    '''Primer ejemplo del uso del try y el except
    try:
        print(palindromo(1))
    except TypeError:
        print("Solo se pueden ingresar Strings")

'''