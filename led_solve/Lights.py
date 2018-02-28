class Lights(object):

    def __init__(self, L):
        """Constructor for the class"""
        self.__L = L
        self.__grid =  [[False]*self.__L for i in range(self.__L)]
        self.__onCount = 0
        self.__offCount = L*L

    def runCmd(self, method, l1, l2, l3, l4):
        """Toggle the state of lights"""
        if method == "turn on":
            for r in range(l1,l3+1):
                for c in range(l2,l4+1):
                    if self.__grid[r][c]==False:
                        self.__grid[r][c]=True
                        self.__onCount+=1
                        self.__offCount-=1

        elif method == "turn off":
            for r in range(l1,l3+1):
                for c in range(l2,l4+1):
                    if self.__grid[r][c] == True:
                        self.__grid[r][c]=False
                        self.__offCount+=1
                        self.__onCount-=1

        elif method == "switch":
            for r in range(l1,l3+1):
                for c in range(l2,l4+1):
                    if self.__grid[r][c] == True:
                        self.__grid[r][c]=False
                        self.__offCount+=1
                        self.__onCount-=1
                    else:
                        self.__grid[r][c]=False
                        self.__onCount+=1
                        self.__offCount-=1
        return(self.__onCount,self.__offCount)