def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():
    
    try:
        num = int(input('Ingresa un número: '))
        if num <= 0:
            raise ValueError('No se aceotan numero negativos ')
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError as ve:
        print('Debes ingresar un numero')
        print(ve)


if __name__ == '__main__':
    run()