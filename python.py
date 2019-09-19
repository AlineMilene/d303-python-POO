# ESTRUTURA DA CLASSE
# class CuboMagico(self)
# self é utilizado para se referir ao objeto que foi criado a partir dessa classe

# *********** EXEMPLO 1 - CUBO MAGICO ************

# class CuboMagico():
    
#     def __init__(self, cores, lados):
#         self.colors = cores
#         self.sides = lados
    
#     def get_cores(self):
#         return self.colors

#     def print_cores_por_linha(self):
#         for i in self.colors:
#             print(i)

#     def get_lados(self):
#         return self.sides
    
#     def set_cores(self, pigmentos):
#         self.colors = pigmentos
#         return self.colors
    
#     def set_lados(self, lados):
#         self.sides = lados
#         return self.sides

# lista_de_cores = ['vermelho', 'azul', 'amarelo', 'verde', 'branco', 'laranja']
# porco = CuboMagico(lista_de_cores, 6)

# cores_do_porco = porco.get_cores()
# print(cores_do_porco)
# print()

# porco.set_cores(['marrom','roxo','cinza','bege','preto','rosa'])
# print(porco.get_cores()) 


# *********** EXEMPLO 2 - ANIMAL ************
class Animal():
    vida = True

    def __init__(self, pelo, especie, olhos, patas):
        self.pelo = pelo
        self.especie = especie
        self.olhos = olhos
        self.patas = patas
    
    def get_all(self):
        print("Esse animal é um {}, tem {} olhos e tem {} patas.". format(
            self.especie, self.olhos, self.patas
        ))
    
class Cachorro(Animal):
    def __init__ (self, raca, olhos, patas, nome):
        self.raca = raca
        self.olhos = olhos
        self.patas = patas
        self.nome = nome
    
    def get_vida(self):
        print(self.vida)

cleiton = Cachorro("Vira - Lata", 1, 3, "Cleiton")
# cleiton.get_all()
cleiton.get_vida()

porco = Animal(True, "Suíno", 2, 4)
porco.get_all()
