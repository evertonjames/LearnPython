nome = "James"
print(nome)
idade = 30
print(idade)

def mais_um_ano(idade):
    print("Tá dentro da função")
    return print(idade + 1)
mais_um_ano(50)

print("###################")

filmes = ["Toy Story 4", "Matriz", "Crônicas de Nárnia"]
print(filmes)

def imprime_filmes(filmes_que_quero_imprimir):
    print("Lista de filmes que estão disponíveis")
    print(filmes_que_quero_imprimir)
imprime_filmes(filmes)

#imprime segundo filme da lista
print(filmes[1])
#Laço
for filme in filmes:
  print(filme)
  print("...")
print("Estou fora")

#Funcao para imprimir filmes
print("Inicio da Função Imprime_Filmes")
def imprime_filmes(filmes_que_quero_imprimir):
    print("Lista de filmes que estão disponíveis")
    for filme in filmes_que_quero_imprimir:
      print(filme)
imprime_filmes(filmes)

print("############### Conjunto de Dados ######################")
dados = {"nome" : "James",
         "idade" : "30",
         "empresa" : "iCarros",
         "genero" : "Masculino",
         }

print(dados["idade"])