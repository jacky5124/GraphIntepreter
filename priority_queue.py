class PriorityNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def get_data(self):
        return self.data

    def get_priority(self):
        return self.priority


class PriorityQueue:
    def __init__(self, is_min=True):
        self.is_min = is_min
        self.pq = []
        self.posn = {}
        self.size = 0

    def build(self, nodes):
        pass

    def get_size(self):
        return self.size

    def is_inside(self, node):
        test = self.posn.get(node)
        return test is not None

    def insert(self, node):
        self.pq.append(node)
        node_index = self.size
        self.posn[node] = node_index
        self.size += 1
        self.bubble_up(node_index)

    def remove(self):
        if self.size > 1:
            last_index = 0
            root_index = self.size - 1

            root = self.pq[last_index]
            last = self.pq[root_index]
            self.pq[last_index] = last
            self.posn[last] = last_index

            self.pq.pop()
            del self.posn[root]
            self.size -= 1

            self.bubble_down(last_index)

            return root

        elif self.size is 1:
            self.size -= 1
            return self.pq.pop()

        else:
            return None

    def change_priority(self, node, new_priority):
        if node.priority > new_priority:
            node.priority = new_priority
            if self.is_min:
                self.bubble_up(self.posn[node])
            else:
                self.bubble_down(self.posn[node])
        else:
            node.priority = new_priority
            if self.is_min:
                self.bubble_down(self.posn[node])
            else:
                self.bubble_up(self.posn[node])

    def bubble_down(self, index):
        target_index = index
        target = self.pq[index]
        while not self.is_leaf(target_index):
            child_index = self.higher_priority_child_index(target_index)
            higher_child = self.pq[child_index]
            if target.priority < higher_child.priority:
                if self.is_min:
                    break
                else:
                    self.pq[child_index] = target
                    self.posn[target] = child_index
                    self.pq[target_index] = higher_child
                    self.posn[higher_child] = target_index
                    target_index = child_index
            else:
                if self.is_min:
                    self.pq[child_index] = target
                    self.posn[target] = child_index
                    self.pq[target_index] = higher_child
                    self.posn[higher_child] = target_index
                    target_index = child_index
                else:
                    break

    def bubble_up(self, index):
        target_index = index
        target = self.pq[index]
        while target_index is not 0:
            parent_index = (target_index - 1) // 2
            parent = self.pq[parent_index]
            if target.priority < parent.priority:
                if self.is_min:
                    self.pq[target_index] = parent
                    self.posn[parent] = target_index
                    self.pq[parent_index] = target
                    self.posn[target] = parent_index
                    target_index = parent_index
                else:
                    break
            else:
                if self.is_min:
                    break
                else:
                    self.pq[target_index] = parent
                    self.posn[parent] = target_index
                    self.pq[parent_index] = target
                    self.posn[target] = parent_index
                    target_index = parent_index

    def is_leaf(self, index):
        return 2 * index + 1 >= self.size

    def higher_priority_child_index(self, index):
        left_child_index = 2 * index + 1
        left_child = self.pq[left_child_index]
        if left_child_index == self.size - 1:
            return left_child_index
        else:
            right_child_index = left_child_index + 1
            right_child = self.pq[right_child_index]
            if left_child.priority < right_child.priority:
                if self.is_min:
                    return left_child_index
                else:
                    return right_child_index
            else:
                if self.is_min:
                    return right_child_index
                else:
                    return left_child_index
