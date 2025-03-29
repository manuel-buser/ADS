import random

a = [n for n in range(40)]

# -------------------------------------
# 📊 Selection Sort – Runtime Analysis
#
# Best Case:    O(n²) comparisons, O(n) swaps
# Average Case: O(n²) comparisons, O(n) swaps
# Worst Case:   O(n²) comparisons, O(n) swaps
#
# Notes:
# - Not adaptive (does not benefit from already sorted input)
# - Number of comparisons is always the same: n(n−1)/2
# - Number of swaps: exactly n−1 (one per outer iteration)
# -------------------------------------
def selection_sort(a):
    # Outer loop runs (n - 1) times
    for i in range(len(a) - 1):
        mind_ind = i
        # Inner loop does (n - i - 1) comparisons in this round
        # Total comparisons across all loops = n(n - 1)/2 → O(n²)
        for j in range(i + 1, len(a)):
            if a[j] < a[mind_ind]:
                mind_ind = j
        # One swap per outer loop → (n - 1) swaps in total → O(n)
        a[i], a[mind_ind] = a[mind_ind], a[i]
    return a


def selection_sort_with_prints(a):
    # Same algorithm as above, with added print statements to trace the process
    for i in range(len(a) - 1):
        mind_ind = i
        print(f"\n🔍 Looking for the minimum from index {i} to {len(a) - 1}")

        for j in range(i + 1, len(a)):
            if a[j] < a[mind_ind]:
                mind_ind = j
                print(f"   ➡️ New minimum found: a[{j}] = {a[j]}")

        if mind_ind != i:
            print(f"🔁 Swapping a[{i}] = {a[i]} with a[{mind_ind}] = {a[mind_ind]}")
            a[i], a[mind_ind] = a[mind_ind], a[i]
        else:
            print(f"✅ No swap needed, a[{i}] = {a[i]} is already minimum")

        print(f"Array after step {i}: {a}")

    return a


if __name__ == '__main__':
    random.shuffle(a)
    print("🔀 Shuffled array:", a)

    selection_sort(a)
    print("✅ Sorted array:", a)

    random.shuffle(a)
    print("\n🔄 Shuffled again for detailed run:")
    selection_sort_with_prints(a)
