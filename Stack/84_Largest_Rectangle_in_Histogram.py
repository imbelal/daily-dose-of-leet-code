class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, heights[0])]  # index, height
        maxArea = 0
        lastIndex = 0
        for i in range(1, len(heights)):
            x = heights[i]
            lastIndex = i
            if x < stack[-1][1]:
                while(stack and x < stack[-1][1]):
                    lastIndex = stack[-1][0]
                    maxArea = max(maxArea, (i - lastIndex) * stack[-1][1])
                    stack.pop()
            stack.append((lastIndex, x))
        lastIndex = len(heights)
        for i, x in enumerate(stack):
            maxArea = max(maxArea, (lastIndex - x[0]) * x[1])
        return maxArea
