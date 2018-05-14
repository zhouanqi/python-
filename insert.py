# -*- coding: utf-8 -*-

class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """

    def insert(self, intervals, newInterval):
        weizhi = 0
        result = []
        if newInterval.start == None:
            return intervals

        for interval in intervals:
            if interval.start > newInterval.end:
                result.append(interval)
            elif interval.end > newInterval.start:
                result.append(interval)
                weizhi = weizhi + 1
            else:
                newInterval.start = min(interval.end, newInterval.start)
                newInterval.end = min(interval.start, newInterval.end)
        result.insert(weizhi, newInterval)
        return result

