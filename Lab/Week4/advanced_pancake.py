def flip(arr, start, end):
    """Flip/reverse elements from start to end (inclusive)"""
    arr = arr.copy()
    arr[start:end+1] = arr[start:end+1][::-1]
    return arr

def get_breakpoints(arr):
    """Find positions where consecutive elements aren't consecutive in value"""
    bps = []
    for i in range(1, len(arr)): 
        if abs(arr[i - 1] - arr[i]) != 1:
            bps.append(i)  
    return bps

def rearrange_arr(arr, bps):
    flips = []
    arr = arr.copy()
    sorted_arr = list(range(1, len(arr) + 1))
    
    while arr != sorted_arr:
        bps = get_breakpoints(arr)  
        
        if not bps:  
            break
            
        best_flip = None
        best_bp_count = len(bps)
        
        
        for i in range(len(bps)):
            for j in range(i + 1, len(bps)):
            
                test_arr = flip(arr, bps[i], bps[j] - 1)
                new_bps = get_breakpoints(test_arr)
                
                
                if len(new_bps) < best_bp_count:
                    best_bp_count = len(new_bps)
                    best_flip = (bps[i], bps[j] - 1)
        if best_flip:
            arr = flip(arr, best_flip[0], best_flip[1])
            flips.append(list(best_flip))
            print(f"Flipped from {best_flip[0]} to {best_flip[1]}: {arr}")
    
    return flips, arr

# Test
arr = [1, 8, 9, 2, 3, 7, 6, 5, 4, 10]
print(f"Original array: {arr}")

breakpoints = get_breakpoints(arr)
print(f"Initial breakpoints: {breakpoints}")

flips, result = rearrange_arr(arr, breakpoints)
print(f"Final array: {result}")
print(f"Number of flips: {len(flips)}")
print(f"Flip operations: {flips}")