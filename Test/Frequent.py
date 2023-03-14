def topKFrequent(nums, k):
    length=len(nums)
    List1=[]
    count=0
    for i in range(length):
        for j in range(length):
            if nums[i]==nums[j]:
                count+=1
        if count>=k:
            List1.append(nums[i])
        count=0
    return list(set(List1))
Listq=[1,45,4,4,4,2,3,3,2,2]
a=topKFrequent(Listq,2)
print(a)