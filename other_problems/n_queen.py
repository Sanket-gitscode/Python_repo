class Solution:
    def solveNQueens(self, n: int):
        result = []
        
        board = [["."] * n for _ in range(n)]

        col = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):

            if row == n:
                result.append(["".join(r) for r in board])
                return 

            for cols in range(n):

                if cols in col or row - cols in diag1 or row + cols in diag2:
                   continue

                board[row][cols] = 'Q'
                col.add(cols)
                diag1.add(row - cols)
                diag2.add(row + cols)

                backtrack(row + 1)

                board[row][cols] = '.'
                col.remove(cols)
                diag1.remove(row - cols)
                diag2.remove(row + cols)

        backtrack(0)

        return result 


sol = Solution()
print(sol.solveNQueens(4))

