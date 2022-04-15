import sys


class Node:
    def __init__(self, key, data):
    self.left = None
    self.right = None
    self.parent = None
    self.key = key
    self.data = data
    self.dataSum = data


def Insert(root, z):
    # Locate the parent of the node
    y = None
    x = root
    while x is not None:
    y = x
    if z.key < x.key:
    x = x.left
    else:
    x = x.right
    # Insert the node
    z.parent = y
    if z.key < y.key:
    y.left = z
    else:
    y.right = z
    # Update the sum
    while y is not None:
    y.dataSum += z.dataSum
    y = y.parent
# sums the values less than b


def sumLesser(x, b):
    val = 0
    v = x
    while v is not None:
    if v.key <= b:
    val += v.data
    if (v.left is not None):
    val += v.left.dataSum
    v = v.right
    else:
    v = v.left
    return val
# sums the values greater than a


def sumGreater(x, a):
    val = 0
    v = x
    while v is not None:
    if v.key >= a:
    val += v.data
    if (v.right is not None):
    val += v.right.dataSum
    v = v.left
    else:
    v = v.right
    return val
# Sums the y values in x key range


def sumYinRangeX(a, b, root):
    v = root
    sum = 0
    while (v is not None) and ((v.key < a) or (v.key > b)):
    if (v.key <= a):
    v = v.right
    elif (v.key >= b):
    v = v.left
    # print(v)
    if (v is not None):
    sum += v.data
    sum += sumLesser(v.right, b)
    sum += sumGreater(v.left, a)
    return sum


# Open files and initialize tree
dataJ = open(sys.argv[1], 'r')
rangeJ = open(sys.argv[2], 'r')
rootKV = dataJ.readline().split()
rootKey = int(rootKV[0])
rootData = int(rootKV[1])
root = Node(rootKey, rootData)
# Generate the tree
data = dataJ.readlines()
for i in data:
    tmp = i.split()
    k = int(tmp[0])
    v = int(tmp[1])
    z = Node(k, v)
    Insert(root, z)
# Get ranges and generate output
fList = []
range = rangeJ.readlines()
for i in range:
    tmp = i.split()
    a = int(tmp[0])
    b = int(tmp[1])
    sum = sumYinRangeX(a, b, root)
    tmptuple = (a, b, sum)
    fList.append(tmptuple)
# Open output.txt and write tuples line by line
f = open('output.txt', 'w')
for i in fList:
    f.write(f"{i[0]} {i[1]} {i[2]}\n")
# Make sure files are closed
dataJ.close()
rangeJ.close()
f.close()
