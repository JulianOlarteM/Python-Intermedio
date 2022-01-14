def main():

    my_list = [1, 'hello', True, 4.5]
    my_dict = {"fristname": "Facundo", "lastname" : "Garcia"}
    super_list = [
        {"fristname": "Facundo", "lastname" : "Garcia"},
        {"fristname": "Miguel", "lastname" : "torres"},
        {"fristname": "Pepe", "lastname" : "Rodelo"},
        {"fristname": "Susana", "lastname" : "Martinez"},
        {"fristname": "Jose", "lastname" : "Garcia"}
    ]
    
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "interger_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.63]
    }

    for key, values in super_dict.items():
        print(key, "-",values)


    for  vals in  super_list:
        for key2, values2 in vals.items():
            print(key2, values2)
  

if __name__ == '__main__':
    main()
