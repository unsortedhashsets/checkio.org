def checkio(matrix):
    A = matrix
    for i in range(len(A)): 
        for j in range(len(A[0])-3):
            if A[i][j] == A[i][j+1]== A[i][j+2]== A[i][j+3]:
                return True
    for j in range(len(A[0])):
        for i in range(len(A)-3):
            if A[i][j] == A[i+1][j]== A[i+2][j]== A[i+3][j]:
                return True
    for j in range(len(A[0])-3):
        for i in (range(len(A)-3)):
            if A[i][j] == A[i+1][j+1] == A[i+2][j+2] == A[i+3][j+3]:
                return True
    for j in reversed(range(len(A[0]))):
        for i in (range(len(A)-3)):
            if (j-3)<0:
                return False
            if A[i][j] == A[i+1][j-1]== A[i+2][j-2]== A[i+3][j-3]:
                return True   

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
