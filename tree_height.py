# 221RDB386 Mārtiņš Nikiforovs 11.grupa
import sys
import threading
import numpy

def compute_height(n, parentsList):
    # Write this function
    nodeChildren = [[] for _ in range(n)]
    for i in range(n):
      childParent = parentsList[i]
      if childParent == -1:
        treeRoot = i
      else:
        nodeChildren[childParent].append(i)


  
    def compute_depth(node):
      if not nodeChildren[node]:
        return 1
      max_depth = 0
      
      for child in nodeChildren[node]:
        depth = compute_depth(child)
        max_depth = max(max_depth, depth)
      return max_depth + 1
    return compute_depth(treeRoot)



def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    #pass
  
  keyInp = input()
  if 'I' in keyInp:
      n2 = int(input())
      parentsList2 = list(map(int, input().split()))
      heightI = compute_height(n2, parentsList2)
      print(heightI)
  elif 'F' in keyInp:
    filename = input()
    if "a" not in filename:
        with open("test/" + filename,'r') as f:
            n3 = int(f.readline())
            parentsList3 = list(map(int, f.readline().split()))
            heightF = compute_height(n3, parentsList3)
            print(heightF)
  else:
    print("error")
    exit()

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
