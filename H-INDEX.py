def hIndex(citations):
    n = len(citations)
    buckets = [0] * (n + 1)
    
    # Fill the buckets
    for c in citations:
        if c >= n:
            buckets[n] += 1
        else:
            buckets[c] += 1
    
    # Compute H-Index
    total = 0
    for i in range(n, -1, -1):
        total += buckets[i]
        if total >= i:
            return i
    
    return 0
