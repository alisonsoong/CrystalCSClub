

class Node:

    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id

    def getName(self) -> str:
        return self.name

    def getId(self):
        return self.id


class Edge:

    def __init__(self, start:int, end:int, weight:int):
        self.start = start
        self.end = end
        self.weight = weight

    def getCon(self):
        return (self.start, self.end)


def main():

    numRooms = 6
    names = ["M1",
            "M2",
            "M3",
            "M4",
            "M5",
            "M6"]
    nodes = [Node(names[i]) for i in range(numRooms)]

    arr = []
    for i in range(numRooms):
        arr.append(Node(names[i]))


    








        