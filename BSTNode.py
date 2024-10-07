class User:
    def __init__(self, username,name,email) -> None:
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self) -> str:
        return "User(username='{}', name='{}', email='{}')".format(self.username,self.name,self.email)
    
    def __str__(self) -> str:
        return self.__repr__()

class UserDatabase:
    def __init__(self) -> None:
        self.users = []

    def insert(self,user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i,user)
    
    def find(self,username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self,user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users
        

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

class BSTNode():
    def __init__(self, key, value = None) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def display_keys(self,space='\t',level = 0):
        if self is None:
            print(space*level + '∅')
            return
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return
        BSTNode.display_keys(self.right,space,level+1)
        print(space*level + str(self.key))
        BSTNode.display_keys(self.left,space, level+1) 

    def insert(node,key,value):
        if node is None:
            node = BSTNode(key,value)
        elif key < node.key:
            node.left = BSTNode.insert(node.left,key,value)
            node.left.parent = node
        elif key > node.key:
            node.right = BSTNode.insert(node.right,key,value)
            node.right.parent = node
        return node 
    
    def find(node,key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return BSTNode.find(node.left, key)
        if key > node.key:
            return BSTNode.find(node.right, key)
        
    def update(node,key,value):
        target = BSTNode.find(node, key)
        if target is not None:
            target.value = value

    def list_all(node):
        if node is None:
            return []
        
        return BSTNode.list_all(node.left) + [(node.key, node.value)] + BSTNode.list_all(node.right)
    
    def is_balanced(node):
        if node is None:
            return True,0
        balanced_l, height_l = BSTNode.is_balanced(node.left)
        balanced_r, height_r = BSTNode.is_balanced(node.right)
        balanced = balanced_l and balanced_r and abs(height_l-height_r) <=1
        height = 1 + max(height_l, height_r)
        return balanced,height

#level 0
tree = BSTNode.insert(None,jadhesh.username,jadhesh)
BSTNode.insert(tree,biraj.username,biraj)
BSTNode.insert(tree, sonaksh.username, sonaksh)
BSTNode.insert(tree, aakash.username, aakash)
BSTNode.insert(tree, hemanth.username, hemanth)
BSTNode.insert(tree, siddhant.username, siddhant)
BSTNode.insert(tree, vishal.username, siddhant)

BSTNode.update(tree,'hemanth', User('hemanth', 'Hemanth JJ', 'hemanth@example.com'))
tree2 = BSTNode.find(tree,'hemanth')
# tree.display_keys()


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data)-1
    if lo>hi:
        return None
    
    mid = (lo+hi)//2
    key, value = data[mid] 
    root = BSTNode(key,value)
    root.parent = parent
    root.left = make_balanced_bst(data,lo,mid-1,root)
    root.right = make_balanced_bst(data,mid+1,hi,root)

    return root

data = [(user.username, user) for user in users]
tree3 = make_balanced_bst(data)

def balance_bst(node):
    return make_balanced_bst(BSTNode.list_all(node))

tree1 = None

for user in users:
    tree1 = BSTNode.insert(tree1, user.username, user)

tree2 = balance_bst(tree1)
# BSTNode.display_keys(tree2)

class TreeMap():
    def __init__(self):
        self.root = None
        
    def __setitem__(self, key, value):
        node = BSTNode.find(self.root, key)
        if not node:
            self.root = BSTNode.insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            BSTNode.update(self.root, key, value)
            
        
    def __getitem__(self, key):
        node = BSTNode.find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in BSTNode.list_all(self.root))
    
    def __len__(self):
        return BSTNode.tree_size(self.root)
    
    def display(self):
        return BSTNode.display_keys(self.root)
    
    
treemap = TreeMap()
treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh
treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal

for key, value in treemap:
    print(key, value)