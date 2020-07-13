# Trees are a part of graph theory
class Node:
    def __init__(self, payload, parent=None):
        self.payload = payload
        self.children = list()
        self.parent = parent

    def set_parent(self, new_parent):
        self.parent = new_parent

    def add_child(self, new_child):
        self.children.append(new_child)

    def print_all_nodes(self):
        has_run = False
        if has_run is False:
            print("[", end="")
            print(self.payload, end=", ")

        else:
            print(self.payload, end="")
            # print("[", end="")

        for child in self.children:
            # print("This is {}".format(child.payload))
            if child is None:
                # print(None, end=", ")
                continue
            child.print_all_nodes()

        print("]", end="")

    def find_element(self, element):
        if self.payload == element:
            return self

        # count = 0

        for child in self.children:
            # count += 1
            # if child is None:
            # continue

            child_answer = child.find_element(element)
            if child_answer is not None:
                return child_answer

        return None

    def sort_children(self):
        if len(self.children) < 2:
            print("You're sorting with a unsaturated list.")
            return

        elif self.children[0].payload < self.children[1].payload:
            return

        self.children.append(self.children[0])
        self.children.remove(self.children[0])

    def work_through_tree(self, element, current_parent_node):

        if element <= current_parent_node.payload:

            if not len(current_parent_node.children):
                node_child = Node(element)
                current_parent_node.add_child(node_child)
                node_child.set_parent(current_parent_node)

                return

            elif len(current_parent_node.children) == 2:
                current_parent_node = current_parent_node.children[0]
                current_parent_node.work_through_tree(element, current_parent_node)
                return

            elif current_parent_node.children[0].payload <= current_parent_node.payload:

                current_parent_node = current_parent_node.children[0]
                current_parent_node.work_through_tree(element, current_parent_node)
                return

            node_child = Node(element)
            current_parent_node.add_child(node_child)
            node_child.set_parent(current_parent_node)

            if len(current_parent_node.children) == 2:
                # my_tree.print_elements()
                # print("Hi")
                current_parent_node.sort_children()
                # print("Bye")
                my_tree.print_elements()
            return

            # if len(current_parent_node.children) == 0:
            #     current_parent_node.children.append(Node(element))
            #     return
            #
            # elif len(current_parent_node.children) == 2:
            #     current_parent_node.children[0] = Node(element)
            #     return

        else:

            if not len(current_parent_node.children):
                node_child = Node(element)
                current_parent_node.add_child(node_child)
                node_child.set_parent(current_parent_node)
                return

            elif len(current_parent_node.children) == 2:
                current_parent_node = current_parent_node.children[1]
                current_parent_node.work_through_tree(element, current_parent_node)
                return

            elif current_parent_node.children[0].payload > current_parent_node.payload:

                current_parent_node = current_parent_node.children[0]
                current_parent_node.work_through_tree(element, current_parent_node)
                return

            node_child = Node(element)
            current_parent_node.add_child(node_child)
            node_child.set_parent(current_parent_node)

            if len(current_parent_node.children) == 2:
                # my_tree.print_elements()
                # print("Hi")
                current_parent_node.sort_children()
                # print("Bye")
                # my_tree.print_elements()
            return

            # if len(current_parent_node.children) == 1:
            #     current_parent_node.children.append(Node(element))
            #     return
            #
            # elif len(current_parent_node.children) == 0:
            #     current_parent_node.children.append(Node(None))
            #     current_parent_node.children.append(Node(element))
            #     return
            #
            #
            #
            #
            #
            #
            # current_parent_node = current_parent_node.children[1]
            # current_parent_node.work_through_tree(element, current_parent_node)
            #

    def find_right_subtree_minimum(self):

        benchmark = self.children[1]
        # print(benchmark.payload)
        minimum_node = self.children[1].find_minimum(benchmark)
        return minimum_node

    def find_minimum(self, benchmark):
        # print(self.payload)
        # print(benchmark.payload)

        if self.payload < benchmark.payload:
            return 0

        for child in self.children:
            child_answer = child.find_minimum(benchmark)

            if child_answer == 0:
                benchmark = child

        return benchmark

    def remove_node(self):

        if not len(self.children):
            # print("A")
            self.parent.children.remove(self)

        elif len(self.children) == 1:
            # print("B")
            self.parent.children.append(self.children[0])
            self.parent.sort_children()
            self.parent.children.remove(self)

        else:
            # print("C")
            minimum = self.find_right_subtree_minimum()
            # print(minimum.payload)
            # print(removed_node.payload)
            # print(minimum.payload)
            # removed_node = minimum
            # print(removed_node.payload)
            self.parent.children.append(Node(minimum.payload))

            # print(removed_node.parent.children[2].payload)
            self.parent.children[2].children = self.children
            self.parent.sort_children()
            self.parent.children.remove(self)
            minimum.remove_node()


class Tree:

    def __init__(self, head=None):
        self.head = head

    def insert(self, element):

        if self.head is None:
            self.head = Node(element, None)
            return

        current_parent_node = self.head
        current_parent_node.work_through_tree(element, current_parent_node)

    def find_(self, element):
        if self.head is None:
            return None
        else:
            return self.head.find_element(element)

    def is_in_tree(self, element):
        if self.find_(element) is not None:
            return True
        else:
            return False

    # def go_to_removal(self):
    #     current_node = self.head
    #     while Node(element) not in current_node.children:
    #         for child in current_node.children:

    def remove(self, element):
        if self.head.payload == element:
            print("Don't know what to do with the BST when the head needs to be removed.")
            return
        # return [child_answer, child]
        removed_node = self.find_(element)
        # print(parent.payload)
        # print(removed_node.payload)
        removed_node.remove_node()

        # parent.children.remove(removed_node)
        return
        # if parent.childnren.payload <= values[1].payload:
        #     values[1].children[0] = values[0].children
        #     return
        #
        # values[1].children[1] = values[0].children
        # return

        #
        # current_node = self.head
        # while Node(element) not in current_node.children:
        #     for child in current_node.children:

        # if self.payload == element:
        #     return self
        #
        # for child in self.children:
        #     # if child is None:
        #         # continue
        #
        #     child_answer = child.find_element(element)
        #     if child_answer is not None:
        #         return [child_answer, child]
        #
        # return None

    def print_elements(self):
        self.head.print_all_nodes()


my_tree = Tree()
my_tree.insert(5)
# my_tree.head.print_all_nodes()
my_tree.insert(10)
my_tree.insert(4)
# my_tree.insert(7)
# my_tree.insert(15)
# my_tree.insert(11)
# my_tree.insert(16)
# my_tree.insert(12)
my_tree.print_elements()
# my_tree.insert(3)
# my_tree.insert(8)
# my_tree.insert(7)
# my_tree.remove(10)
my_tree.print_elements()
# print(my_tree.head.children[1].payload)
# %% codecell
# my_tree.print_elements()
# print(my_tree.head.children[1].children[0].parent.payload)
# my_tree.head.print_all_nodes()
# <codecell>
# print(my_tree.is_in_tree(6))
# my_tree.print_elements()
# %% md
# <codecell>
# print(None < 2)
# print(my_tree.head.payload)
