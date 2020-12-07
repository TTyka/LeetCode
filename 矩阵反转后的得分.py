class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        if !(len(A) or len(A[0])):
            return 0
        def change2to10(lista):
            result = 0
            for i in lista:
                result = result*2+i
            return result
        col_a = len(A[0])
        row_a = len(A)
        Result = [len(A)]
        # 先将所有行的首位变为1
        for i in range(row_a):
            if A[i][0] is 0:
                for j in range(col_a):
                    A[i][j] = 1-A[i][j]
        # 再保证除第一列的所有列1的数量要大于等于一半
        for i in range(1,col_a):
            sum_col = sum([ A[j][i] for j in range(row_a)])
            Result.append(max(sum_col,row_a -sum_col))
        return change2to10(Result)
