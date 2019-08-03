"""
DESCRIPTION:-
Emma is playing a new mobile game involving clouds, C(i), numbered '0' from to 'N-1'. A player initially starts
out on cloud 0, and they must jump to cloud (N-1). In each step, she can jump from any cloud 'i' to cloud (i+1) or cloud (i+2).
There are two types of clouds, ordinary clouds and thunderclouds. The game ends if Emma jumps onto a thundercloud.
If she reaches the last cloud, i.e., C(N-1), she wins the game.

TASK:-
To find the minimum number of jumps Emma must make to win the game. It is guaranteed that
clouds C(0) and C(N-1) are ordinary clouds and it is always possible to win the game.

INPUT:-
The first line contains an integer, N, denoting the total number of clouds.
The second line contains N space-separated binary integers describing clouds (0 for ordinary and 1 for thunder clous)

OUTPUT:-
Print the minimum number of jumps needed to win the game.
"""
import math as M
import BFS_shortestPath as bfs  ## Included BFS algorithm file for shortest path calculation in linear time

def getJumps(arr):
    d = {}
    for i in range(len(arr)):
        if(arr[i] == 0):
            ## Dictionary is formatted into adjacency list so that BFS algorithm can be implemented
            d[i] = {}
            d[i]['edges'] = []
            d[i]['isVisited'] = False
            d[i]['distance'] = M.inf
            
            for j in range(len(arr)):
                ## Condition defined to allow connection between visitable nodes as advised in task (jumps allowed from i to (i+1) or (i+2))
                if((j == i or j == i-1 or j == i-2 or j == i+1 or j == i+2) and j != i and arr[j] == 0):
                    d[i]['edges'].append(j)

    return bfs.BFS(d, 0)

if __name__ == '__main__':
##    input()
##    clouds = input().split()
    clouds = "0 0 1 0 0 1 0".split()
    clouds = [int(i) for i in clouds]
    print("INPUT", clouds)

    minJumps = getJumps(clouds)
    print(minJumps)
