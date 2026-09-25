def findMedianSortedArrays(nums1, nums2):

    # Always binary search on the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)

    # Number of elements that should be on the left
    left_size = (m + n + 1) // 2

    low = 0
    high = m

    while low <= high:

        # Partition positions
        cut1 = (low + high) // 2
        cut2 = left_size - cut1

        # Elements around nums1's partition
        nums1_left = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
        nums1_right = float("inf") if cut1 == m else nums1[cut1]

        # Elements around nums2's partition
        nums2_left = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
        nums2_right = float("inf") if cut2 == n else nums2[cut2]

        # Correct partition
        if nums1_left <= nums2_right and nums2_left <= nums1_right:

            # Odd total
            if (m + n) % 2 == 1:
                return max(nums1_left, nums2_left)

            # Even total
            else:
                left_max = max(nums1_left, nums2_left)
                right_min = min(nums1_right, nums2_right)

                return (left_max + right_min) / 2

        # nums1 partition is too far right
        elif nums1_left > nums2_right:
            high = cut1 - 1

        # nums1 partition is too far left
        else:
            low = cut1 + 1
