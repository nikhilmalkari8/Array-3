def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    leftMax, rightMax = 0, 0
    trapped_water = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                trapped_water += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                trapped_water += rightMax - height[right]
            right -= 1

    return trapped_water
