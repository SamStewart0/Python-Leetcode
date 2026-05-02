# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        use queue to track nodes, keep track of the length of each level at each stage

        once we finish a level we increment the count
        '''

        if not root: return 0

        depth = 0

        queue = deque([root])

        while queue:

            #get the length of the current level

            current_level_len = len(queue)

            for _ in range (current_level_len):

                #append the next level to the queue

                current = queue.popleft()

                if current.left:

                    queue.append(current.left)

                if current.right:

                    queue.append(current.right)
            
            #increment depth count

            depth += 1

        return depth
