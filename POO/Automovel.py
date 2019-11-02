# Elaborar uma classe chamada Automovel

class Automovel:
    # Saber os numeros de objetos criados
    numeros_de_objects = 0
    #Constructor com atributos: Matricula | Marca | Cilindrada
    
    
    def __init__(self, Matrícula = "sem", Marca="sem", Cilindrada=0):
        self.Matrícula = Matrícula
        self.Marca = Marca
        self.Cilindrada = Cilindrada
        Automovel.numeros_de_objects += 1
    #Consultar individualmente os atributos de um automóvel
    def verMatricula(self):
        return self.Matrícula

    def verMarca(self):
        return self.Marca

    def verCilindrada(self):
        return self.Cilindrada

    # Verificar se a cilindrada de um automóvel é superior a um determinado valor
    def verificarsuperior(self, value):
        return self.Cilindrada > value

    #Verificar se a cilindrada de um automóvel é superior à de outro
    

    #Determinar a diferença de cilindrada entre dois automóveis
    def diferenca(self, value):
        return self.Cilindrada - value
        

    #Obter a representação textual e legível de um automóvel
    def representação(self):
        return f'Automóvel com matricula de {self.Matrícula} é um {self.Marca} e tem {self.Cilindrada}'

    def verificarmaior(self, value):
        return self.Cilindrada > value

    


