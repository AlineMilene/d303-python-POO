# Criar o exemplo da receita genérica, atributos e metodos que todas as receitas teriam
# A partir disso..

class Receita():
    def __init__ (self, nome, ingredientes, preparo):
        self.ingredientes = ingredientes
        self.modo_de_preparo = preparo
        self.nome = nome

    def get_all(self): 
        print("A receita é de {}". format(self.nome))
        print("Os ingredientes da receita são: ")
        for i in self.ingredientes:
            print(i)
        print("\nO modo de preparo é: ")
        for j in self.modo_de_preparo:
            print(j)
                
        # print("Os ingredientes dessa receita são \n{}, \ne o modo de preparo é \n{}".format(
        # self.ingredientes,self.modo_de_preparo))

macarronada = Receita("Macarronada",["1 - Macarrão", "2 - Óleo", "3 - Água", "4 - Sal", "5 - Molho de Tomate"],["1º Ferva a água", "2º Adicione sal à gosto", "3º Adicione o óleo e o macarrão", "4º Tire depois de 8min e adicione o molho"])
macarronada.get_all()



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

