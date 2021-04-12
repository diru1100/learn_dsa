class Solution:
    def bruteSol(self, A):
        # n^3 time_complecity + sorting n^logn
        size = len(A)
        triplets_zero_sum = []
        for i in range(0, size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    if A[i] + A[j] + A[k] == 0:
                        temp = [A[i], A[j], A[k]]
                        temp.sort()
                        triplets_zero_sum.append(temp)
        return triplets_zero_sum

    def bttrSol(self, A):
        # sort n^logn and 3 pointer approach n^2 ig in worst case
        size = len(A)
        triplets_zero_sum = []
        A.sort()

        p1 = 0

        while 1:

            p2 = p1 + 1
            p3 = size - 1

            while p2 < p3:
                temp_sum = A[p1] + A[p2] + A[p3]
                # print(temp_sum)
                if temp_sum == 0:
                    triplets_zero_sum.append([A[p1], A[p2], A[p3]])
                    p2 = p2 + 1
                    p3 = p3 - 1

                elif temp_sum > 0:
                    p3 = p3 - 1

                else:
                    p2 = p2 + 1

            p1 = p1 + 1
            # print(p1)
            if p1 >= (size - 2):
                #    print(triplets_zero_sum)
                break

        return triplets_zero_sum

    def threeSum(self, A):
        """
        :type A: list of int
        :rtype: list of list of int
        """

        return self.bttrSol(A)


s = Solution()
print(s.threeSum([-2, 0, 1, -1, 7, -10, 3, 2]))