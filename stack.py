# -----------------------------
# TP 05 du 11/10/2017
# Module stack
# Version 1 du 10/10/2017
# -----------------------------

class EmptyStack(Exception):
    pass


class Stack(object):
    def __init__(self):
        self.__list = []

    def IsEmpty(self):
        return self.__list == []

    def Push(self, x):
        self.__list.append(x)

    def Pop(self):
        if self.IsEmpty():
            raise EmptyStack
        else:
            return self.__list.pop()

    def Print(self):
        print(self.__list)
