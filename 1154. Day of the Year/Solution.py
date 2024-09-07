class Solution:
    def dayOfYear(self, date: str) -> int:
        dayCount = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = list(map(int, date.split("-")))
        if year%4 == 0 and (year%100 != 0 or year%1000 == 0):
            dayCount[2] += 1
        days = 0
        for i in range(month):
            days += dayCount[i]
        return days + day
