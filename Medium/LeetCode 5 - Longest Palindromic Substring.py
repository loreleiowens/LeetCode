class Solution:
    def longestPalindrome(self, s: str) -> str:
        stack = []
        dummyStack = [] # Dummy stack to remove elements from
        queue = []
        newString = ''

      # Add characters to the stacks
        for char in s:
            stack.append(char)
            dummyStack.append(char)

      # Add characters to the queue
        for i in range(len(stack)):
            letter = dummyStack.pop()
            queue.append(letter)

      # Check if the characters within the stack & queue line up
        for letter in range(len(queue)):
            if stack[letter] == queue[letter]:
                newString += stack[letter]
        
        return newString
