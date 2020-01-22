# Definition for a binary tree node.
class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class Solution:
    def printAll(self, node, output=[]):
        if node == None:
            return output

        output.append(node.val)

        if node.left != None:
            self.printAll(node.left, output)
        if node.right != None:
            self.printAll(node.right, output)

        return output

    def mapNodesInTree(self, root, dictData):
        if root == None:
            return None

        # Long version of return =)
        # greaterRoot = Node(dictData[root.val] + root.val)
        # greaterLeft = self.mapNodesInTree(root.left, dictData)
        # greaterRight = self.mapNodesInTree(root.right, dictData)

        # greaterRoot.left = greaterLeft
        # greaterRoot.right = greaterRight

        return Node(dictData[root.val] + root.val, self.mapNodesInTree(root.left, dictData), self.mapNodesInTree(root.right, dictData))

    def convertBST(self, root: Node) -> Node:
        # get all values
        allNodes = self.printAll(root, [])
        # sort and reverse
        allNodes.sort(reverse=True)
        # Dict for getting sum value, greater than current
        dictDataByValue = dict()

        sum = 0
        # Init
        for value in allNodes:
            dictDataByValue[value] = sum
            sum += value

        return self.mapNodesInTree(root, dictDataByValue)


tree0 = Node(5, Node(2),  Node(13))

my = Solution()
output2 = my.printAll(tree0, [])
print('output', output2)

greaterTree = my.convertBST(tree0)
outputGreat = my.printAll(greaterTree, [])
print('outputGreat', outputGreat)

# Don't know why, but it's too slow =(
# Runtime: 148 ms, faster than 5.10% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 17.1 MB, less than 6.25% of Python3 online submissions for Convert BST to Greater Tree.
