"""
394. Decode String
https://leetcode.com/problems/decode-string/
Stack
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for cha in s:
            if cha != ']':
                stack.append(cha)
            else:
                # cha == ']'

                # get string
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop()
                temp = temp[::-1]

                # get number
                temp2 = []
                while stack and stack[-1].isdigit():
                    temp2.append(stack.pop())
                temp2 = temp2[::-1]
                num = int(''.join(temp2))

                # merge
                stack += temp * num

        return ''.join(stack)
