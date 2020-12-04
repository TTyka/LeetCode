class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        def update(end_list,num,m):
            if end_list.get(num,0):
                end_list[num].append(m)
            else:
                end_list[num]=[m]
            return end_list
        end_list = dict()  # 用于存放所有子序列中结尾的字符的序列长度
        sub_list = dict() # 用于存放每个字符结尾的子序列个数
        if len(nums)<3:
            return False
        for i in range(0, len(nums)):
            # 判断是否存以上一个字符结尾的字符
            if sub_list.get(nums[i]-1,0):
                m = min(end_list[nums[i]-1])   
                if sub_list[nums[i]-1]==1:   # 如果只存在一个,以num[i-1]字符结尾的子序列
                    # end_list = end_list.get(nums[i],[]).append(m+1) 
                    del end_list[nums[i]-1]  # 删除以上一个字符结尾的子序列的长度
                else:
                    end_list[nums[i]-1].remove(m)
                end_list = update(end_list,nums[i],m+1) # 新建一个以当前字符结尾的序列长度 
                sub_list[nums[i]-1] -= 1    # 以num[i]-1结尾的子序列个数减1
                sub_list[nums[i]] = 1+sub_list.get(nums[i],0) # 以num[i]结尾的子序列个数加1
            else:
                end_list = update(end_list,nums[i],1)
                sub_list[nums[i]]= 1+sub_list.get(nums[i],0)
        # print(list(end_list.items()))
        check_list =[min(q[1]) for q in list(end_list.items())]
        if min(check_list)<3:
            return False
        return True
            
#################以下为官方代码#############################

    # def isPossible(self, nums: List[int]) -> bool:
    #     mp = collections.defaultdict(list)
    #     print(mp.get(nums[1]))
    #     for x in nums:
    #         if queue := mp.get(x - 1):
    #             prevLength = heapq.heappop(queue)
    #             heapq.heappush(mp[x], prevLength + 1)
    #         else:
    #             heapq.heappush(mp[x], 1)
        
    #     return not any(queue and queue[0] < 3 for queue in mp.values())
