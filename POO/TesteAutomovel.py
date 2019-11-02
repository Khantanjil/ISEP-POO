#Criar uma classe principal chamada TesteAutomovel que permita testar todas as funcionalidades da classe Automovel.

from Automovel import Automovel

class TesteAutomovel(Automovel):
    pass

a1 = Automovel('11-11-AA', 'Toyota', 14000)
print(a1.representação())
print(a1.Matrícula)
print(Automovel.numeros_de_objects)

a2 = Automovel('22-22-BB', 'Audi')
print(a2.representação())
a2.Cilindrada = 18000
print(a2.representação())
print(Automovel.numeros_de_objects)

print(abs(a1.diferenca(a2.Cilindrada)))



#l) Verificar se a cilindrada do automóvel a1 é superior a 2000 cc.
print(a1.verificarsuperior(2000))
print(a1.verificarmaior(a2.Cilindrada) and a1.Matrícula or a2.Matrícula)
