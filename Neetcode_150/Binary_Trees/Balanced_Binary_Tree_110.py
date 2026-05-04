class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Depth of the subtrees of every node never differs by more than one

        find height of left and right subtree at each node
        '''

        def check(node):

            if not node: return 0

            #recursively check the left subtree
            left_height = check(node.left)
            if left_height == -1:
                return -1

            #then check right subtree
            right_height = check(node.right)
            if right_height == -1:
                return -1

            #if tree is unbalanced return -1
            if abs(left_height-right_height) > 1:
                return -1

            #otherwise return height to the parent
            return max(left_height, right_height) +1

        return check(root) != -1
