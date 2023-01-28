class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []  # position, speed
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        for p, s in pair:
            if stack and (target - p) / s <= (target - stack[-1][0]) / stack[-1][1]:
                continue
            else:
                stack.append((p, s))
        return len(stack)
