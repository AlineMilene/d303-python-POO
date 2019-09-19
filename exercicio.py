# Criar o exemplo da receita genérica, atributos e metodos que todas as receitas teriam
# A partir disso..

class Receita():
    def __init__ (self, ingredientes, preparo):
        self.ingredientes = ingredientes
        self.modo_de_preparo = preparo


    def get_all(self): 
        print("Os ingredientes da receita são: ")
        for i in self.ingredientes:
            print(i)
        print("\nO modo de preparo é: ")
        for j in self.modo_de_preparo:
            print(j)
                
        # print("Os ingredientes dessa receita são \n{}, \ne o modo de preparo é \n{}".format(
        # self.ingredientes,self.modo_de_preparo))

# ******* HERANÇA ********
class Doces(Receita):
    def __init__(self, nivel_acucar, ingredientes, preparo):
        self.nivel = nivel_acucar
        self.ingredientes = ingredientes
        self.modo_de_preparo = preparo
    
class Salgados(Receita):
    def __init__(self, nivel_sal, ingredientes, preparo):
        self.nivel = nivel_sal
        self.ingredientes = ingredientes
        self.modo_de_preparo = preparo
    
mousse = Doces('Nível de acúçar: 8/10',['1- Leite Condensado', '2- Creme de leite', '3 - 1pct de gelatina','4 - Água'], ['1- Prepare a gelatina conforme a embalagem', '2- Adicione tudo ao liquidificador', '3- Bata tudo por 2min'])
print(mousse.nivel)
mousse.get_all()
print()
print()
churrasco = Salgados('Nível de sal: 5/10',['1- Pão de Alho', '2- Carne', '3 - Linguiça','4 - Carvão'], ['1- Limpe as carne', '2- Ligue a churrasqueira ', '3- Coloque os ingredites restante e retire quando assados'])
print(churrasco.nivel)
churrasco.get_all()


# macarronada = Receita(["1 - Macarrão", "2 - Óleo", "3 - Água", "4 - Sal", "5 - Molho de Tomate"],["1º Ferva a água", "2º Adicione sal à gosto", "3º Adicione o óleo e o macarrão", "4º Tire depois de 8min e adicione o molho"])
# macarronada.get_all()



    # def get_ingredientes(self):
    #     return self.ingredientes
    
    # def get_preparo(self):
    #     return self.modo_de_preparo
    
    # def set_ingredientes(self, ingredientes_novo):
    #     self.ingredientes = ingredientes_novo
    #     return self.ingredientes

    # def set_modo_de_preparo(self, passos):
    #     self.modo_de_preparo = passos
    #     return self.modo_de_preparo

