class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

t1=TreeNode('drinks')
t2=TreeNode('hot')
t3=TreeNode('cold')
t4=TreeNode('tea')
t1.left=t2
t1.right=t3
t5=TreeNode('coffee')
t2.left=t4
t2.right=t5
t6=TreeNode('coke')
t7=TreeNode('lassi')
t3.left=t6
t3.right=t7




def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root):
    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)


def bfs(root):
    if not root:
        return 
    q=[root]

    while q:
        n=q.pop(0)

        print(n.val,end=' ')

        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)


def insert(root,val):
    newNode=TreeNode(val)

    if not root:
        root=newNode
    else:
        q=[root]

        while q:
            n=q.pop(0)

            if n.left:
                q.append(n.left)
            else:
                n.left=newNode
                return 'insertion done'
            
            if n.right:
                q.append(n.right)
            else:
                n.right=newNode
                return 'insertion done'
            

def deepestNode(root):
    if not root:
        return 
    q=[root]

    while q:
        n=q.pop(0)

        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return n.val

def deldeepestNode(root,value):
    if not root:
        return
    q=[root]

    while q:
        n=q.pop(0)
        if n.val==value:
            n.val=None
            return

        if n.left:
            if n.left.val==value:
                n.left=None
                return
            else:
                q.append(n.left)
        
        if n.right:
            if n.right.val==value:
                n.right=None
                return
            else:
                q.append(n.right)

def deleteBinaryTree(root,value):
    if not root:
        return 'Not PResent'
    q=[root]

    while q:
        n=q.pop(0)
        if n.val==value:
            dep=deepestNode(root)
            deldeepestNode(root,dep)
            n.val=dep
            return 'Node deleted'
        
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    
    return 'Failed to Delelte'


    



print(insert(t1,'mangoshake'))
print(insert(t1,'black_coffee'))
bfs(t1)
print('\n')
print(deleteBinaryTree(t1,'mangoshake'))

bfs(t1)

