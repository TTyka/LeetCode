class Solution:
    ##########################方法一########空间占用13M左右速度6600ms
    # def countPrimes(self, n: int) -> int:
    #     count = 0
    #     if n <3:
    #         return 0
    #     count += 1
    #     def check_prime(n):
    #         n_a = int(n**0.5)
    #         if n%2==0:
    #             return 0
    #         for i in range(3,n_a +1,2):
    #             if n%i ==0:
    #                 return 0
    #         return 1
    #     for i in range(3,n,2):
    #         count += check_prime(i)
    #     return count
    #     count=[]
##########################方法二########空间占用23M左右速度500ms
    # def countPrimes(self, n: int) -> int:
    #     if n <3:
    #         return 0
    #     primes = [1]*(n//2)
    #     stack = []
    #     for i in range(3 ,n ,2):
    #         if primes[i>>1]:
    #             stack.append(i)
    #         for pr in stack:
    #             B = pr*i
    #             if B >= n:
    #                 break
    #             # print((pr*i)>>1,i,pr)
    #             primes[B>>1] = 0
    #     return len(stack)+1
    
##########################方法三########空间占用36M左右速度110ms
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0   # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号n的所有质数的倍数剔除
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1) # 比如i=3，把3*（3+1）的数都变成0，列表中isPrime[i * i:n:i]的个数就是((n - 1 - i * i) // i + 1)
        return sum(isPrime) # 求没有变成0的数的总和，即数量
