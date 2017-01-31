from .graph import *


def test2():

    v_1 = Vertex(1)
    v_2 = Vertex(2)
    v_4 = Vertex(4)
    v_8 = Vertex(8)
    v_16 = Vertex(16)
    v_32 = Vertex(32)
    v_64 = Vertex(64)

    e_1_8 = Edge(v_1, v_8)
    e_2_8 = Edge(v_2, v_8)
    e_4_8 = Edge(v_4, v_8)
    e_16_8 = Edge(v_16, v_8)
    e_32_8 = Edge(v_32, v_8)
    e_64_8 = Edge(v_64, v_8)
    e_1_2 = Edge(v_1, v_2)
    e_2_4 = Edge(v_2, v_4)
    e_4_16 = Edge(v_4, v_16)
    e_16_32 = Edge(v_16, v_32)
    e_32_64 = Edge(v_32, v_64)
    e_64_1 = Edge(v_64, v_1)

    V = [v_1, v_2, v_4, v_8, v_16, v_32, v_64]
    E = [e_1_8, e_2_8, e_4_8, e_16_8, e_32_8, e_64_8,
         e_1_2, e_2_4, e_4_16, e_16_32, e_32_64, e_64_1]

    G = Graph()
    G.build(V, E)

    G.display()
    print()

    G.find_universal_sink()
