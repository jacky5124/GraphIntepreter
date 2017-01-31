from .graph import *


def test4():

    v_a = Vertex('a')
    v_b = Vertex('b')
    v_c = Vertex('c')
    v_d = Vertex('d')
    v_e = Vertex('e')
    v_f = Vertex('f')
    v_g = Vertex('g')
    v_h = Vertex('h')
    v_i = Vertex('i')

    e_a_b = Edge(v_a, v_b, 4)
    e_a_h = Edge(v_a, v_h, 8)
    e_b_a = Edge(v_b, v_a, 4)
    e_b_c = Edge(v_b, v_c, 8)
    e_b_h = Edge(v_b, v_h, 11)
    e_c_b = Edge(v_c, v_b, 8)
    e_c_d = Edge(v_c, v_d, 7)
    e_c_f = Edge(v_c, v_f, 4)
    e_c_i = Edge(v_c, v_i, 2)
    e_d_c = Edge(v_d, v_c, 7)
    e_d_e = Edge(v_d, v_e, 9)
    e_d_f = Edge(v_d, v_f, 14)
    e_e_d = Edge(v_e, v_d, 9)
    e_e_f = Edge(v_e, v_f, 10)
    e_f_c = Edge(v_f, v_c, 4)
    e_f_d = Edge(v_f, v_d, 14)
    e_f_e = Edge(v_f, v_e, 10)
    e_f_g = Edge(v_f, v_g, 2)
    e_g_f = Edge(v_g, v_f, 2)
    e_g_h = Edge(v_g, v_h, 1)
    e_g_i = Edge(v_g, v_i, 6)
    e_h_a = Edge(v_h, v_a, 8)
    e_h_b = Edge(v_h, v_b, 11)
    e_h_g = Edge(v_h, v_g, 1)
    e_h_i = Edge(v_h, v_i, 7)
    e_i_c = Edge(v_i, v_c, 2)
    e_i_g = Edge(v_i, v_g, 6)
    e_i_h = Edge(v_i, v_h, 7)

    V = [v_a, v_b, v_c, v_d, v_e, v_f, v_g, v_h, v_i]
    E = [e_a_b, e_a_h, e_b_a, e_b_c, e_b_h, e_c_b, e_c_d, e_c_f, e_c_i, e_d_c,
         e_d_e, e_d_f, e_e_d, e_e_f, e_f_c, e_f_d, e_f_e, e_f_g, e_g_f, e_g_h,
         e_g_i, e_h_a, e_h_b, e_h_g, e_h_i, e_i_c, e_i_g, e_i_h]

    G = Graph()
    G.build(V, E)
    G_MST_K = G.kruskal()
    G_MST_P = G.prim()

    G.display()
    print()

    G_MST_K.display()
    print()

    G_MST_P.display()
