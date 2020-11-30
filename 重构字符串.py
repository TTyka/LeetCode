class Solution:
    def reorganizeString(self, S: str) -> str:
        length=len(S)
        if length < 2:
            return S
        result = ''
        dict_ch = dict()
        for ch in S:
            dict_ch[ch]=dict_ch.get(ch,0)+1
            if dict_ch[ch] >= 1+ (length+1)//2:
                return result
        # 确定可以排布之后在进行排布以排两个数为一步，每步排剩余数最大的两个数
        items = list(map(list,dict_ch.items()))
        items.sort(key=lambda x:x[1],reverse=True)
        result += items[0][0]
        items[0][1] -= 1
        for i in range(1, len(S)):
            items.sort(key=lambda x:x[1],reverse=True)
            if items[0][0]!=result[-1]:
                result += items[0][0]
                items[0][1] -= 1
                if items[0][1] == 0:
                    del items[0]
            else:
                result += items[1][0]
                items[1][1] -= 1
                if items[1][1] == 0:
                    del items[1]
            print(result)
        return result
        
################使用count函数############################
#         d3=dict()
# 　　    for x in s:
#     　　    d3[x]=s.count(x)