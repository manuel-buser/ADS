# ------------------------------------------------------------------------------------#
# 📊 Merge Sort – Runtime Analysis
#
# Time Complexity:
#   Worst Case:   O(n log n)
#   Average Case: O(n log n)
#   Best Case:    O(n log n)
#
# Space Complexity:
#   O(n) extra space (for the temp array)
#
# Stable: ✅ Yes – keeps the order of equal elements
# Adaptive: ❌ No – does full recursion and merging, even if already sorted - only adaptive with optimizations
#
# Characteristics:
#   - Divide-and-conquer strategy
#   - Recursive (top-down)
#   - Good for large datasets
# ------------------------------------------------------------------------------------#

def merge(array, tmp, lo, mid, hi):
    i = lo
    j = mid + 1
    # Merge elements from both halves into tmp
    for k in range(lo, hi + 1):
        if j > hi or (i <= mid and array[i] <= array[j]):
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1
    # Copy sorted elements back into original array
    for k in range(lo, hi + 1):
        array[k] = tmp[k]


def sort(array):
    tmp = [0] * len(array)  # Temporary helper array
    sort_aux(array, tmp, 0, len(array) - 1)


def sort_aux(array, tmp, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    sort_aux(array, tmp, lo, mid)         # Sort left half
    sort_aux(array, tmp, mid + 1, hi)     # Sort right half
    merge(array, tmp, lo, mid, hi)        # Merge both halves

# ------------------------------------------------------------------------------------#
# added inside functions print statements for deeper understanding
# ------------------------------------------------------------------------------------#

def merge_with_prints(array, tmp, lo, mid, hi):
    print(f"\n🔀 Merging range [{lo}, {hi}] with mid = {mid}")
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if j > hi or (i <= mid and array[i] <= array[j]):
            print(f"   ✅ Taking array[{i}] = {array[i]}")
            tmp[k] = array[i]
            i += 1
        else:
            print(f"   🔁 Taking array[{j}] = {array[j]}")
            tmp[k] = array[j]
            j += 1
    print(f"📥 Copying merged elements back to array[{lo}:{hi + 1}]")
    for k in range(lo, hi + 1):
        array[k] = tmp[k]
    print(f"✅ Merged result: {array[lo:hi + 1]}")


def sort_with_prints(array):
    tmp = [0] * len(array)
    sort_aux_with_prints(array, tmp, 0, len(array) - 1)


def sort_aux_with_prints(array, tmp, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    print(f"\n📦 sort_aux called on range [{lo}, {hi}], mid = {mid}")
    sort_aux_with_prints(array, tmp, lo, mid)
    sort_aux_with_prints(array, tmp, mid + 1, hi)
    merge_with_prints(array, tmp, lo, mid, hi)

arr = [5, 3, 8, 1, 2, 7]
print("🔄 Original array:", arr)
sort_with_prints(arr)
print("✅ Final sorted array:", arr)




