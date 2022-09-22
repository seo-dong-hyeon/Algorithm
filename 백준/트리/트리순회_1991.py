dict_node = {}
pre_list = []
in_list = []
post_list = []

N = int(input())
for i in range(N):
    p, l, r = input().split()
    dict_node[p] = [l, r]

def preorder(p):
    pre_list.append(p)
    if dict_node[p][0] != '.':
        preorder(dict_node[p][0])
    if dict_node[p][1] != '.':
        preorder(dict_node[p][1])

def inorder(p):
    if dict_node[p][0] != '.':
        inorder(dict_node[p][0])
    in_list.append(p)
    if dict_node[p][1] != '.':
        inorder(dict_node[p][1])

def postorder(p):
    postorder
    if dict_node[p][0] != '.':
        postorder(dict_node[p][0])
    if dict_node[p][1] != '.':
        postorder(dict_node[p][1])
    post_list.append(p)

preorder('A')
inorder('A')
postorder('A')

print("".join(pre_list))
print("".join(in_list))
print("".join(post_list))