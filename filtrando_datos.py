DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def main ():
    '''filtrando los que manejan el lenguaje python con list comprehesion '''
    all_python_devs=[worker["name"] for worker in DATA if worker["language"] == "python"]
    print(F'MANEJAN PYTHON LC: {all_python_devs}')
    

    '''filtrando los que manejan el lenguaje python con high funcions '''
    all_python_devs2 = list(filter(lambda worker: worker["language"] == "python",DATA))
    all_python_devs2 = list(map(lambda worker: worker["name"],all_python_devs2))
    print(F'MANEJAN PYTHON HF: {all_python_devs2}')
    print('*'*50)

    '''filtrando los que trabajan en Platzi  con listo  comprehesion '''
    all_Platzi_Worked=[worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    print(f'Trabajan en Platzi: {all_Platzi_Worked}')
    

    '''filtrando los que trabajan en Platzi  con high funtions '''
    all_Platzi_Worked2=list(filter(lambda worker: worker["organization"] == "Platzi" , DATA))
    all_Platzi_Worked2=list(map(lambda worker: worker["name"], all_Platzi_Worked2))
    print(f'Trabajan en Platzi: {all_Platzi_Worked2}')
    print('*'*50)


    '''filtrando a los adultos con high funcions '''
    adults = list(filter(lambda worker: worker["age"] > 18 ,DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    print(f'los adultos son HF: {adults}')

    

    '''filtrando a los adultos con dict comprenhension '''
    adults2=[worker["name"] for worker in DATA if worker["age"] > 18 ]
    print(f'los adultos son DC: {adults2}')
    print('*'*50)

    '''filtrando a la gente vieja con high funcions '''
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70 },DATA))
    print(F' gente viej HF: {old_people}')
    print('-'*50)


    '''filtrando a la gente vieja con dict comprenhensions '''
    old_people2 = [worker | {"old":  worker["age"] >70}  for worker in DATA]
    print(F' gente viej HF: {old_people2}')
    print('*'*50)

    
    
     
if __name__=='__main__':
    main()