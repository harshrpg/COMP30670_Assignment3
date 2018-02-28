class Lights(object):

    def __init__(self, L):
        """Constructor for the class"""
        self.__L = L
        self.__grid =  [[False]*self.__L for i in range(self.__L)]
        self.__onCount = 0
        self.__offCount = L*L
