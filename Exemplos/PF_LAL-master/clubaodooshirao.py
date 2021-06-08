class automovel():
    def __init__(self):
        self.portas = int(input('portas'))
        #self.rodas = int(input('rodas'))
        self.motor = float(input('motor'))
        #self.marca = input('marca')
    def abrir_porta(self):
        ação = input("quer abrir uma porta?")
        if ação == "sim":
            qnt = int(input("qnts portas?"))
            self.portas_abertas = qnt
            self.portas_fechadas = self.portas-self.portas_abertas
            print(f'portas abertas: {self.portas_abertas}, portas fechadas: {self.portas_fechadas}')
        else:
            print("vtncc")
    def racha(self,auto1,auto2):
        if auto1.motor > auto2.motor:
            print("carro 1 ganhou")
        else:
            print("carro 2 ganhou")

gol = automovel()
celta = automovel()
gol.abrir_porta()





