# ----------------------------------------------
# 📊 Optimized Merge Sort – Runtime Analysis
#
# Time Complexity:
#   Worst Case:   O(n log n)
#   Average Case: O(n log n)
#   Best Case:    O(n log n), or close to O(n) with optimizations
#
# Space Complexity:
#   O(n) extra space (uses a temporary array)
#
# Stable: ✅ Yes
# Adaptive: ⚠️ Not in standard form, but ✅ with optimizations
#
# Optimizations:
# ✅ Optimization 1: Use insertion sort for small subarrays (hi - lo <= 10)
#     → reduces overhead, better cache usage
# ✅ Optimization 2: Skip merge if already sorted
#     → avoids unnecessary merging when data is partially sorted
# ----------------------------------------------

# 🔧 Insertion Sort for a subarray from lo to hi
def insertion_sort_range(array, lo, hi):
    for i in range(lo + 1, hi + 1):
        val = array[i]
        j = i
        # Shift elements right until correct position for val is found
        while j > lo and array[j - 1] > val:
            array[j] = array[j - 1]
            j -= 1
        array[j] = val


# 🔁 Standard merge step: merge two sorted halves [lo..mid] and [mid+1..hi]
def merge(array, tmp, lo, mid, hi):
    i = lo           # pointer for left half
    j = mid + 1      # pointer for right half

    # Merge elements into tmp array in sorted order
    for k in range(lo, hi + 1):
        if j > hi or (i <= mid and array[i] <= array[j]):
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1

    # Copy sorted tmp segment back to original array
    for k in range(lo, hi + 1):
        array[k] = tmp[k]


# 🧠 Main entry point: creates the tmp array and starts recursion
def sort(array):
    tmp = [0] * len(array)  # helper array for merging
    sort_aux(array, tmp, 0, len(array) - 1)


# 🔁 Recursive sort helper: divides array and merges back
def sort_aux(array, tmp, lo, hi):
    if hi <= lo:
        return

    # 🔍 Print what part we're about to sort
    print(f"\n📦 Sorting range [{lo}, {hi}]")

    # ✅ Use insertion sort for small parts
    if hi - lo <= 10:
        print(f"✨ Using insertion sort for range [{lo}, {hi}]")
        insertion_sort_range(array, lo, hi)
        return

    mid = lo + (hi - lo) // 2

    sort_aux(array, tmp, lo, mid)
    sort_aux(array, tmp, mid + 1, hi)

    # ✅ Skip merge if already sorted
    if array[mid] <= array[mid + 1]:
        print(f"⏭️  Skipping merge for [{lo}, {hi}] (already sorted)")
        return

    print(f"🔁 Merging range [{lo}, {mid}] and [{mid + 1}, {hi}]")
    merge(array, tmp, lo, mid, hi)

