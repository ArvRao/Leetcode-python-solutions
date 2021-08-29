def diagonalSum(self, mat: List[List[int]]) -> int:
    diagonal_sum = 0
    length = len(mat)
    for i in range(length):     # i and j are rows and columns respectively
        for j in range(len(mat[i])):
            if i==j:
                diagonal_sum += mat[i][j]
            elif i == length-j-1:
                diagonal_sum += mat[i][j]
            
    return diagonal_sum
  
# In this logic, every primary diagonal has same i and j value, for secondary diagonal, value of i is length of row - specific column -1.
