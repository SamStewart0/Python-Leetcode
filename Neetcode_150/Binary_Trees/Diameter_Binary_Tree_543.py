class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        find max length of left and right side seperately
        add together
        '''

        if not root: return 0
        
        max_diameter = 0
        
        def get_height(node):
            
            #allows us to update max_diameter outside of the function

            nonlocal max_diameter

            #when we hit None return 0 to start the count

            if node is None: return 0

            #traverse leftmost side until we hit None

            left_h = get_height(node.left)
            
            #traverse rightmost side until we hit None

            right_h = get_height(node.right)

            #update max_diameter with current path length

            max_diameter = max(max_diameter, left_h + right_h)

            #return the current longest path count to the parent node
            
            return max(left_h, right_h) + 1

        get_height(root)

        return max_diameter
