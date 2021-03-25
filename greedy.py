import time
import random
import os
from os.path import dirname

def merge(list1, list2): #Turns two lists into a **list of tuples** with the combined elements of both lists
    merged_list=tuple(zip(list1, list2))
    return merged_list
    
def greedy_start():
    listmin=[]
    listmax=[]
    for i in range(len(dij)):
        listmin.append(min(dij[i][1:])) #<--- minimum distance of each facility, aka the closest customer
        listmax.append(max(dij[i][1:]))
    vmin=min(listmin) #<------ minimum distance among the closest customers
    vmax=max(listmax)
    radius = (vmax + vmin)/2 #Greedy Start radius
    #---------------------Initial Selection----------------------------
    inside_radius=[]
    for i in range(len(dij)):
        inside_radius.append(0)
    for i in range(len(dij)):
        for j in range(n):
            if dij[i][j] <= radius:
                inside_radius[i]+=1
    #print(inside_radius)
    list_index_facilities=[]
    for i in range(m):
        list_index_facilities.append(i)
    ir = merge(list_index_facilities, inside_radius)
    irsorted=sorted(ir, key=lambda i: i[1], reverse=True) #The ones with more customers closer to them at the beggining of the list
    #print(irsorted)
    F=[]
    for i in range(p):
        F.append(irsorted[i][0])
    #gsF = calculate_distance(F) #* <---- objective function evaluation 
    #print('Objective function with Greedy start', gsF )
    return F #gsF

#*-------------------------Insta
#nce Reader------------------------------------------------------------------------------------*#
print('.txt files in directory\n')
for file in os.listdir(dirname(os.path.realpath(__file__))):#os.path.realpath(__file__)
    if file.endswith(".txt"):
        print(f"* {file} ")
print('\n')
try:
    filename=input('Enter a filename or press Enter to leave it as instancia: ')
    if len(filename) != 0:
        filename+='.txt'
except:
    filename=' '

if len(filename) == 0:    
    with open('instancia.txt', 'r') as f:
        data = f.read().splitlines()
        #datapd= pd.read_csv('instancia.txt')
        f.close()   

elif filename != ' ':
    try:
        with open(filename, 'r') as f:
            data = f.read().splitlines()
            #datapd= pd.read_csv(filename)
            f.close()
    except:
        print('Instance not received')
        

     
list_elements=[]

i=0
for e in data:
    i+=1
    #print(i)
    list_elements.append(tuple(e.split())) #.split()= each space represents another element of the tuple
#print(list_elements)
#list of tuples
m=list_elements[0][0]
n=list_elements[0][1] 
p=list_elements[0][2]
mu=list_elements[0][3]

print('Instance received')
print("The instance received contains "+ m + " facilities and "+ n + " customers \nThe amount of facilities to be opened is:", p)
print('\n')
m=int(m)
n=int(n)
p=int(p)
mu=int(mu)

x=0
dist_ij=[]
for e in data[1:]:        
    x=x+1
    dist_ij.append(data[x])

dij=[]
for e in dist_ij:
    dij.append(tuple(map(float, e.split())))
#print(dij) <-----------------------------------------Lista de listas con las distancias, cada lista representa una fila

F = greedy_start()
print(F)
