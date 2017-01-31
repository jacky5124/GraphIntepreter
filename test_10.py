from .graph import *


def test10():
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')

    e1 = Edge(a, c, 0)
    e2 = Edge(a, b, 1)
    e3 = Edge(a, d, 99)
    e4 = Edge(b, c, 1)
    e5 = Edge(d, b, -300)

    V = [a, b, c, d]
    E = [e1, e2, e3, e4, e5]
    G = Graph()
    G.build(V, E)
    shortest = G.dijkstra(a)

    for u in sorted(shortest.keys(), key=lambda x: x.data):
        print("shortest paths from " + str(u.data) + " are: ", end="")
        for v in sorted(shortest[u].keys(), key=lambda y: y.data):
            answer = shortest[u][v]
            if answer[1] is not None:
                predecessor = answer[1].data
            else:
                predecessor = None
            print("(" + str(v.data) + ", " +
                  "d=" + str(answer[0]) + ", " +
                  "p=" + str(predecessor) + ")", end=" ")
        print()
    print()
