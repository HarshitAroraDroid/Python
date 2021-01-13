def count_one(dict1):
    """
    This function is used to return the will return maximum value in the dictionary.
    """
    maximum = 0
    key = ""
    ans = {}
    for key1,value in dict1.items():
        if maximum < value:
            maximum = value
            key = key1
    ans.update({key: value})
    return ans

dict1 =  {
   "1" : "name1",
   "2" : "name2",
   "3" : "name3"
}
dict2 =  {
   "1" : 50,
   "2" : 60,
   "3" : 70
}

answer = count_one(dict2)
print(answer)