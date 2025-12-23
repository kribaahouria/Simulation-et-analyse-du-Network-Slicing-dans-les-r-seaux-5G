def max_delay(slice_obj):
    if not slice_obj.delays:
        return 0
    return max(slice_obj.delays)

def min_delay(slice_obj):
    if not slice_obj.delays:
        return 0
    return min(slice_obj.delays)

def variance_delay(slice_obj):
    if not slice_obj.delays:
        return 0
    mean = slice_obj.average_delay()
    return sum((d - mean)**2 for d in slice_obj.delays) / len(slice_obj.delays)
