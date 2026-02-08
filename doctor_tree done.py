class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side):
        parent_node = self._find_node(self.root, parent_name)
        if parent_node is None:
            print(f"Parent doctor '{parent_name}' not found.")
            return
        new_node = DoctorNode(doctor_name)
        if side == 'left':
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                print(f"Left child of '{parent_name}' already exists.")
        elif side == 'right':
            if parent_node.right is None:
                parent_node.right = new_node
            else:
                print(f"side must be 'left' or 'right'.")

    def _find_node(self, current_node, name):
        if current_node is None:
            return None
        if current_node.name == name:
            return current_node
        left_result = self._find_node(current_node.left, name)
        if left_result is not None:
            return left_result
        return self._find_node(current_node.right, name)
    
    def preorder(self, node):
        if node is not None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)
    
    def inorder(self, node):
        if node is not None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)
    
    def postorder(self, node):
        if node is not None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]




# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))