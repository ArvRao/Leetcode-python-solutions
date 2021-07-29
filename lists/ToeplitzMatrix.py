Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example:
  
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.



class Solution:
        '''
        [1,2,3, ]
        [ ,1,2,3]
        
        [5,1,2, ]
        [ ,5,1,2]
        
        '''
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for m in range(len(matrix)-1):
            if matrix[m][:-1] != matrix[m+1][1:] :
                return False
            
        return True
