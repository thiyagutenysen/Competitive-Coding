# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        from collections import defaultdict
        if n%2==0:
            return []
        answers = defaultdict(list)
        answers[1].append(TreeNode())
        if n==1:
            return answers[n]
        for i in range(3, n+1, 2):
            possible = []
            for j in range(1, i, 2):
                k = i-j-1
                for p in answers[j]:
                    for q in answers[k]:   
                        root = TreeNode()
                        root.left = p
                        root.right = q
                        possible.append(root)
            answers[i]+=possible
        return answers[n]