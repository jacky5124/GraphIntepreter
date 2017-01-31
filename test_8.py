from .graph import *


def test8():

    v_1 = Vertex(1)
    v_2 = Vertex(2)
    v_3 = Vertex(3)
    v_4 = Vertex(4)
    v_5 = Vertex(5)

    e_1_2 = Edge(v_1, v_2, 3)
    e_1_3 = Edge(v_1, v_3, 8)
    e_1_5 = Edge(v_1, v_5, -4)
    e_2_4 = Edge(v_2, v_4, 1)
    e_2_5 = Edge(v_2, v_5, 7)
    e_3_2 = Edge(v_3, v_2, 4)
    e_4_1 = Edge(v_4, v_1, 2)
    e_4_3 = Edge(v_4, v_3, -5)
    e_5_4 = Edge(v_5, v_4, 6)

    V = [v_1, v_2, v_3, v_4, v_5]
    E = [e_1_2, e_1_3, e_1_5, e_2_4, e_2_5, e_3_2, e_4_1, e_4_3, e_5_4]

    G = Graph()
    # G.build(V, E)
    for v in V:
        G.insert_vertex(v)
        G.delete_vertex(v)
        G.insert_vertex(v)
    for e in E:
        G.insert_edge(e)
        G.delete_edge(e)
        G.insert_edge(e)
    G_all_pairs_1 = G.find_all_pairs_shortest_paths()
    G_all_pairs_2 = G.floyd_warshall()
    G_transitives = G.transitive_closure()
    G_all_pairs_3 = G.johnson()

    G.display()
    print()

    for u in sorted(G_all_pairs_1.keys(), key=lambda x: x.data):
        print("shortest paths from " + str(u.data) + " are: ", end="")
        for v in sorted(G_all_pairs_1[u].keys(), key=lambda y: y.data):
            answer = G_all_pairs_1[u][v]
            if answer[1] is not None:
                predecessor = answer[1].data
            else:
                predecessor = None
            print("(" + str(v.data) + ", " +
                  "d=" + str(answer[0]) + ", " +
                  "p=" + str(predecessor) + ")", end=" ")
        print()
    print()

    for u in sorted(G_all_pairs_2.keys(), key=lambda x: x.data):
        print("shortest paths from " + str(u.data) + " are: ", end="")
        for v in sorted(G_all_pairs_2[u].keys(), key=lambda y: y.data):
            answer = G_all_pairs_2[u][v]
            if answer[1] is not None:
                predecessor = answer[1].data
            else:
                predecessor = None
            print("(" + str(v.data) + ", " +
                  "d=" + str(answer[0]) + ", " +
                  "p=" + str(predecessor) + ")", end=" ")
        print()
    print()

    for u in sorted(G_transitives.keys(), key=lambda x: x.data):
        print(str(u.data) + " has a path to ", end="")
        for v in sorted(G_transitives[u].keys(), key=lambda y: y.data):
            answer = G_transitives[u][v]
            if answer[1] is not None:
                predecessor = answer[1].data
            else:
                predecessor = None
            print("(" + str(v.data) + ", " +
                  "d=" + str(answer[0]) + ", " +
                  "p=" + str(predecessor) + ")", end=" ")
        print()
    print()

    for u in sorted(G_all_pairs_3.keys(), key=lambda x: x.data):
        print("shortest paths from " + str(u.data) + " are: ", end="")
        for v in sorted(G_all_pairs_3[u].keys(), key=lambda y: y.data):
            answer = G_all_pairs_3[u][v]
            if answer[1] is not None:
                predecessor = answer[1].data
            else:
                predecessor = None
            print("(" + str(v.data) + ", " +
                  "d=" + str(answer[0]) + ", " +
                  "p=" + str(predecessor) + ")", end=" ")
        print()
    print()
