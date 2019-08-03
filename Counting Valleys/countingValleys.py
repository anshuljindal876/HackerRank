def getNumHV(path):
    heightFromSea = 0                               ## Height from sea level
    count = [0, 0, 0]                               ## Stores the number of mountains, valleys and sea levels encountered when traversing through the input
    
    for i in path:
        ## Encoding U's and D's into 1's and 0's for easy data handling
        if(i == 'U'):
            i = 1
        if(i == 'D'):
            i = -1

        heightFromSea = heightFromSea + i           ## Change current height according to path

        ## typ variable stores the "type" of path. 0 for mountain, 1 for valley and 2 for sea level
        if(heightFromSea > 0):
            typ = 0
        if(heightFromSea < 0):
            typ = 1
        if(heightFromSea == 0):
            count[typ] = count[typ] + 1             ## Count is updated only when sea level is encountered
            count[2] = count[2] + 1

    return count

if __name__ == '__main__':
    path = input()
    path = list(path)
    print("INPUT", path)

    count = getNumHV(path)
    print("Mountains, Valleys, Sea Level", count)   ## Output can be changed accordingly
