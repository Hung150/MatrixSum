# simple_test.py
class Solution:
    def maxMatrixSum(self, matrix):
        n = len(matrix)
        total_sum = 0
        min_abs = float('inf')
        negative_count = 0
        
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                abs_val = abs(val)
                total_sum += abs_val
                min_abs = min(min_abs, abs_val)
                
                if val < 0:
                    negative_count += 1
        
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs
        
        return total_sum

# Test ngay
matrix = [[1, -1], [-1, 1]]
sol = Solution()
result = sol.maxMatrixSum(matrix)
print(f"Matrix: {matrix}")
print(f"Result: {result}")
print("Expected: 4")
print(f"Test {'PASSED' if result == 4 else 'FAILED'}")

# Test thêm
print("\n--- More tests ---")
test_cases = [
    ([[1, 2, 3], [-1, -2, -3], [1, 2, 3]], 16),
    ([[-1, 0, -1], [-2, 1, 3], [4, 5, -6]], 23),
]

for matrix, expected in test_cases:
    result = sol.maxMatrixSum(matrix)
    print(f"\nMatrix: {matrix}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"{'✓' if result == expected else '✗'}")
