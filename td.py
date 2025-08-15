import pandas as pd 
import seaborn as srn 
import statistics as sts

dataset = pd.read_csv("tempo.csv", sep=";")
#explora o df categorico
agrup = dataset.groupby(['Vento']).size()

#mosta quais colunas tem valores nulos
print(dataset.isnull().sum())

#UMIDADE----------
#preenche os campos nulos com a media e mediana
medianav = sts.median(dataset['Umidade'])
# Preenche os valores nulos da coluna 'Umidade' com a mediana
dataset['Umidade'].fillna(medianav, inplace=True)
#preenche os valores maiores que 200 da coluna de umidade com a mediana
dataset.loc[dataset['Umidade'] > 100, 'Umidade'] = medianav

#TEMPERATURA---------
#mediana de temperatura
medianat = sts.median(dataset['Temperatura'])
#preenche o valor maior que 100 com a mediana
dataset.loc[dataset['Temperatura'] > 100, 'Temperatura'] = medianat

#VENTO----------
# Preenche os valores nulos da coluna 'Vento' com a moda
dataset['Vento'].fillna("FALSO", inplace=True)

#APARENCIA---------
#atribuindo  a moda de aparencia em case fora de categoria
agrupo = dataset.groupby(['Aparencia']).size()
print(agrupo)
#categorico, escolho os que ta fora de ordem e atribuo a moda da coluna aparencia
dataset.loc[dataset['Aparencia'].isin(['menos']), 'Aparencia'] = "chuva"

#JOGAR--------
#Preenche os valores de jogar de acordo com a aparencia
dataset.loc[dataset['Aparencia'] == "chuva", 'jogar'] = "nao"
dataset.loc[dataset['Aparencia'] == "sol", 'jogar'] = "sim"
dataset.loc[dataset['Aparencia'] == "nublado", 'jogar'] = "sim"

#DATASET------- (FINALMENTE)
print(dataset)
# Salva o DataFrame limpo em um novo arquivo CSV
dataset.to_csv("tempo_limpo2.csv", index=False)