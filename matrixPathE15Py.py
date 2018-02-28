class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

print(" For a 20x20 grid")
Matrix = [[0 for x in range(21)] for y in range(21)]
print("0 matrix created: ",Matrix)
val = 1 
for i in range(21):
    for j in range(21):
        Matrix[i][j] = val
        val += 1
print("Populaed matrix: ",Matrix)
totalnum =0
def populateMat(i,j,matrix):
        global totalnum
        if i > 20 or j > 20:
            return None
        #print(i,j)
        node = Tree()
        node.data = matrix[i][j]
        print(node.data)
        if node.data == 441:
            totalnum += 1
            print("=====")
        node.left = populateMat(i+1,j,matrix)
        node.right = populateMat(i,j+1,matrix)
        return node
root = populateMat(0,0,Matrix)
print(totalnum)
#this brute force method hardly works for large numbers as it is time consuming. 
# However, from (1,1) to (i,j) you make i-1 down steps and j-1 right steps, so binomial(i-1+j-1, i-1)
#In the PE problem example, 4 steps total with 2 down and 2 right, so binomial(4,2)=6
#40C20