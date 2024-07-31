import pandas as pd  # utilizada para trabalhar com dataframes
import numpy as np   # biblioteca matematica
#from pandas_datareader import data # função para carregar dados online
import matplotlib.pyplot as plt #biblioteca padrao de visualizao no python
import seaborn as sns # graficos mais avançados para visualizaçao de graficos
import plotly.express as px # biblioteca com graficos dinamicos
import yfinance as yf 

acoes = ['GOLL4.SA', 'CVCB3.SA', 'WEGE3.SA', 'MGLU3.SA', 'TOTS3.SA', 'BOVA11.SA'] #formato de lista

acoes_df = pd.DataFrame() #buscar valores das empresas acima em um unico dataframe

for acao in acoes:  # para percorrer cada elemento da lista
    acoes_df[acao] = yf.download(acao,start='2015-01-01')['Close'] # vamos trabalhar somente com a coluna close

#print (acoes_df)

#renomear as colunas desse dataframe abaixo  para facilitar o processo

acoes_df = acoes_df.rename(columns={'GOLL4.SA': 'GOL', 'CVCB3.SA': 'CVC', 'WEGE3.SA': 'WEGE',
                                    'MGLU3.SA': 'MGLU', 'TOTS3.SA': 'TOTS', 'BOVA11.SA': 'BOVA'})
#print(acoes_df)

#acoes_df.head()

acoes_df.isnull().sum() # .isnull() indentificar somatorios nulos e .sum() para mostrar o somatorio deles

acoes_df.dropna(inplace=True) #comando .dropna(inplace=True) para apagar resultados nulos
#acoes_df.shape()


acoes_df.to_csv('acoes.csv')
acoes_df = pd.read_csv('acoes.csv')

sns.histplot(acoes_df['GOL']); 
len(acoes_df.columns) # vai retornar quantas totais nos temos
np.arange(1, len(acoes_df.columns))

plt.figure(figsize=(15,7))
i = 1
for i in np.arange(1, len(acoes_df.columns)): # vai gerar numeros para acessar a coluna 
  plt.subplot(7, 1, i + 1) # gerar um subgraficos
  sns.histplot(acoes_df[acoes_df.columns[i]], kde = True) #
  plt.title(acoes_df.columns[i]) # definir um titulo 


acoes_df.plot(x= 'Date', figsize=(15,7), title='historico do preço')


acoes_df_normalizado = acoes_df.copy() #manter o df normalizado e a copia 
for i in acoes_df_normalizado.columns[1:]:
  acoes_df_normalizado[i] = acoes_df_normalizado[i] / acoes_df_normalizado[i][0]

acoes_df_normalizado.plot(x= 'Date', figsize=(15,7), title='historico do preço - normalizado')
plt.show()

Figura= px.line (title='historico do preço de açoes ')
for i in acoes_df.columns[1:]:
   Figura.add_scatter(x= acoes_df['Date'],  y=acoes_df[i],name= i)

Figura.show()  

