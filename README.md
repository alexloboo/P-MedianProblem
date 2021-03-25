# P-MedianProblem

 Given a set of potential facilities, a set of customers, a function of the distance between each customer and its closest facility, determine which facilities to open to minimize the sum of the distances from each user to its closest open facility. It is assumed that the fixed costs for the location of the facilities are identical and therefore are not considered in the formulation of the problem.

# Real world aplications
• The p-median and uncapacitated location problems both consider facilities with more than enough capacity or supply to provide for all their assigned customers. However, as facilities in many cases have only a finite supply or capacity, in practice this may not always be the case. 

• Even though this problem doesn’t have capacity constraints it does give an approximation to its more “realistic” counterparts, and even with this in mind, there might be cases where capacity is not a problem. 

# First Found Strategy

•Swap two facilities with the highest sum for two that are smaller ,
check if the objective function is better than the current one, if so,
update the current solution, start over with the list of facilities.

•Once you go through the whole list of facilities and compare the ones
not in your solution to the two with the greatest sum of distances in
your solution, if you find no improvement then you are done.
