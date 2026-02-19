class Solution(object):
    def transpose(self, matrix):

        transposed = list(zip(*matrix))

        return transposed
