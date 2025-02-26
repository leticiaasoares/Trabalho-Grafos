# GRUPO 10
#
# Nomes: Caio Cezar Miranda Carvalho
#        Letícia de Oliveira Soares
#        Matheus Monteiro Huebra Perdigão


def builds_post_order(pre_order, in_order):
    
    if pre_order == '':
        return ''
    
    root = pre_order[0]
    root_index_inorder = in_order.index(root)

    left_subtree_inorder = in_order[0:root_index_inorder]
    right_subtree_inorder = in_order[root_index_inorder+1:]
    left_subtree_preorder = pre_order[1:len(left_subtree_inorder)+1]
    right_subtree_preorder = pre_order[len(left_subtree_inorder)+1:]

    left_subtree_postoreder = builds_post_order(left_subtree_preorder, left_subtree_inorder)
    right_subtree_postorder = builds_post_order(right_subtree_preorder, right_subtree_inorder)

    return left_subtree_postoreder + right_subtree_postorder + root



test_cases = int(input())
while(test_cases > 0):
    tree_info = input().split()

    qnt_nodes = int(tree_info[0])
    pre_order = tree_info[1]
    in_order = tree_info[2]

    post_order = builds_post_order(pre_order=pre_order, in_order=in_order)
    print(post_order)

    test_cases -= 1