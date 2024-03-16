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

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertext(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertext in self.adj_list[vertex]:
                self.adj_list[other_vertext].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


mgraph = Graph()

mgraph.add_vertext(1)
mgraph.add_vertext(2)
mgraph.add_vertext(3)
mgraph.add_vertext(4)


mgraph.add_edge(1, 2)
mgraph.add_edge(1, 3)
mgraph.add_edge(1, 4)
mgraph.add_edge(2, 3)
mgraph.add_edge(2, 4)
mgraph.add_edge(3, 4)


mgraph.remove_vertext(4)


mgraph.print_graph()
