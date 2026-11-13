# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Map values to their indices in the inorder traversal for $O(1)$ lookups
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        preorder_idx = 0
        
        def helper(left: int, right: int) -> TreeNode | None:
            nonlocal preorder_idx
            
            if left > right:
                return None
                
            root_val = preorder[preorder_idx]
            preorder_idx += 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]
            
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root

        return helper(0, len(inorder) - 1)