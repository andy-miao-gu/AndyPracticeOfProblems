### Make a random matrix of 10x10
## Get diagonal eleemnts of matrix
## get upper diagonal
## get lower Diagonal MAtrix


import numpy as np

mat = np.random.randint(1,10,(5,5))
print(mat)


dd = np.diag((mat))
print(dd)

ww = np.triu((mat))
print(ww)
