class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        num_R = deque()
        num_D = deque()
        len_th = len(senate)
        for i in range(len_th):
            if senate[i]=="R":
                num_R.append(i)
            else:
                num_D.append(i)
        # 只要有一方达到或超过另一方的两倍，那么无论怎么排都会是多的一方胜
        if len(num_D)>=2*len(num_R):
            return "Dire"
        elif 2*len(num_D)<=len(num_R):
            return "Radiant"
        # 其他情况下根据排列的顺序进行模拟直到有一方被完全剔除，用队列结构存每个D,R的相对位置，每次只删除离自己最近的下一个其他字符
        while len(num_D) and len(num_R):
            if num_R[0]<num_D[0]:
                num_R.popleft()
                num_R.append(len_th)
                num_D.popleft()
                len_th+=1
            else:
                num_D.popleft()
                num_D.append(len_th)
                len_th+=1
                num_R.popleft()
        return "Radiant" if len(num_R) else "Dire"