from code import Automovel

f = Automovel('24-35-AC', 'fiat', 12000) # Adiciona o objecto Fiat
m = Automovel('21-54-BD', 'mercedez', 15300) # Adiciona o objeto mercedez


print(f.representação())
print(m.representação())

print(f.verificarsuperior(12500) and "maior" or "menor")
m.verificarsuperior(12500)
m.verificarsuperior(f.verCilindrada())

print(f.verMatricula())
print(m.verMatricula())

print(f.verMarca())
print(m.verMarca())

print(f.verCilindrada())
print(m.verCilindrada())

print(Automovel.numeros_de_objects)
