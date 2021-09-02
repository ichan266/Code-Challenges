# Leetcode # 347
# https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from collections import Counter
import heapq


def topKFrequent(nums, k):

    if len(nums) == k:
        return nums

    count = Counter(nums)

    return heapq.nlargest(k, count.keys(), key=count.get)

#         countItems = sorted(count.items(), key=lambda item: item[1])

#         return [item[0] for item in countItems[-k:]]
