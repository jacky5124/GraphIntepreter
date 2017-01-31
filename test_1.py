from .graph import *


def test1():

    v_1 = Vertex(1)
    v_2 = Vertex(2)
    v_3 = Vertex(3)
    v_4 = Vertex(4)
    v_5 = Vertex(5)
    v_6 = Vertex(6)

    e_1_2 = Edge(v_1, v_2)
    e_1_4 = Edge(v_1, v_4)
    e_2_5 = Edge(v_2, v_5)
    e_3_5 = Edge(v_3, v_5)
    e_3_6 = Edge(v_3, v_6)
    e_4_2 = Edge(v_4, v_2)
    e_5_4 = Edge(v_5, v_4)
    e_6_6 = Edge(v_6, v_6)

    V = [v_1, v_2, v_3, v_4, v_5, v_6]
    E = [e_1_2, e_1_4, e_2_5, e_3_5, e_3_6, e_4_2, e_5_4, e_6_6]

    G = Graph()
    G.build(V, E)
    G_BFS = G.breadth_first_search(v_1)
    G_DFS = G.depth_first_search(v_1)
    T = deque([])
    G_DFF = G.depth_first_forest(T)

    G.display()
    print()

    G.transpose()
    G.display()
    print()

    G.transpose()
    G.display()
    print()

    G_BFS.display()
    print()

    G_DFS.display()
    print()

    print("-------- forest begins! --------\n")
    for i in range(len(G_DFF)):
        G_DFF[i].display()
        print()
    print("--------  forest ends!  --------\n")

    for j in range(len(T)):
        print(T[j].data, end=" ")
    print("\n")

    G.find_universal_sink()
