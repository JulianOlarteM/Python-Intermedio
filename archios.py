def main():
    pass
def read():
    numers = []
    with open("./archivos/numbers.txt","r", encoding="utf-8") as f: #open(carpeta en la ue estamos, "r"= Solo lectura,  encoding = todo lo que leamos no tenga caractetes especiales como tildes y otro.   
        for line in f :
            numers.append(int(line))
    print(numers)

def write():
    names=["Facundo","Miguel", "Pepe","Cristian","Rocío"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f: #w = no guarda los cambios del scrpt con el .txt -- a= si guarda los cambios del scrpt en
        for name in names:
            f.write(name)
            f.write("\n") #salto de linea

def run():
    write()

if __name__=='__main__':
    run()
   