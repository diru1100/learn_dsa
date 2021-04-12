class Solution:
    # takes n time and primes_till_n space
    def enumeratePrimes(self, N):

        primes_till_n = []

        for i in range(2, N):
            flag = 0
            for prime in primes_till_n:
                if i % prime == 0:
                    flag = 1
                    break

            if flag == 0:
                primes_till_n.append(i)

        return primes_till_n


s = Solution()
print(s.enumeratePrimes(270))