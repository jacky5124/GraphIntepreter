from .graph import *


def test6():

    v_r = Vertex('r')
    v_s = Vertex('s')
    v_t = Vertex('t')
    v_x = Vertex('x')
    v_y = Vertex('y')
    v_z = Vertex('z')

    e_r_s = Edge(v_r, v_s, 5)
    e_r_t = Edge(v_r, v_t, 3)
    e_s_t = Edge(v_s, v_t, 2)
    e_s_x = Edge(v_s, v_x, 6)
    e_t_x = Edge(v_t, v_x, 7)
    e_t_y = Edge(v_t, v_y, 4)
    e_t_z = Edge(v_t, v_z, 2)
    e_x_y = Edge(v_x, v_y, -1)
    e_x_z = Edge(v_x, v_z, 1)
    e_y_z = Edge(v_y, v_z, -2)

    V = [v_r, v_s, v_t, v_x, v_y, v_z]
    E = [e_r_s, e_r_t, e_s_t, e_s_x, e_t_x, e_t_y, e_t_z, e_x_y, e_x_z, e_y_z]

    G = Graph()
    G.build(V, E)
    G_shortest_path = G.dag_shortest_paths(v_s)

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
