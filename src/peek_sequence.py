def peek_sequence(nums):
    k = 1
    peek_s, cur_seq = 0, 0
    while k < len(nums) - 1:
        if nums[k - 1] < nums[k] and nums[k] > nums[k + 1]:
            cur_peek = k
            while cur_peek - 1 >= 0 and nums[cur_peek] > nums[cur_peek - 1]:
                cur_seq += 1
                cur_peek -= 1
            cur_peek = k
            cur_seq += 1
            while cur_peek < len(nums) - 1 and nums[cur_peek] > nums[cur_peek + 1]:
                cur_seq += 1
                cur_peek += 1
            if peek_s < cur_seq:
                peek_s = cur_seq
            cur_seq = 0
        k += 1
    return peek_s
