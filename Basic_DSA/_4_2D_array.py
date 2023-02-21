# 1 2 3
# 4 5 6
# 7 8 9

# storing data in row and column manner 

rows=int(input("Enter the number of rows : "))
cols=int(input("Enter the number of coloumns : "))

matrix = []
for i in range(rows): # 0
    row = []
    for j in range(cols): # 2
        elements = int(input("Enter element : "))
        row.append(elements)
    matrix.append(row)

print(matrix)

for i in matrix:
    print(i)

for i in range(rows): # 1
    for j in range(cols): # 1
        print(matrix[i][j],end=" ")
    print()        
       
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


