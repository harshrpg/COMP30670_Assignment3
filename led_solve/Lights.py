class Lights(object):

    def __init__(self, L):
        """Constructor for the class"""
        self.__L = L
        self.__grid = [[False]*self.__L for i in range(self.__L)]
        self.__onCount = 0
        self.__offCount = L*L

    def runCmd(self, method, l1, l2, l3, l4):
        # print('Inside runcms')
        """Toggle the state of lights"""
        if method == "turn on":
            if l1 <= l3 and l2 <= l4:
                for row in range(l2, l4+1):
                    # print(l4)
                    # print(row)
                    for i, r in enumerate(self.__grid[row]):
                        if i >= l1 and i <= l3 and self.__grid[row][i] == False:
                            self.__grid[row][i] = True

        elif method == "turn off":
            if l1 <= l3 and l2 <= l4:
                for row in range(l2, l4+1):
                    # print(l4)
                    # print(row)
                    for i, r in enumerate(self.__grid[row]):
                        if i >= l1 and i <= l3 and self.__grid[row][i] == True:
                            self.__grid[row][i] = False

        elif method == "switch":
            if l1 <= l3 and l2 <= l4:
                for row in range(l2, l4+1):
                    # print(l4)
                    # print(row)
                    for i, r in enumerate(self.__grid[row]):
                        if i >= l1 and i <= l3:
                            if self.__grid[row][i]:
                                self.__grid[row][i] = False
                            else:
                                self.__grid[row][i] = True

    def counts(self):
        self.__onCount = (sum([row.count(True) for row in self.__grid]))
        self.__offCount = self.__offCount-self.__onCount
        return(self.__onCount, self.__offCount)
