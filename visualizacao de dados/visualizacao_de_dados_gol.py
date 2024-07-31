import pandas as pd  # utilizada para trabalhar com dataframes
import numpy as np   # biblioteca matematica
#from pandas_datareader import data # função para carregar dados online
import matplotlib.pyplot as plt #biblioteca padrao de visualizao no python
import seaborn as sns # graficos mais avançados para visualizaçao de graficos
import plotly.express as px # biblioteca com graficos dinamicos
import yfinance as yf 


gol_df = yf.download("GOLL4.SA", start='2015-01-01')
print(gol_df) 

print(30*"---")

info = gol_df.info() # .info() obter informaçoes da base de dados acima 
print(info)

print(30*"---")

topo = gol_df.head(2) # .head() observar os primeiros registros
print(topo) 

print(30*"---")

ultimos = gol_df.tail(3) # .tail() observar os ultimos numeros 
print(ultimos) 

print(30*"---")

descricao= gol_df.describe() # .describe() observar algumas estasticas 
print(descricao)

print(30*"---")

filtro = gol_df[gol_df['Close']>= 43.79] # filtra o atributo com base na açao indicada
print (filtro)

filtro_1 = gol_df[(gol_df['Close'] >= 1.15) & (gol_df['Close'] <= 1.16)]
print(filtro_1) 

print(30*"---") 

gol_df.to_csv('gol.csv') # salvar informaçoes em arquivo . csv 

gol_df2 = pd.read_csv('D:\Python para finanças\gol.csv')
print(gol_df2)


