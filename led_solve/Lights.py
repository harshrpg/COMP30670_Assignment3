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
           while l2 <= l4+1:
                while l1 <= l3+1:
                    if l2 < self.__L and l1 < self.__L and self.__grid[l2][l1] == False:
                        self.__grid[l2][l1]=True
                        self.__onCount+=1
                        self.__offCount-=1
                    l1+=1
                l2+=1

        elif method == "turn off":
            while l2 <= l4+1:
                while l1 <= l3+1:
                    if l2 < self.__L and l1 < self.__L and self.__grid[l2][l1] == True :
                        self.__grid[l2][l1]=False
                        self.__offCount+=1
                        self.__onCount-=1
                    l1+=1
                l2+=1

        elif method == "switch":
            while l2<=l4+1:
                while l1<=l3+1:
                    if l2 < self.__L and l1 < self.__L and self.__grid[l2][l1] == False:
                        self.__grid[l2][l1] = True
                        self.__onCount += 1
                        self.__offCount -= 1
                    elif l2 < self.__L and l1 < self.__L and self.__grid[l2][l1] == True:
                        self.__grid[l2][l1] = False
                        self.__offCount +=1
                        self.__onCount -= 1
                    l1+=1
                l2+=1

        return("Leds ON: {}, Leds OFF: {}".format(self.__onCount,self.__offCount))
