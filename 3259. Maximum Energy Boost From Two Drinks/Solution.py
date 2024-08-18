class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        A = [0] * n
        B = [0] * n
        for i in range(n):
            A[i] = max(A[i-1]+energyDrinkA[i], B[i-2] + energyDrinkA[i])
            B[i] = max(B[i-1]+energyDrinkB[i], A[i-2] + energyDrinkB[i])
        return max(A[-1], B[-1])
