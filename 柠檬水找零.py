class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if len(bills) is 0:
            return True
        if bills[0] != 5:
            return False
        nums_5 = 1
        nums_10 = 0
        for i in range(1,len(bills)):
            if bills[i] is 5:
                nums_5+=1
            elif bills[i] is 10:
                if nums_5 < 0: return False
                nums_5-=1
                nums_10+=1
            elif nums_10>0:  # 当给20时，有10元先找10元
                nums_10 -= 1
                nums_5 -= 1
                if nums_5 < 0: return False
            else:  # 没有10元就找三个5元
                nums_5 -= 3
                if nums_5 < 0:
                    return False
        return True