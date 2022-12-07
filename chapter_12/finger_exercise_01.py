# Finger exercise, p.263
# Why does the code use 'mid+1' rather than 'mid' in the second recursive call?

# Figure 12-3, p. 261
def search(L, e):
    """Assumes L is a list, the elements of which are in ascending order.
       Returns True if e is in L and False otherwise
    """
    def bin_search(L, e, low, high):
        # Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            return bin_search(L, e, low, mid-1)
        return bin_search(L, e, mid+1, high)
    
    if len(L) == 0:
        return False
    return bin_search(L, e, 0, len(L)-1)


# The code uses 'mid+1' because we already checked the element at index 'mid'
# and we know that the element is not equal 'e' nor is it greater than 'e'
# With that knowledge we can skip 'mid' for the next recursive call by 
# setting low=mid+1
