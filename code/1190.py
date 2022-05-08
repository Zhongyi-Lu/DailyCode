

"""
1190. Reverse Substrings Between Each Pair of Parentheses
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
Stack
"""
# Zhongyi Lu 2022-05-08


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for cha in s:
            if cha != ')':
                stack.append(cha)
            else:
                # cha == ')'
                temp = []
                while stack and stack[-1] != '(':
                    # flip character in stack[-1] until `(`
                    temp.append(stack.pop())

                # do not forget to pop `(` out
                if stack and stack[-1] == '(':
                    stack.pop()

                # merge stack with flipped string
                stack += temp

        # convert stack to string
        return ''.join(stack)
