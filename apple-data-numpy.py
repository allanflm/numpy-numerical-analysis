import numpy as np

url = "https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv"

dado = np.loadtxt(url, delimiter=",", usecols=np.arange(1, 88, 1))
# -> print(dado)
# -> print(dado.ndim) = quantidade de dimensões
# -> print(dado.size) = quantiade de elementos de um array
# -> print(dado.shape)= numero de elementos em cada dimensão
 
dado_transposto = dado.T # iverte a estrutura: troca linhas por colunas
