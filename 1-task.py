def majority_element(arr):
    counts = {}

    for n in arr:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

        if counts[n] > len(arr) // 2:
            return n