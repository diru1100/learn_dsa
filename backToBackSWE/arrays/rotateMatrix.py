class Solution:
    def rotate(self, matrix):
        """
        :type matrix: list of list of int
        :rtype: list of list of int
        """
        # n^2 time and n^2 space solution
        size = len(matrix)
        rotated_matrix = []
        for i in range(0, size):
            temp_row = [matrix[j][i] for j in range(0, len(matrix))]
            rotated_matrix.append(temp_row[::-1])
        return rotated_matrix


s = Solution()
print(s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))