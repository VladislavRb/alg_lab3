from math import ceil


class Node:
    def __init__(self, value: int, parent=None, left_child=None, right_child=None):
        self.value = value

        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

        self.left_children_amount = 0
        self.right_children_amount = 0

    def __str__(self):
        node_str = "Value = " + str(self.value)

        if self.parent:
            node_str += ", parent value = " + str(self.parent.value)

        if self.left_child:
            node_str += ", left child value = " + str(self.left_child.value)

        if self.right_child:
            node_str += ", right child value = " + str(self.right_child.value)

        return node_str


class BinaryTree:
    def __init__(self, arr: list):
        self.root = Node(arr[0])

        for i in range(1, len(arr)):
            self.insert_node(Node(arr[i]))

    def insert_node(self, new_node: Node):
        current_node = self.root

        while True:
            if new_node.value <= current_node.value:
                current_node.left_children_amount += 1

                if current_node.left_child:
                    current_node = current_node.left_child
                else:
                    current_node.left_child = new_node
                    new_node.parent = current_node
                    break
            else:
                current_node.right_children_amount += 1

                if current_node.right_child:
                    current_node = current_node.right_child
                else:
                    current_node.right_child = new_node
                    new_node.parent = current_node
                    break

    def min(self):
        current_node = self.root

        while current_node.left_child:
            current_node = current_node.left_child

        return current_node.value

    def max(self):
        current_node = self.root

        while current_node.right_child:
            current_node = current_node.right_child

        return current_node.value

    def k_min_node(self, k: int, start_node: Node):
        current_node = start_node

        while not k == current_node.left_children_amount + 1:
            if k <= current_node.left_children_amount:
                current_node = current_node.left_child
            else:
                k -= current_node.left_children_amount + 1
                current_node = current_node.right_child

        return current_node

    def __height_from_node_to_node(self, start_node: Node, end_node: Node):
        current_node = start_node
        height = 0

        while not current_node.value == end_node.value:
            height += 1

            if end_node.value <= current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

        return height

    def __fill_sorted_array(self, sorted_arr: list, current_node: Node, reverse: bool):
        if reverse:
            if current_node.right_child:
                self.__fill_sorted_array(sorted_arr, current_node.right_child, reverse)

            sorted_arr.append(current_node.value)

            if current_node.left_child:
                self.__fill_sorted_array(sorted_arr, current_node.left_child, reverse)
        else:
            if current_node.left_child:
                self.__fill_sorted_array(sorted_arr, current_node.left_child, reverse)

            sorted_arr.append(current_node.value)

            if current_node.right_child:
                self.__fill_sorted_array(sorted_arr, current_node.right_child, reverse)

    def get_sorted_array(self, reverse=False):
        sorted_arr = []

        self.__fill_sorted_array(sorted_arr, self.root, reverse)

        return sorted_arr

    # def get_node_by_value(self, value: int):
    #     current_node = self.root
    #
    #     while not current_node.value == value:
    #         if value <= current_node.value:
    #             current_node = current_node.left_child
    #         else:
    #             current_node = current_node.right_child
    #
    #     return current_node

    def __fill_heights_array(self, node: Node, arr: list, height_counter=0):
        if node.left_child and node.right_child:
            self.__fill_heights_array(node.left_child, arr, height_counter + 1)
            self.__fill_heights_array(node.right_child, arr, height_counter + 1)
        elif not node.left_child and node.right_child:
            self.__fill_heights_array(node.right_child, arr, height_counter + 1)
        elif node.left_child and not node.right_child:
            self.__fill_heights_array(node.left_child, arr, height_counter + 1)
        else:
            arr.append(height_counter)

    def get_height(self, node: Node):
        heights_arr = []

        self.__fill_heights_array(node, heights_arr)

        return max(heights_arr)

    def get_balance_factor(self, node: Node):
        if node.left_child and node.right_child:
            return self.get_height(node.left_child) - self.get_height(node.right_child)
        elif not node.left_child and node.right_child:
            return - self.get_height(node)
        elif node.left_child and not node.right_child:
            return self.get_height(node)

        return 0

    def rotate_left(self, node: Node):
        y = node.right_child
        parent = node.parent

        if y:
            b_node = y.left_child

            a = node.left_children_amount
            b = y.left_children_amount

            if parent:
                if node.value > parent.value:
                    parent.right_child = y
                else:
                    parent.left_child = y

            node.parent = y
            node.right_child = b_node
            node.right_children_amount = b

            y.parent = parent
            y.left_child = node
            y.left_children_amount = a + b + 1

            if b_node:
                b_node.parent = node

            if not parent:
                self.root = y
        else:
            if parent:
                a_node = node.left_child
                a = node.left_children_amount

                grand_parent = parent.parent

                if grand_parent:
                    if parent.value > grand_parent.value:
                        grand_parent.right_child = node
                    else:
                        grand_parent.left_child = node

                parent.parent = node
                parent.right_child = a_node
                parent.right_children_amount = a

                node.parent = grand_parent
                node.left_child = parent
                node.left_children_amount = a + parent.left_children_amount + 1

                a_node.parent = parent

                if not grand_parent:
                    self.root = node

    def rotate_right(self, node: Node):
        x = node.left_child
        parent = node.parent

        if x:
            b_node = x.right_child

            c = node.right_children_amount
            b = x.right_children_amount

            if parent:
                if node.value > parent.value:
                    parent.right_child = x
                else:
                    parent.left_child = x

            node.parent = x
            node.left_child = b_node
            node.left_children_amount = b

            x.parent = parent
            x.right_child = node
            x.right_children_amount = b + c + 1

            if b_node:
                b_node.parent = node

            if not parent:
                self.root = x
        else:
            if parent:
                c_node = node.right_child
                c = node.right_children_amount

                grand_parent = parent.parent

                if grand_parent:
                    if parent.value > grand_parent.value:
                        grand_parent.right_child = node
                    else:
                        grand_parent.left_child = node

                parent.parent = node
                parent.left_child = c_node
                parent.left_children_amount = c

                node.parent = grand_parent
                node.right_child = parent
                node.right_children_amount = c + parent.right_children_amount + 1

                c_node.parent = parent

                if not grand_parent:
                    self.root = node

    def balance(self, node: Node):
        min_half_k = ceil((node.left_children_amount + node.right_children_amount + 1) / 2)

        min_half_k_node = self.k_min_node(min_half_k, node)
        height_to_min_half_k = self.__height_from_node_to_node(node, min_half_k_node)

        for i in range(height_to_min_half_k):
            if min_half_k_node.value <= min_half_k_node.parent.value:
                self.rotate_right(min_half_k_node.parent)
            else:
                self.rotate_left(min_half_k_node.parent)

        if min_half_k_node.left_child and min_half_k_node.right_child:
            self.balance(min_half_k_node.left_child)
            self.balance(min_half_k_node.right_child)

    def is_balanced(self, node: Node):
        if node.left_child and node.right_child:
            if abs(self.get_balance_factor(node)) < 2:
                return self.is_balanced(node.left_child) and self.is_balanced(node.right_child)

            return False

        elif not node.left_child and node.right_child:
            return self.get_balance_factor(node) == -1

        elif node.left_child and not node.right_child:
            return self.get_balance_factor(node) == 1

        return True

    def print_node(self, value):
        current_node = self.root

        while not current_node.value == value:
            if value <= current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

        print(current_node)

    def __print_tree_starting_from_node(self, node: Node):
        print(node)

        if node.left_child:
            self.__print_tree_starting_from_node(node.left_child)

        if node.right_child:
            self.__print_tree_starting_from_node(node.right_child)

    def print_tree(self):
        self.__print_tree_starting_from_node(self.root)
