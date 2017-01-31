from .graph import *


def test7():

    v_s = Vertex('s')
    v_t = Vertex('t')
    v_x = Vertex('x')
    v_y = Vertex('y')
    v_z = Vertex('z')

    e_s_t = Edge(v_s, v_t, 10)
    e_s_y = Edge(v_s, v_y, 5)
    e_t_x = Edge(v_t, v_x, 1)
    e_t_y = Edge(v_t, v_y, 2)
    e_x_z = Edge(v_x, v_z, 4)
    e_y_t = Edge(v_y, v_t, 3)
    e_y_x = Edge(v_y, v_x, 9)
    e_y_z = Edge(v_y, v_z, 2)
    e_z_s = Edge(v_z, v_s, 7)
    e_z_x = Edge(v_z, v_x, 6)

    V = [v_s, v_t, v_x, v_y, v_z]
    E = [e_s_t, e_s_y, e_t_x, e_t_y, e_x_z, e_y_t, e_y_x, e_y_z, e_z_s, e_z_x]

    G = Graph()
    G.build(V, E)
    G_shortest_path = G.dijkstra(v_s)

    G.display()
    print()

    print("shortest path from " + str(v_s.data) + " is: ", end="")
    for v in sorted(G_shortest_path.keys(), key=lambda y: y.data):
        answer = G_shortest_path[v]
        if answer[1] is not None:
            predecessor = answer[1].data
        else:
            predecessor = None
        print("(" + str(v.data) + ", " +
              "d=" + str(answer[0]) + ", " +
              "p=" + str(predecessor) + ")", end=" ")
    print()
