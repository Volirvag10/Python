class Matrix:
    
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''
        
    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)


m = Matrix([[0, 1, 1], [0, -1, 1], [-1, 1, -1], [0, 1, -1]])
new_m = Matrix([[-3, 0, 7], [-5, 1, 6], [0, 4, -5], [0, 8, -5]])
print(m.__add__(new_m))