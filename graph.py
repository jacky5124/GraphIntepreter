from collections import deque, OrderedDict
from .priority_queue import *
from math import inf


class Vertex:
    def __init__(self, v):
        self.data = v


class Edge:
    def __init__(self, u, v, weight=1, flow=0):
        self.u = u
        self.v = v
        self.weight = weight
        self.flow = flow


class Graph:
    def __init__(self):
        self.v_out = {}
        self.v_in = {}

    def build(self, vertices, edges):
        self.v_out.clear()
        self.v_in.clear()
        self.v_out = {v: {} for v in vertices}
        self.v_in = {v: {} for v in vertices}
        for e in edges:
            self.v_out[e.u][e.v] = [e.weight, e.flow]
            self.v_in[e.v][e.u] = [e.weight, e.flow]

    def insert_vertex(self, v):
        if v not in self.v_out:
            self.v_out[v] = {}
            self.v_in[v] = {}
        else:
            print("The vertex is already in the graph!")

    def insert_edge(self, e):
        if e.u in self.v_out:
            if e.v in self.v_in:
                weight = self.v_out[e.u].get(e.v)
                if weight is None:
                    self.v_out[e.u][e.v] = [e.weight, e.flow]
                    self.v_in[e.v][e.u] = [e.weight, e.flow]
                else:
                    print("There is already an edge from u to v in the graph!")
            else:
                print("The vertex v of the edge is not in the graph!")
        else:
            print("The vertex u of the edge is not in the graph!")

    def delete_vertex(self, v):
        if v in self.v_out:
            del self.v_out[v]
            del self.v_in[v]
        else:
            print("There is no such vertex in the graph!")

    def delete_edge(self, e):
        if e.u in self.v_out:
            if e.v in self.v_in:
                weight = self.v_out[e.u].get(e.v)
                if weight is not None:
                    del self.v_out[e.u][e.v]
                    del self.v_in[e.v][e.u]
                else:
                    print("There is no such edge from u to v in the graph!")
            else:
                print("The vertex v of the edge is not in the graph!")
        else:
            print("The vertex u of the edge is not in the graph!")

    def display(self):
        for u, vs in sorted(self.v_out.items(), key=lambda x: x[0].data):
            print(str(u.data) + " is connected to ", end="")
            for v, weight in sorted(vs.items(), key=lambda y: y[0].data):
                print("(" + str(v.data) + ", " +
                      "w/cf=" + str(weight) + ")", end=" ")
            print()

    def transpose(self):
        all_out = self.v_out
        all_in = self.v_in
        self.v_out = all_in
        self.v_in = all_out

    def find_universal_sink(self):
        lm1 = len(self.v_out) - 1
        for v in self.v_out:
            if len(self.v_in[v]) == lm1 and len(self.v_out[v]) == 0:
                print(str(v.data) + " is a universal sink!")
                return
        print("There is no spoon^H^H^H^H_ink!")

    def breadth_first_search(self, s, t=None):
        visited = {v: False for v in self.v_out}
        new_vertices = []
        new_edges = []
        visited[s] = True
        queue = deque([])
        queue.append(s)
        while len(queue) != 0:
            u = queue.popleft()
            new_vertices.append(u)
            for v, weight in self.v_out[u].items():
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    new_edges.append(Edge(u, v, weight[0], weight[1]))
        tree = Graph()
        tree.build(new_vertices, new_edges)
        return tree

    def depth_first_search(self, s, t=None):
        visited = {v: False for v in self.v_out}
        return self.df_visit(s, visited, t=t)

    def df_visit(self, s, visited, t=None, topo=None):
        new_vertices = []
        new_edges = []
        visited[s] = True
        stack = [s]
        while len(stack) != 0:
            u = stack[len(stack) - 1]
            v = None
            weight = None
            for adj, cost in self.v_out[u].items():
                if not visited[adj]:
                    v = adj
                    weight = cost
                    break
            if v is not None:
                visited[v] = True
                stack.append(v)
                new_edges.append(Edge(u, v, weight[0], weight[1]))
            else:
                stack.pop()
                new_vertices.append(u)
                if topo is not None:
                    topo.appendleft(u)
        tree = Graph()
        tree.build(new_vertices, new_edges)
        return tree

    def depth_first_forest(self, topo=None, is_scc=False):
        forest = []
        if not is_scc:
            visited = {v: False for v in self.v_out}
            for s, v in visited.items():
                if not v:
                    forest.append(self.df_visit(s, visited, topo=topo))
        else:
            visited = OrderedDict([(v, False) for v in topo])
            for s, v in visited.items():
                if not v:
                    forest.append(self.df_visit(s, visited))
        return forest

    def find_strongly_connected_components(self):
        topology = deque([])
        self.depth_first_forest(topology)
        self.transpose()
        forest_needed = self.depth_first_forest(topology, True)
        self.transpose()
        return forest_needed

    def kruskal(self):
        def find(r):
            rep = roots[r]
            if rep == r:
                return rep
            else:
                return find(rep)

        def union(rep1, rep2):
            roots[rep1] = rep2

        new_vertices = [v for v in self.v_out]
        new_edges = []
        roots = {v: v for v in self.v_out}
        edges_to_check = []
        for u, vs in self.v_out.items():
            for v, weight in vs.items():
                edges_to_check.append(Edge(u, v, weight[0], weight[1]))
        edges_to_check.sort(key=lambda w: w.weight)
        for e in edges_to_check:
            u_rep = find(e.u)
            v_rep = find(e.v)
            if u_rep != v_rep:
                if self.v_out[e.v].get(e.u) is not None:
                    new_edges.append(e)
                    new_edges.append(Edge(e.v, e.u, e.weight, e.flow))
                    union(u_rep, v_rep)
        tree = Graph()
        tree.build(new_vertices, new_edges)
        return tree

    def prim(self):
        new_vertices = []
        new_edges = []
        min_pq = PriorityQueue(is_min=True)
        nodes = {v: PriorityNode([None, v], inf) for v in self.v_in}
        for n in nodes.values():
            min_pq.insert(n)
        source = nodes.popitem()
        min_pq.change_priority(source[1], 0)
        nodes.update([source])
        while min_pq.get_size() is not 0:
            u_node = min_pq.remove()
            p = u_node.get_data()[0]
            u = u_node.get_data()[1]
            new_vertices.append(u)
            for v, weight in self.v_out[u].items():
                v_node = nodes[v]
                if min_pq.is_inside(v_node) \
                        and weight[0] < v_node.get_priority():
                    v_node.get_data()[0] = u
                    min_pq.change_priority(v_node, weight[0])
            if p is not None:
                cost = self.v_out[u].get(p)
                if cost is not None:
                    new_edges.append(Edge(p, u, cost[0], cost[1]))
                    new_edges.append(Edge(u, p, cost[0], cost[1]))
        tree = Graph()
        tree.build(new_vertices, new_edges)
        return tree

    def bellman_ford(self, s):
        self_edges = []
        for u, vs in self.v_out.items():
            for v, weight in vs.items():
                self_edges.append(Edge(u, v, weight[0], weight[1]))
        shortest = {v: [inf, None] for v in self.v_in}
        shortest[s][0] = 0
        for i in range(len(self.v_out) - 1):
            for e in self_edges:
                v_d = shortest[e.v][0]
                u_d = shortest[e.u][0]
                if v_d > u_d + e.weight:
                    shortest[e.v][0] = u_d + e.weight
                    shortest[e.v][1] = e.u
        for e in self_edges:
            v_d = shortest[e.v][0]
            u_d = shortest[e.u][0]
            if v_d > u_d + e.weight:
                return None
        return shortest

    def dag_shortest_paths(self, s):
        topology = deque([])
        self.depth_first_forest(topology)
        shortest = {v: [inf, None] for v in self.v_in}
        shortest[s][0] = 0
        for u in topology:
            u_d = shortest[u][0]
            for v, weight in self.v_out[u].items():
                v_d = shortest[v][0]
                if v_d > u_d + weight[0]:
                    shortest[v][0] = u_d + weight[0]
                    shortest[v][1] = u
        return shortest

    def dijkstra(self, s):
        min_pq = PriorityQueue(is_min=True)
        nodes = {v: PriorityNode([None, v], inf) for v in self.v_in}
        for n in nodes.values():
            min_pq.insert(n)
        min_pq.change_priority(nodes[s], 0)
        while min_pq.get_size() is not 0:
            u_node = min_pq.remove()
            u = u_node.get_data()[1]
            u_d = u_node.get_priority()
            for v, weight in self.v_out[u].items():
                v_node = nodes[v]
                v_d = v_node.get_priority()
                if v_d > u_d + weight[0]:
                    v_d = u_d + weight[0]
                    v_node.get_data()[0] = u
                    min_pq.change_priority(v_node, v_d)
        shortest = {k: (v.get_priority(), v.get_data()[0])
                    for k, v in nodes.items()}
        return shortest

    def find_all_pairs_shortest_paths(self):
        table = {u: {v: inf for v in self.v_in} for u in self.v_out}
        answer = {u: {v: [inf, None] for v in self.v_in} for u in self.v_out}
        for u in self.v_out:
            table[u][u] = 0
            answer[u][u][0] = 0
            for v, weight in self.v_out[u].items():
                table[u][v] = weight[0]
        for k in range(len(self.v_out)):
            for i in self.v_out:
                for j in self.v_in:
                    another = inf
                    predecessor = i
                    for v in self.v_in:
                        consider = answer[i][v][0] + table[v][j]
                        if consider < another:
                            another = consider
                            predecessor = v
                    target = answer[i][j]
                    if another < target[0]:
                        target[0] = another
                        target[1] = predecessor
        return answer

    def floyd_warshall(self):
        answer = {u: {v: [inf, None] for v in self.v_in} for u in self.v_out}
        for u in self.v_out:
            answer[u][u][0] = 0
            for v, weight in self.v_out[u].items():
                target = answer[u][v]
                target[0] = weight[0]
                target[1] = u
        for k in self.v_in:
            for i in self.v_out:
                for j in self.v_in:
                    pik = answer[i][k]
                    pkj = answer[k][j]
                    consider = pik[0] + pkj[0]
                    target = answer[i][j]
                    if consider < target[0]:
                        target[0] = consider
                        target[1] = pkj[1]
        return answer

    def transitive_closure(self):
        answer = {u: {v: [False, None] for v in self.v_in} for u in self.v_out}
        for u in self.v_out:
            answer[u][u][0] = True
            for v in self.v_out[u]:
                target = answer[u][v]
                target[0] = True
                target[1] = u
        for k in self.v_in:
            for i in self.v_out:
                for j in self.v_in:
                    pik = answer[i][k]
                    pkj = answer[k][j]
                    consider = pik[0] and pkj[0]
                    target = answer[i][j]
                    if not target[0] and consider:
                        target[0] = consider
                        target[1] = pkj[1]
        return answer

    def johnson(self):
        new_vertex = Vertex('s')
        self.insert_vertex(new_vertex)
        new_edges = [Edge(new_vertex, v, 0) for v in self.v_in]
        for e in new_edges:
            self.insert_edge(e)
        shortest_from_s = self.bellman_ford(new_vertex)
        if shortest_from_s is None:
            print("There is a negative cycle in the graph!")
            return
        hs = {k: v[0] for k, v in shortest_from_s.items()}
        for u, vs in self.v_out.items():
            for v in vs:
                vs[v][0] = vs[v][0] + hs[u] - hs[v]
        self.delete_vertex(new_vertex)
        answer = {u: {v: [inf, None] for v in self.v_in} for u in self.v_out}
        for u in self.v_out:
            shortest_from_u = self.dijkstra(u)
            for v in self.v_in:
                target = answer[u][v]
                result = shortest_from_u[v]
                target[0] = result[0] + hs[v] - hs[u]
                target[1] = result[1]
        return answer

    def ford_fulkerson_with_edmonds_karp(self, s, t):
        residual_vertices = [v for v in self.v_out]
        residual_edges = [Edge(u, v, weight[0])
                          for u, vs in self.v_out.items()
                          for v, weight in vs.items()]
        residual_graph = Graph()
        residual_graph.build(residual_vertices, residual_edges)
        # do something to find augment path
        pass
