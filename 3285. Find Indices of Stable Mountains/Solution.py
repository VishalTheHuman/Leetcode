class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        indices = []
        for i in range(1, len(height)):
            if height[i-1] > threshold:
                indices.append(i)
        return indices
