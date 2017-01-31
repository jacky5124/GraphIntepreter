from .graph import *


def test3():

    v_a = Vertex('a')
    v_b = Vertex('b')
    v_c = Vertex('c')
    v_d = Vertex('d')
    v_e = Vertex('e')
    v_f = Vertex('f')
    v_g = Vertex('g')
    v_h = Vertex('h')

    e_a_b = Edge(v_a, v_b)
    e_b_c = Edge(v_b, v_c)
    e_b_e = Edge(v_b, v_e)
    e_b_f = Edge(v_b, v_f)
    e_c_d = Edge(v_c, v_d)
    e_c_g = Edge(v_c, v_g)
    e_d_c = Edge(v_d, v_c)
    e_d_h = Edge(v_d, v_h)
    e_e_a = Edge(v_e, v_a)
    e_e_f = Edge(v_e, v_f)
    e_f_g = Edge(v_f, v_g)
    e_g_f = Edge(v_g, v_f)
    e_g_h = Edge(v_g, v_h)
    e_h_h = Edge(v_h, v_h)

    V = [v_a, v_b, v_c, v_d, v_e, v_f, v_g, v_h]
    E = [e_a_b, e_b_c, e_b_e, e_b_f, e_c_d, e_c_g, e_d_c,
         e_d_h, e_e_a, e_e_f, e_f_g, e_g_f, e_g_h, e_h_h]

    G = Graph()
    G.build(V, E)

    G_SCC = G.find_strongly_connected_components()
    G.display()
    print()

    print("-------- forest begins! --------\n")
    for i in range(len(G_SCC)):
        G_SCC[i].display()
        print()
    print("--------  forest ends!  --------\n")
