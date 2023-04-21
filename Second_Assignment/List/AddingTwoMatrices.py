#Write a program which asks for order of two matrices and read two matrices as given order.
#  Add two input arrays and display the resultant matrix
def two_matrices():

    row = int(input("Enter the order of row:"))
    column = int(input("Enter the order of the column: "))

    matrices1 = []
    matrices2 = []
    matric = []

    for i in range(row):
        rows = []
        for j in range(column):

            matrixx = int(input())
            rows.append(matrixx)
    matrices1 = row
    return matrices1    
        

    
result = two_matrices()
print(f"The matrix is {result}")
