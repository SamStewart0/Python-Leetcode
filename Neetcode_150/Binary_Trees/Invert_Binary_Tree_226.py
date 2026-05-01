from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''
        To invert each tree, each leaf node has its left and right pointers changed

        1. start at the root and add to the queue
        2. pop off the queue and invert this nodes pointers
        3. if left or right node are not none add to the queue to be processed 
        4. return the root when the queue is empty
        '''

        if not root:

            return None

        queue = deque([root])

        while queue:

            current = queue.popleft()

            current.right, current.left = current.left, current.right

            if current.right:

                queue.append(current.right)

            if current.left:

                queue.append(current.left)

        return root 
