# ----------------------------------------------
# 📊 Bottom-Up Merge Sort – Runtime Analysis
#
# Time Complexity:
#   Worst Case:   O(n log n)
#   Average Case: O(n log n)
#   Best Case:    O(n log n) (still splits & merges regardless of order)
#
# Space Complexity:
#   O(n) extra space (uses a temp array)
#
# Stable: ✅ Yes (keeps original order of equal elements)
# Adaptive: ❌ No (does not benefit from already sorted input - only with improvements)
#
# Notes:
#   - Uses an iterative approach (no recursion)
#   - Builds up sorted subarrays of size 1, 2, 4, 8, ...
#   - Great for systems that avoid recursion (e.g., limited stack space)
# ----------------------------------------------

def merge(array, tmp, lo, mid, hi):
    print(f"🔁 Merging [{lo}..{mid}] and [{mid + 1}..{hi}]")
    i = lo
    j = mid + 1

    for k in range(lo, hi + 1):
        if j > hi or (i <= mid and array[i] <= array[j]):
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1

    for k in range(lo, hi + 1):
        array[k] = tmp[k]

    print(f"✅ Result after merge: {array[lo:hi + 1]}")


def bottom_up_merge_sort(array):
    n = len(array)
    tmp = [0] * n
    length = 1
    step = 1

    while length < n:
        print(f"\n🔄 Pass {step}: merging subarrays of length {length}")
        lo = 0
        while lo < n - length:
            mid = lo + length - 1
            hi = min(lo + 2 * length - 1, n - 1)
            merge(array, tmp, lo, mid, hi)
            lo += 2 * length
        step += 1
        length *= 2
    print("\n✅ Final sorted array:", array)


# 🔬 TESTING — just run, no wrapping
print("\n====== Bottom-Up Merge Sort Tests ======")

arr1 = [5, 3, 8, 1, 2, 7]
print("Before:", arr1)
bottom_up_merge_sort(arr1)
print("After: ", arr1)

arr2 = [1, 2, 3, 4, 5]
print("\nBefore:", arr2)
bottom_up_merge_sort(arr2)
print("After: ", arr2)

arr3 = [5, 4, 3, 2, 1]
print("\nBefore:", arr3)
bottom_up_merge_sort(arr3)
print("After: ", arr3)

arr4 = [1, 1, 1, 1]
print("\nBefore:", arr4)
bottom_up_merge_sort(arr4)
print("After: ", arr4)

arr5 = []
print("\nBefore:", arr5)
bottom_up_merge_sort(arr5)
print("After: ", arr5)
