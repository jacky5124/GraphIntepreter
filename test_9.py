from .graph import *


def test9():

    v_s = Vertex('s')
    v_t = Vertex('t')
    v_v1 = Vertex('v1')
    v_v2 = Vertex('v2')
    v_v3 = Vertex('v3')
    v_v4 = Vertex('v4')

    e_s_v1 = Edge(v_s, v_v1, 16)
    e_s_v2 = Edge(v_s, v_v2, 13)
    e_v1_v3 = Edge(v_v1, v_v3, 12)
    e_v2_v1 = Edge(v_v2, v_v1, 4)
    e_v2_v4 = Edge(v_v2, v_v4, 14)
    e_v3_v2 = Edge(v_v3, v_v2, 9)
    e_v3_t = Edge(v_v3, v_t, 20)
    e_v4_v3 = Edge(v_v4, v_v3, 7)
    e_v4_t = Edge(v_v4, v_t, 4)

    V = [v_s, v_t, v_v1, v_v2, v_v3, v_v4]
    E = [e_s_v1, e_s_v2, e_v1_v3, e_v2_v1, e_v2_v4,
         e_v3_v2, e_v3_t, e_v4_v3, e_v4_t]
    G = Graph()
    G.build(V, E)
    G.display()
