def conflict(state, nextX):    #記錄在state棋子已經放好的狀況下，後續的所有解答
    nextY = len(state)
    if any(abs(state[i] - nextX)== 0 for i in range(len(state))): #同行
        return True
    if any(abs(state[i] - nextX)== nextY - i for i in range(len(state))): #同對角線
        return True
    return 

def queens(n, state=()):  #將state的默認值設為空元組()  呼叫函數queens(4,())似乎有點麻煩，我們希望只要呼叫函數queens(4)
    if len(state) == n: 
        return [()]
    ans = []
    for pos in range(n):
        if not conflict(state, pos):
            ans += [(pos,)+ result for result in queens(n, state + (pos,))]
    return ans
s=int(input()) 
print(queens(8))  #print(queens(要放幾個queens))  (第1列的位子,第2列的位子........)