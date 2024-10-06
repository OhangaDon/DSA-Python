class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0 
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left)+TreeNode.size(self.right)
    
    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left)+self.key+TreeNode.traverse_in_order(self.right))
    
    def display_keys(self,space='\t',level = 0):
        if self is None:
            print(space*level + '∅')
            return
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return
        TreeNode.display_keys(self.right,space,level+1)
        print(space*level + str(self.key))
        TreeNode.display_keys(self.left,space, level+1) 

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self) -> str:
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self) -> str:
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data,tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node




tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = TreeNode.parse_tuple(tree_tuple)


def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and 
              (max_l is None or node.key > max_l) and 
              (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key
print(is_bst(tree))

# def parse_tuple(data):
#     if isinstance(data, tuple) and len(data) == 3:
#         node = TreeNode(data[1])
#         node.left = parse_tuple(data[0])
#         node.right = parse_tuple(data[2])
#     elif data is None:
#         node = None
#     else:
#         node = TreeNode(data)
    
#     return node

# tree2 = parse_tuple(tree_tuple)

# def display_keys(node, space='\t', level=0):
#     # print(node.key if node else None, level)
    
#     # If the node is empty
#     if node is None:
#         print(space*level + '∅')
#         return   
    
#     # If the node is a leaf 
#     if node.left is None and node.right is None:
#         print(space*level + str(node.key))
#         return
    
#     # If the node has children
#     display_keys(node.right, space, level+1)
#     print(space*level + str(node.key))
#     display_keys(node.left,space, level+1)  
# display_keys(tree2,' ')  

# def traverse_in_order(node):
#     if node is None:
#         return []
#     return(traverse_in_order(node.left)+[node.key]+traverse_in_order(node.right))

# def tree_height(node):
#     if node is None:
#         return 0
#     return 1 + max(tree_height(node.left), tree_height(node.right))

# def tree_size(node):
#     if node is None:
#         return 0
#     return 1 + tree_size(node.left) + tree_size(node.right)

# print(tree_size(tree2))