class Solution:
    """3<=len(A)<=100"""
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        c_default = 0
        for i in range(2,A.__len__()):
            if A[i]+A[i-1]>A[i-2]:
                c_default = sum(A[i-2:i+1])
                break
        return c_default
#################方法二改方法一尝试提速但速度更慢######################
        # A=sorted(A)
        # i = len(A)-3
        # while A[i]+A[i+1]<=A[i+2]:
        #     if i>0:
        #          i -= 1
        #     else:
        #         return 0
        # return A[i]+A[i+1]+A[i+2]
########################方法二####################
        # A=sorted(A)
        # c_default = 0
        # i = len(A)-3
        # while(i>=0):
        #     if A[i]+A[i+1]>A[i+2]:
        #         c_default = A[i]+A[i+1]+A[i+2]
        #         break
        #     i-=1
        # return c_default
###########################求三角形面积的最大面积###########################
        # 面积公式，返回所能构成的面积最大的三角形的面积
        # s_default = 0
        # for i in range(2,A.__len__()):
        #     p = (A[i]+A[i-1]+A[i-2])/2
        #     s = p*(p-A[i])*(p-A[i-1])*(p-A[i-2])
        #     if s>s_default:
        #         s_default=s
        # return s**0.5