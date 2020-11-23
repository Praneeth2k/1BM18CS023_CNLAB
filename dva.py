
#Still writing

def start():
    dm[20][20] = {0}
    print("Enter the nubmer of nodes")
    no = input()
    print("Enter the distance matrix:")
    for i in range(no):
        for j in range(no):
            dm[i][j] = input()
            
