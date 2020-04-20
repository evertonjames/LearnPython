import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
filmes = pd.read_csv(uri) #dataframe
filmes.columns = ["filmeId","titulo", "generos"]
#filmes.head()
print(filmes.head())

uri2 = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
notas = pd.read_csv(uri2)
#print(notas.head())

#não aceitou alteracao de nome da coluna
#notas.column = ["usuarioId", "filmeId", "nota", "momento"]
print(notas.head())

#series
print("Listar apenas coluna rating dos 5 primeiros filmes")
print(notas["rating"].head())

print("Listar notas unicas (distinct)")
notasUnicas = notas["rating"].unique()
print(notasUnicas)

calculoMedia = notas["rating"].mean()
textoMedia = "Média total das notas = "
print(textoMedia, calculoMedia)

menorNota = notas["rating"].min()
textoMin = "Menor nota = "
print(textoMin, menorNota)

maiorNota = notas["rating"].max()
textoMax = "Maior nota = "
print(textoMax, maiorNota)

medianaNota = notas["rating"].median()
textoMediana = "Mediana Nota = "
print(textoMediana, medianaNota)

#Descrição de cada uma das variáveis
describe = notas.describe()
print(describe)
print("Nota média por filme:")
medias_por_filme = notas.groupby("movieId").mean().rating
print(medias_por_filme.head())

#Gerar histograma de notas
sns.set() #seta os quadriculados ao fundo do gráfico
plt.hist(notas['rating'])
plt.xlabel('Notas')
plt.ylabel("Quantidade")
plt.show()

#Gráfico boxplot comparando as notas dos 5 primeiros filmes
sns.boxplot(x = "movieId", y = "rating", data= notas.query("movieId in [1,2,3,4,5]"))
plt.show()