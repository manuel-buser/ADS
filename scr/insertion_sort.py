def insertion_sort(array):
    # Runtime:
    # Best Case:    O(n) comparisons, 0 swaps (already sorted)
    # Worst Case:   O(n^2) comparisons and swaps (reversed)
    # Average Case: O(n^2)
    # Space: O(1), In-place: ✅, Stable: ✅, Adaptive: ✅

    n = len(array)
    for i in range(1, n):  # Loop runs n-1 times
        j = i
        # Inner loop can run up to i times → total work across all i is O(n^2)
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


def insertion_sort_with_prints(array):
    # Same algorithm with print statements to show step-by-step behavior

    n = len(array)
    for i in range(1, n):
        print(f"\n🔍 Inserting element at index {i} (value {array[i]})")
        j = i
        while j > 0 and array[j - 1] > array[j]:
            print(f"   ↪️ array[{j - 1}] = {array[j - 1]} > array[{j}] = {array[j]} → swapping")
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
            print(f"   📦 Current array state: {array}")
        if j == i:
            print(f"✅ Element at index {i} already in correct place")
        else:
            print(f"✅ Inserted at index {j}, array now: {array}")

def insertion_sort_slightly_faster(array):
    for i in range(1, len(array)):
        val = array[i]  # 🔹 Store the current element (we’ll insert it later)
        j = i  # 🔹 j will track where we need to insert val

        # 🔁 Shift all elements > val one step to the right
        while j > 0 and array[j - 1] > val:
            array[j] = array[j - 1]  # 🔸 Move the larger element to the right
            j -= 1  # 🔸 Check the next element to the left

        # ✅ Insert the saved value at its final correct position
        array[j] = val # this way we reduce unnecessary swapping



# 🔬 Testing the function
a = [5, 3, 4, 1, 2]
print("🔄 Before sorting:", a)
insertion_sort_with_prints(a)
print("\n✅ Final sorted array:", a)







