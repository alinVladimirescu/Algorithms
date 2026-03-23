class Symbol_Matrix:
    def __init__(self, matrix):
        self.dict = {}
        self.rows, self.columns = len(matrix), len(matrix[0])
        for row in range(self.rows):
            for col in range(self.columns):
                if matrix[row][col] != 0:
                    self.add_element(row, col, matrix[row][col])
    
    def add_element(self, x, y, value):
        if value > 0: 
            if x not in self.dict:
                self.dict[x] = {}
            self.dict[x][y] = value
    
    def __str__(self):
        lines = []
        for row in range(self.rows):
            current_row = []
            for col in range(self.columns):
                if row in self.dict and col in self.dict[row]:
                    current_row.append(str(self.dict[row][col]))
                else:
                    current_row.append("0")
            lines.append(" ".join(current_row))
            
        return "\n".join(lines) 

    @staticmethod
    def sum_matrix(matrix1, matrix2):
        if matrix1.rows != matrix2.rows or matrix1.columns != matrix2.columns:
            print("Matrices need to have equal dimensions to add")
            return None
        
        empty_base = [[0 for _ in range(matrix1.columns)] for _ in range(matrix1.rows)]
        s_matrix = Symbol_Matrix(empty_base)
        
        for row, cols in matrix1.dict.items():
            for col, val in cols.items():
                s_matrix.add_element(row, col, val)
                
        for row, cols in matrix2.dict.items():
            for col, val in cols.items():
                # If the slot already has a value from matrix1, add them
                if row in s_matrix.dict and col in s_matrix.dict[row]:
                    s_matrix.dict[row][col] += val
                else:
                    s_matrix.add_element(row, col, val)
                    
        return s_matrix
            
                    
                    
        
                
    @staticmethod
    def multiply_matrix(matrix1, matrix2):
        if matrix1.columns != matrix2.rows:
            return None
        empty_base = [[0 for _ in range(matrix2.columns)] for _ in range(matrix1.rows)]
        m_matrix = Symbol_Matrix(empty_base)
        for row, row_val in matrix1.dict.items():
            for col, value in row_val.items():
                if col in matrix2.dict:
                    for j, col_val in matrix2.dict[col].items():
                        product = value * col_val
                        if row in m_matrix.dict and j in m_matrix.dict[row]:
                            m_matrix.dict[row][j] += product
                        else:
                            m_matrix.add_element(row, j, product)
                    
        return m_matrix 


def test_symbol_matrix():
    print("Running tests...")

    m1_list = [
        [0, 5, 0],
        [0, 0, 0],
        [3, 0, 1]
    ]
    m1 = Symbol_Matrix(m1_list)
    
    assert m1.rows == 3
    assert m1.columns == 3
    
    assert m1.dict == {0: {1: 5}, 2: {0: 3, 2: 1}}

    expected_str = "0 5 0\n0 0 0\n3 0 1"
    assert str(m1) == expected_str

    m2_list = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 4]
    ]
    m2 = Symbol_Matrix(m2_list)
    
    m3 = Symbol_Matrix.sum_matrix(m1, m2)
    
    expected_sum_dict = {
        0: {1: 5, 0: 1}, 
        1: {1: 2}, 
        2: {0: 3, 2: 5}     }
    assert m3.dict == expected_sum_dict
    
    expected_sum_str = "1 5 0\n0 2 0\n3 0 5"
    assert str(m3) == expected_sum_str

    m4_list = [[1, 2], [3, 4]]
    m4 = Symbol_Matrix(m4_list)
    
    m_invalid = Symbol_Matrix.sum_matrix(m1, m4)
    assert m_invalid is None
    print("\n--- Testing Matrix Multiplication ---")
    
    m_a_list = [
        [1, 0, 2],
        [0, 3, 0]
    ]
    m_a = Symbol_Matrix(m_a_list)
    print("Matrix A:")
    print(m_a)
    
    m_b_list = [
        [0, 4],
        [5, 0],
        [0, 6]
    ]
    m_b = Symbol_Matrix(m_b_list)
    print("\nMatrix B:")
    print(m_b)
    
    m_mult = Symbol_Matrix.multiply_matrix(m_a, m_b)
    print("\nResult of A * B:")
    print(m_mult)
    
    assert m_mult.dict == {0: {1: 16}, 1: {0: 15}}
    
    assert m_invalid is None
    
    print("\nAll multiplication tests passed successfully!")

    print("All tests passed successfully!")

if __name__ == "__main__":
    test_symbol_matrix()

 
