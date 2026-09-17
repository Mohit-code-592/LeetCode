# container with most water

def brute_force(height):
    max_water = 0
    for i in range(len(height) - 1):
        for j in range(i + 1, len(height)):
            water = j - i
            min_height = min(height[i], height[j])
            current_water = water * min_height
            max_water = max(max_water, current_water)
        
    return max_water


def Optimal(height):
    max_water = 0
    left = 0
    right = len(height) - 1

    while left < right:
        water = right - left
        min_height = min(height[left], height[right])
        current_water = water * min_height
        max_water = max(max_water, current_water)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water                