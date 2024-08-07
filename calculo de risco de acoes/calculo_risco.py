import pandas as pd
import numpy as np
import math 
import matplotlib.pyplot as plt 
import seaborn as sns 
from scipy import stats 

dataset = pd.read_csv('acoes.csv') 

dataset.describe() 

# taxa de retorno 2015
rt0 = dataset['CVC'][dataset['Date'] == '2015-01-02'],dataset['CVC'][dataset['Date'] == '2015-12-30'] #Filtro
np.log(11.12/12.52) *100 # Taxa de retorno 

dataset['MGLU'][dataset['Date'] == '2015-01-02'],dataset['MGLU'][dataset['Date'] == '2015-12-30']
np.log(0.64/2.17) *100 

# calculo de retorno 2016
dataset['CVC'][dataset['Date'] == '2016-01-04'],dataset['CVC'][dataset['Date'] == '2015-12-30'] #Filtro
np.log(23.70 / 12.53) * 100 # Taxa de retorno 

a0 = dataset['MGLU'][dataset['Date'] == '2016-01-02'],dataset['MGLU'][dataset['Date'] == '2015-12-30']
np.log(0.41 / 0.07) * 100

# calculo de retorno  2017

dataset['CVC'][dataset['Date'] == '2017-01-02'], dataset['CVC'][dataset['Date'] == '2017-12-29']
np.log(48.50 / 23.02) * 100

a1 = dataset['MGLU'][dataset['Date'] == '2017-01-04'], dataset['MGLU'][dataset['Date'] == '2017-12-29']
np.log(2.50 / 0.39) * 100

# calculo de retorno 2018 

dataset['CVC'][dataset['Date'] == '2018-01-02'], dataset['CVC'][dataset['Date'] == '2018-12-28']
np.log(61.18 / 49.88) * 100

a2=dataset['MGLU'][dataset['Date'] == '2018-01-02'], dataset['MGLU'][dataset['Date'] == '2018-12-28']
np.log(5.65 / 2.47) * 100

# calculo de retorno 2019
dataset['CVC'][dataset['Date'] == '2019-01-02'], dataset['CVC'][dataset['Date'] == '2019-12-30']
np.log(43.79 / 61.09) * 100

a3=dataset['MGLU'][dataset['Date'] == '2019-01-02'], dataset['MGLU'][dataset['Date'] == '2019-12-30']
np.log(11.92 / 5.81) * 100

# calculo de retorno 2020

dataset['CVC'][dataset['Date'] == '2020-01-02'], dataset['CVC'][dataset['Date'] == '2020-11-03']
np.log(12.42 / 44.70) * 100

a4= dataset['MGLU'][dataset['Date'] == '2020-01-02'], dataset['MGLU'][dataset['Date'] == '2020-11-03']
np.log(25.30 / 12.33) * 100

# taxa de retorno 

taxas_cvc = np.array([11.12,10.32,11.12, 18.97, 41.11,50.42])

media_cvc= taxas_cvc.sum() / len(taxas_cvc)

variancia_cvc = taxas_cvc.var()

taxas_mglu = np.array(3.50,23.17, 52.92, 54.36,  111.53,115.3,233.73)

print(a0,a1,a2,a3,a4)