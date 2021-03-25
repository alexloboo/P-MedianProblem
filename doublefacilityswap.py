import time
import random
import os
from os.path import dirname
import winsound

def merge(list1, list2):  # Turns two lists into a **list of tuples** with the combined elements of both lists
    merged_list = tuple(zip(list1, list2))
    return merged_list


def greedy_start():
    listmin = []
    listmax = []
    for i in range(len(dij)):
        listmin.append(min(dij[i][1:]))  # <--- minimum distance of each facility, aka the closest customer
        listmax.append(max(dij[i][1:]))
    vmin = min(listmin)  # <------ minimum distance among the closest customers
    vmax = max(listmax)
    radius = (vmax + vmin) / 2  # Greedy Start radius
    # ---------------------Initial Selection----------------------------
    inside_radius = []
    for i in range(len(dij)):
        inside_radius.append(0)
    for i in range(len(dij)):
        for j in range(n):
            if dij[i][j] <= radius:
                inside_radius[i] += 1
    # print(inside_radius)
    list_index_facilities = []
    for i in range(m):
        list_index_facilities.append(i)
    ir = merge(list_index_facilities, inside_radius)
    irsorted = sorted(ir, key=lambda i: i[1],
                    reverse=True)  # The ones with more customers closer to them at the beggining of the list
    # print(irsorted)
    F = []
    for i in range(p):
        F.append(irsorted[i][0])
    # gsF = calculate_distance(F) #* <---- objective function evaluation
    # print('Objective function with Greedy start', gsF )
    return F  # gsF


def doubleFacility(solution, greedySolution):
    newSolution = 0
    noSol = []
    for i in range(0, m):
        noSol.append(i)
    for i in solution:
        noSol.remove(i)

    vector_solution = getLineFacilitySumMax(solution)
    z = 0
    k = 0
    temp = []
    while k < len(noSol)-1:
        a = 0
        b = 0
        a = vector_solution[z]
        b = vector_solution[z+1]
        vector_solution[z] = noSol[k]
        vector_solution[z+1] = noSol[k+1]
        newSolution = findObjective(vector_solution)
        if newSolution < greedySolution:
            noSol.append(a)
            noSol.append(b)
            noSol.remove(noSol[k])
            noSol.remove(noSol[k])
            k = 0
            greedySolution = newSolution
            temp = vector_solution
            solution = temp
            vector_solution = getLineFacilitySumMax(solution)
            #print(vector_solution)
        else:
            k += 2
            vector_solution[z] = a
            vector_solution[z+1] = b

    return vector_solution


def findObjective(solution):
    aux = []
    sum = 0
    for i in range(1, n + 1):
        for j in solution:
            aux.append(dij[j][i])
        sum = sum + min(aux)
        aux = []
    return sum


def distanceFacility(facility):
    add = 0
    for i in range(0, n+1):
        if i != 0:
            add = add + int(dij[facility][i])
    return add


def getLineFacilitySumMax(vector):
    auxiliary = []
    s = 0
    newOrderFacilities = []
    for i in vector:
        s = distanceFacility(i)
        auxiliary.append(s)
        s = 0
    notOrder = auxiliary
    order = sorted(auxiliary, reverse=True)

    for j in order:
        index = notOrder.index(j)
        elem = vector[index]
        newOrderFacilities.append(elem)
        vector.remove(elem)
        notOrder.remove(j)

    return newOrderFacilities


# *-------------------------Instance Reader------------------------------------------------------------------------------------*#
print('.txt files in directory\n')
for file in os.listdir(dirname(os.path.realpath(__file__))):  # os.path.realpath(__file__)
    if file.endswith(".txt"):
        print(f"* {file} ")
print('\n')
try:
    filename = input('Enter a filename or press Enter to leave it as instancia: ')
    flname = filename
    if len(filename) != 0:
        fls=filename;
        filename += '.txt'
except:
    filename = ' '

if len(filename) == 0:
    with open('instancia.txt', 'r') as f:
        data = f.read().splitlines()
        # datapd= pd.read_csv('instancia.txt')
        f.close()

elif filename != ' ':
    try:
        with open(filename, 'r') as f:
            data = f.read().splitlines()
            # datapd= pd.read_csv(filename)
            f.close()
    except:
        print('Instance not received')

list_elements = []
i = 0
for e in data:
    i += 1
    # print(i)
    list_elements.append(tuple(e.split()))  # .split()= each space represents another element of the tuple
# print(list_elements)
# list of tuples
m = list_elements[0][0]
n = list_elements[0][1]
p = list_elements[0][2]
#mu = list_elements[0][3]

print('Instance received')
print("The instance received contains " + m + " facilities and " + n + " customers \nThe amount of facilities to be opened is:",p)
print('\n')
m = int(m)
n = int(n)
p = int(p)
#mu = int(mu)

x = 0
dist_ij = []
for e in data[1:]:
    x = x + 1
    dist_ij.append(data[x])
# print(dist_ij)
dij = []
for e in dist_ij:
    dij.append(tuple(map(float, e.split())))
# print(dij) #<-----------------------------------------Lista de listas con las distancias, cada lista representa una fila

# Greedy
F = greedy_start()
print("Greedy Facilities Solution: ", F)

# End Greedy
solution_global = F
D = findObjective(solution_global)
print("Objective Function: ", D)
start_time = time.time()
newFacilities = doubleFacility(F, D)
print("\nTime: %s sec" % (time.time() - start_time))
print("New Facilities: ", newFacilities)
print("New Distance: ", findObjective(newFacilities))
print("Difference: ", findObjective(newFacilities)-D)

prnt1 = "%s, %s" %("time","obj Fun")
prnt2 = "%s,%s" %((time.time() - start_time),(findObjective(newFacilities)))

print(prnt2, file=open("Resultados.txt", "a"))
duration = 2000  # milliseconds
freq = 550  # Hz
winsound.Beep(freq, duration)