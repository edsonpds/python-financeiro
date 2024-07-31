import pandas as pd
import numpy as np 
import plotly.express as px 
import matplotlib.pyplot as plt

#taxa de retorno simples 

dataset= pd.read_csv('acoes.csv') 
#dataset.shape()

len(dataset)
dataset['GOL'][0],dataset['GOL'][len(dataset)-1] # busca do primeiro e ultimo registro

#calculo de taxa de retorno simples

((dataset['GOL'][len(dataset) - 1] - dataset['GOL'][0]) / dataset['GOL'][0]) * 100 
((dataset['CVC'][len(dataset) - 1] - dataset['CVC'][0]) / dataset['CVC'][0]) * 100
((dataset['WEGE'][len(dataset) - 1] - dataset['WEGE'][0]) / dataset['WEGE'][0]) * 100
((dataset['MGLU'][len(dataset) - 1] - dataset['MGLU'][0]) / dataset['MGLU'][0]) * 100   
((dataset['MGLU'][len(dataset) - 1] - dataset['MGLU'][0]) / dataset['MGLU'][0]) * 100
((dataset['BOVA'][len(dataset) - 1] - dataset['BOVA'][0]) / dataset['BOVA'][0]) * 100

(dataset['BOVA'][len(dataset) - 1] / dataset['BOVA'][0] - 1) * 100 # outra formula pouco mais simples 

#taxa de retorno diaria e anual 

#dataset['GOL']

dataset['GOL'].shift(1) # zera o primeiro valor e o valor pula pro segundo 
dataset['RS GOL'] = (dataset['GOL']/ dataset['GOL'].shift(1)) - 1 


dataset['RS GOL'].mean() 
dataset.head(246)
(dataset['RS GOL'].mean() * 246) *100

dataset['RS CVC'] = (dataset['CVC']/ dataset['CVC'].shift(1)) - 1
dataset['RS WEGE'] = (dataset['WEGE']/ dataset['WEGE'].shift(1)) - 1
dataset['RS MGLU'] = (dataset['MGLU']/ dataset['MGLU'].shift(1)) - 1
dataset['RS TOTS'] = (dataset['TOTS']/ dataset['TOTS'].shift(1)) - 1
dataset['RS BOVA'] = (dataset['BOVA']/ dataset['BOVA'].shift(1)) - 1



dataset['RS GOL'].mean() 
dataset.head(246)
(dataset['RS GOL'].mean() * 246) *100
(dataset['RS WEGE'].mean() * 246) *100
(dataset['RS TOTS'].mean() * 246) *100
(dataset['RS MGLU'].mean() * 246) *100
(dataset['RS CVC'].mean() * 246) *100 
(dataset['RS BOVA'].mean() * 246) *100 

# Taxa de retorno logarítmica

dataset['GOL'][0],dataset['GOL'][len(dataset)-1]
np.log(dataset['GOL'][len(dataset)-1] / dataset['GOL'][0]) *100
np.log(dataset['CVC'][len(dataset)-1] / dataset['CVC'][0]) *100
np.log(dataset['WEGE'][len(dataset)-1] / dataset['WEGE'][0]) *100
np.log(dataset['MGLU'][len(dataset)-1] / dataset['MGLU'][0]) *100
np.log(dataset['TOTS'][len(dataset)-1] / dataset['TOTS'][0]) *100
np.log(dataset['BOVA'][len(dataset)-1] / dataset['BOVA'][0]) *100

dataset['RL GOL'] = np.log(dataset['GOL'] / dataset['GOL'].shift(1))
dataset['RL GOL'].plot();
dataset['RL GOL'].mean()
(dataset['RL GOL'].mean() * 246) * 100
dataset['RL CVC'] = np.log(dataset['CVC'] / dataset['CVC'].shift(1))
dataset['RL WEGE'] = np.log(dataset['WEGE'] / dataset['WEGE'].shift(1))
dataset['RL MGLU'] = np.log(dataset['MGLU'] / dataset['MGLU'].shift(1))
dataset['RL TOTS'] = np.log(dataset['TOTS'] / dataset['TOTS'].shift(1))
dataset['RL BOVA'] = np.log(dataset['BOVA'] / dataset['BOVA'].shift(1))

(dataset['RL CVC'].mean() * 246) * 100
(dataset['RL WEGE'].mean() * 246) * 100
(dataset['RL MGLU'].mean() * 246) * 100
(dataset['RL TOTS'].mean() * 246) * 100
(dataset['RL BOVA'].mean() * 246) * 100

# retorno de carteira de açoes 
dataset = pd.read_csv('acoes.csv') 
dataset_normalizado = dataset.copy()
for i in dataset_normalizado.columns[1:]:
    dataset_normalizado[i] = (dataset_normalizado[i] / dataset_normalizado[i][0])
    
dataset_normalizado.plot(x = 'Date', figsize=(15,7))
#plt.show()

dataset_normalizado.drop(labels=['Date'], axis=1,inplace=True)

retorno_carteira = (dataset_normalizado / dataset_normalizado.shift(1)) -1 
retorno_carteira.head()

retorno_anual = retorno_carteira.mean() * 246
retorno_anual = retorno_anual * 100 #retorna em porcentagem 

pesos_carteira1 = np.array([0.2,0.2,0.2,0.2,0.2,0.0])
np.dot(retorno_anual,pesos_carteira1)

pesos_carteira2 = np.array([0.1,0.2,0.4,0.1,0.0])
#np.dot(retorno_anual,pesos_carteira2)



dataset_normalizado['CARTEIRA'] = (dataset_normalizado['GOL'] + dataset_normalizado['CVC'] + dataset_normalizado['WEGE'] + dataset_normalizado['MGLU'] + dataset_normalizado['TOTS']) /5

figura = px.line(title = 'Comparativo carteira x BOVA')
for i in dataset_normalizado.columns[1:]:
    figura.add_scatter(x = dataset_normalizado['Date'],y = dataset_normalizado[i], name= i) 

px.show()
