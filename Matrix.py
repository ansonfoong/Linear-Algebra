class Matrix:
    def __init__(self, *args):
        if self.valid_matrix([*args]):
            self.matrix = [*args]
        else:
            raise Exception("Invalid Matrix. All rows must have the same amount of columns")
    
    def valid_matrix(self, matrix):
        if len(matrix) == 0:
            return True
        elif len(matrix) == 1:
            return True
        else:
            row = matrix[0]
            return self.validate(matrix, len(row))

    def validate(self, check, length_of_row):

        if len(check) == 1:
            return len(check[0]) == length_of_row

        curr_row = check.pop(0)
        if len(curr_row) != length_of_row:
            return False
        else:
            return self.validate(check, length_of_row)

def transpose(matrix):
    def initialize(rows, columns):
        matrix = []
        for x in range(rows):
            matrix.append([])
            for y in range(columns):
                matrix[x].insert(y, 0)
        
        return matrix

    def _transpose(initial_matrix, result):
        rows=len(result)
        cols=len(result[0])
        for i in range(rows):
            for j in range(cols):
                result[i][j] = initial_matrix[j][i]

        return result
    init_matrix = initialize(len(matrix[0]),len(matrix))
    return _transpose(matrix, init_matrix)