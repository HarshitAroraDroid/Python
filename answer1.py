def add_list(list1):
    """
    This function is used to return sum of all values present in list.
    """
    ans = 0
    for ele in list1:
        ans += ele
    return ans

list1 = [2,3,4,25,43,26,76,89]
answer = add_list(list1)
print(answer)