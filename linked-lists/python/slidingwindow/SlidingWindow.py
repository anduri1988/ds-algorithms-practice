class SlidingWindow:

    def max_sub_array(arr, k):
        """
        Problem: Maximum Sum Subarray of Size K

        Given an array of integers and a number k, find the maximum sum of a subarray of size k.
        Example: [2, 1, 5, 1, 3, 2]
        K : size of sub Array
        Explanation: The subarrays of size 3 are:
        [2, 1, 5] → Sum = 8
        [1, 5, 1] → Sum = 7
        [5, 1, 3] → Sum = 9
        [1, 3, 2] → Sum = 6 The maximum sum is 9.
        TechineProblem Solving Technique: SlidingWindow

        # Test the function
        arr = [2, 1, 5, 1, 3, 2]
        k = 3
        print(max_sum_subarray(arr, k))  # Output: 9

        Time Complexity: Total Time Complexity:
        Initial Window Sum Calculation: This takes O(k) time to compute the sum of the first k elements.
        Sliding Window: Sliding the window from index k to n-1 takes (n - k) iterations. Each iteration involves only constant time operations (adding and subtracting one element), which takes O(1) time for each slide.

        Therefore, the total time spent sliding the window is O(n - k).
        Final Complexity: 
        Total Time Complexity=O(k)+O(n−k)
        Total Time Complexity=O(k)+O(n−k)
        Simplifying this, since O(k) + O(n - k) is essentially just O(n).

        The space complexity of the sliding window algorithm is O(1) because we only store a few variables:
            window_sum (current sum of the window),
            max_sum (the maximum sum encountered),
            and the loop variable i (used for iteration).
        Thus, there is no additional space required that grows with the size of the input array, so the space complexity is O(1).
        """
        window_sum = sum(arr[:k]) # sum of first K elements
        max_sum = window_sum

        # slide the window through the array
        for i in range(k, len(arr)):
            window_sum += arr[i]  # Add new element
            window_sum -= arr[i-k] #  remove old element

            # Update max_sum if the current window's sum is larger
            max_sum = max(max_sum, window_sum)
        return max_sum

sliding_window = SlidingWindow
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(" max sum of sub array: ", sliding_window.max_sub_array(arr, k))