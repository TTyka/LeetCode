class Solution:
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     if n==0:
    #         return len(tasks)
    #     task_set = dict()
    #     for i in tasks:
    #         task_set[i]=1+task_set.get(i,0)           
    #     task_list = list(map(list,task_set.items()))   
    #     stack = [" "]*n
    #     len_a = 0
    #     m = []
    #     while len(task_list):
    #         cate = task_list.__len__()
    #         task_list.sort(key=lambda x:x[1],reverse=True)
    #         if stack.count(' ')< n-cate and n > cate:
    #             else:
    #                 stack.append(' ')
    #                 m.append(' ')
    #                 len_a += 1
    #                 del stack[0]
    #         else:
    #             k = 0
    #             for i in range(cate):
    #                 if task_list[i][0] not in stack:
    #                     len_a += 1
    #                     stack.append(task_list[i][0])
    #                     m.append(task_list[i][0])
    #                     del stack[0]
    #                     task_list[i][1] -= 1
    #                     if task_list[i][1] == 0:
    #                         task_list.remove(task_list[i])
    #                     break
    #                 else:
    #                     k += 1
    #             if k==cate:
    #                 stack.append(' ')
    #                 m.append(' ')
    #                 len_a += 1
    #                 del stack[0]
    #     print(m)
    #     return len_a                
    #     print(task_list)

##################官方解答###########################
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        # 最多的执行次数
        maxExec = max(freq.values())
        # 具有最多执行次数的任务数量
        maxCount = sum(1 for v in freq.values() if v == maxExec)
        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))