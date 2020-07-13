class Node:

    def __init__(self, value, point=None, previous=None):

        self.point = point
        self.value = value
        self.previous = previous

    def print_value(self):

        print(self.value)

        if self.value is None:
            print(None)

    def print_point(self):

        if self.point is not None:
            point = self.point
            point.print_value()

        else:
            print(None)


class myList:

    def __init__(self, head=None):

        # if element is not None:
        # element = Node(element)
        # self.head = element

        self.head = head

    def return_first(self):
        return self.head

    def append(self, appended_element):

        appended_node = Node(appended_element)

        if self.head is not None:

            pointer = self.head
            # next_element.print_value()

            while pointer.point is not None:
                pointer = pointer.point  # Goes to the penultimate element
                # print("Not Run")
                # next_element.print_value()
                # print("Has Run")

            # print("Loop Ended")
            # last_element.print_value()
            pointer.point = appended_node
            appended_node.previous = pointer

        else:
            self.head = appended_element

    def insert(self, index, inserted_element):

        inserted_node = Node(inserted_element)

        # next_element = self.select_next_element
        if index != 0:

            if self.head is None:
                self.head = inserted_node
                return self

            pointer = self.head
            for i in range(0, index - 1):
                # print(i)

                if pointer is None:
                    # print("HERE")
                    self.append(inserted_element)
                    return self

                pointer = pointer.point
            # print("Here")
            # print(pointer.value)

            inserted_node.point = pointer.point
            pointer.point = inserted_node
            # print("All Run")

        else:

            if self.head is None:
                self.head = inserted_node
                return self

            self.head.previous = inserted_node
            inserted_node.point = self.head
            self.head = inserted_node

            # print("All Run")

    def remove(self, removed_element):
        removed_node = Node(removed_element)

        if self.head.value == removed_node.value:
            # print("Run")
            # removed_node.print_value()
            if self.head.point is not None:
                self.head = self.head.point
                self.head.previous = None
                return
            else:
                self.head = Node(None)
                removed_node.point = None
                return
        else:
            pointer = self.head.point
            while pointer.value != removed_node.value:
                pointer = pointer.point

                if pointer.point is None:
                    raise ValueError("{} not in list".format(removed_element))

            # if  pointer.point != None:
            # self.print_value()
            pointer.point.previous = pointer.previous
            pointer.previous.point = pointer.point
            removed_node.point = None

    def print_list(self):

        pointer = self.head
        print("[", end="", flush=False)
        while pointer is not None:

            if pointer.point is not None:
                print(pointer.value, end=", ", flush=True)
            else:
                print(pointer.value, end="")
            pointer = pointer.point

        print("]")

    def index(self, index_element):
        index = 0
        pointer = self.head
        index_node = Node(index_element)
        while pointer.value != index_node.value:

            pointer = pointer.point
            if pointer is None:
                raise ValueError("{} is not in list".format(index_element))
            index += 1

        return index


X = myList()
X.insert(0, 1)

# X.head.print_value()
X.append(2)
X.append(3)
X.append(4)

X.print_list()
X.remove(3)
X.print_list()
X.append(1)
X.print_list()
X.insert(0, 3)
X.print_list()
X.insert(5, 2)
X.print_list()

a = [1, 2, 3]
a.insert(7, 6)
print(a)
