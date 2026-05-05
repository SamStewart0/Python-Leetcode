class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        '''
        tree is equal if all node values, left and right pointers are also equal

        final return will T/F

        if both nodes are null we can return true, if one is null we can return false

        '''

        def check(node1, node2):

            #if both are null this is a match
            if not node1 and not node2:
                return True

            #if mismtach return false
            if (bool(node1) ^ bool(node2)): 
                return False

            #if mismtach return false
            if node1.val != node2.val: 
                return False

            #check left nodes
            check_left = check(node1.left, node2.left)
            if check_left == False:
                return False

            #check right nodes
            check_right = check(node1.right, node2.right)
            if check_right == False:
                return False

            #if we have made it to here its a match
            return True 

        return check(p,q)
