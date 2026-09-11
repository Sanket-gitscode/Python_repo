def findMedianSortedArrays(nums1, nums2):
        c_list = sorted(nums1 + nums2)

        def helper(array):

            mid = (len(array)-1) // 2
            mid_m1= mid - 1

            median = (array[mid] + array[mid_m1]) / 2

            return median
        
        result = helper(c_list)

        return round(result)
    
    
print(findMedianSortedArrays([1,2],[3,4]))