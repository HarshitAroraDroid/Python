def count_one(list1):
    """
    This function is used to return the count of maximum consecutive one’s present in the  list.
    """
    ans, count = 0, 0
    for ele in list1:
        if ele == 1:
            count+=1
            if ans < count:
                ans = count
        else:
            count = 0
    return ans

list1 = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
answer = count_one(list1)
print(answer)