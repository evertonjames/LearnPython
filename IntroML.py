#pelo longo?
#perna curta?
#faz auau?

porco1 = [0,1,0]
porco2 = [0,1,1]
porco3 = [1,1,0]

cachorro1 = [0,1,1]
cachorro2 = [1,0,1]
cachorro3 = [1,1,1]

#Nada a ver com 0 ou 1 de cima
treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1,1,1,0,0,0] #0 cachorro 1 porco

from sklearn.svm import LinearSVC

modelo = LinearSVC()
print(modelo.fit(treino_x, treino_y))

animal_misterioso = [1,1,1]
print("Animal misterioso é(0 = cachorro e 1 = porco): ")
print(modelo.predict([animal_misterioso]))

#Inserir 3 animais misteriosos
misterio1 = [1,1,1]
misterio2 = [1,1,0]
misterio3 = [0,1,1]

teste_x = [misterio1, misterio2, misterio3]
teste_y = [0,1,1]

previsoes = modelo.predict(teste_x)
print("Animais misteriosos são(0 = cachorro e 1 = porco): ")
print(previsoes)

#Medir acurácia
from sklearn.metrics import accuracy_score
print("A acurácia do modelo é de: ")
print(accuracy_score(teste_y, previsoes))