import sys
import random as random
import numpy as np
# import matplotlib.pyplot as plt

#*-------------------Initial parameters-----------
"""
p=  int(input('Enter the number of facilities to be opened: '))
m=  int(input('Enter the number of facilities available: '))
n=  int(input('Enter the number of users to be considered: '))
dmin=int(input('Smallest distance possible for x/y: '))
dmax=int(input('Greatest distance possible for x/y: '))

"""
cant = 20  #! NO MOVER
n=30000
m=600
p=30
rango = 10000 #! NO MOVER
cont_name = 1
#seed = 1 #ba10(hex) en decimal = 47632//23674 // 3ed10(medio) = 257296//692752 // a110(alto) = 41232
#47632 - 692752 - 41232
#print(seed)


for j in range(cant):
    np.random.seed(41232 + cont_name)
    dmin = int(np.random.randint(4,399))
    dmax = dmin + rango

    

    if dmin < dmax and dmin > 0 and p < m and m > 0:
        #print('input successful')

        mu = (dmin + dmax) / 2   
        np.random.seed(41232 + cont_name)  
        data = np.random.uniform(dmin,dmax,[m,n])
        #plt.scatter(data[:,0], data[:,1])
        #plt.show()
    
        #print(data)
        
        cont_name = str(cont_name)
        filename = "x" + cont_name
        if len(filename) != 0:
            filename+='.txt'
        else:
            filename=' '
        if filename!=' ':
            with open(filename,'w') as f:
                f.write('%r %r %r %r' % (m, n, p, int(mu)))
                f.write('\n')

                for i in range(m):
                    f.write('%r' % (i)+ " ")
                    
                    for j in range(n):
                        f.write('%r' % (data[i][j])+ " ")
                    f.write('\n')
                    
                f.close()
        

        print("input successful " + filename)

        cont_name = int(cont_name)
        cont_name += 1     
        #seed += 1  
        #np.random.seed = seed  
        #print(seed)  
    else:
        print('input failed')

