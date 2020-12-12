n=int(input("Enter no of rows of the square matrix: "))
matrix=[[int(input("Enter element "+str(j+1)+","+str(i+1)+" of the matrix: ")) for i in range(n)] for j in range(n)]

def gen_id_mat(n):
    l=[[0 for i in range(n)] for j in range(n)]
    for k in range(n):
        l[k][k]=1
    return l

def gen_id_mat1(n):
    l=[[0.0 for i in range(n)] for j in range(n)]
    for k in range(n):
        l[k][k]=1.0
    return l

def row_swap(m,r1,r2):
    
    m[r1],m[r2]=m[r2],m[r1]
    return m

def row_op_1(m,r1,r2,c):
    
    for  i in range(len(m)):
        m[r1][i]=(m[r2][i])*c
    return m

def row_op_2(m,r1,r2,c):
    
    for  i in range(len(m)):
        m[r1][i]=m[r1][i]-(c*m[r2][i])
    return m

def disp(m):
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) for row in m]))
    print()
   
idm = gen_id_mat(n)
id_inv = gen_id_mat(n)

count=0
for col in range(n):
    for row in range(n):
        if idm[row][col]==1 and matrix[row][col]==0:
                for g in range(n):
                    if matrix[g][col]!=0:
                        matrix=row_swap(matrix,row,g)
                        print()
                        disp(matrix)
                        print("    ","R"+str(row+1)+" <--> "+"R"+str(g+1))
                        print()
        if matrix[row][col]!=0 and idm[row][col]==1:
            multp=1/matrix[row][col]
            id_inv=row_op_1(id_inv,row,row,(1/matrix[row][col]))
            matrix=row_op_1(matrix,row,row,(1/matrix[row][col]))
            print()
            count+=1
            print("Step "+str(count)+":")
            print()
            disp(matrix)
            disp(id_inv)
            print("    ","R"+str(row+1)+" --> "+"R"+str(row+1)+" x "+str(multp))
            print()
            
            for const in range(n):
                if const==row:
                    continue
                multp=matrix[const][col]
                id_inv=row_op_2(id_inv,const,row,matrix[const][col])
                matrix =row_op_2(matrix,const,row,matrix[const][col])
                
                count+=1
                print("Step "+str(count)+":")
                print()
                disp(matrix)
                disp(id_inv)
                print("    ","R"+str(row+1)+" --> "+"R"+str(row+1)+" - "+str(multp)+ " x "+"R"+str(const+1))
                print()

if matrix==gen_id_mat1(n):
    print("The inverse of the given matrix is:")
    print()
    disp(id_inv)
else:
    print("This matrix is not invertible...")
        

                







    


            



