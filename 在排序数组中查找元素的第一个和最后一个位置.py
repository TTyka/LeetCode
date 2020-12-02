class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            return [nums.index(target),nums.count(target)+nums.index(target)-1]
        except:
            return [-1,-1]
# 下面是一位大佬使用二分查找的方法（虽然没我的快）
# class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     size = len(nums)
    #     if size == 0 : return [-1,-1]
    #     first_pos = self.findFirst(nums,target,size)
    #     last_pos = self.findLast(nums,target,size)
    #     if(first_pos == -1):
    #         return [-1,-1]
    #     else:
    #         return [first_pos,last_pos]
    # def findFirst(self, nums: List[int], target: int, size:int) -> int:
    #     left = 0
    #     right = size-1
    #     while left < right:
    #         mid = (left + right) //2
    #         if nums[mid] < target:
    #             left = mid+1
    #         elif nums[mid] == target:
    #             right = mid 
    #         else:
    #             right = mid -1
            
            
    #     if nums[right]==target:
    #        return right
    #     else:
    #         return -1
    # def findLast(self, nums: List[int], target: int, size:int) -> int:
    #     left = 0
    #     right = size-1
    #     while left < right:
    #         mid = (left + right+1) //2 #因为 left = mid，所以下取整要改为上取整。
    #         if nums[mid] > target:
    #             right = mid-1
    #         elif nums[mid]==target :
    #             left = mid
    #         else:
    #             left = mid +1
    #         #print(mid)
        
    #     return left
# 作者：heydom
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/34zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-de-di-9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。