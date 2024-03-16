class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertext(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True

        return False


mgraph = Graph()

mgraph.add_vertext("A")

mgraph.print_graph()
