def rotate(nums, k):
    n = len(nums)
    k %= n  # Handle cases where k > n
    
    # Helper function to reverse part of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Reverse entire array
    reverse(0, n - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, n - 1)
