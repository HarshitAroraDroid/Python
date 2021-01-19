def count_one(dict1,dict2):
    """
    This function is used to return the will return maximum value in the dictionary.
    """
    # maximum = 0
    # key = ""
    ans = {}
    for key1,value1 in dict1.items():
        for key2,value2 in dict2.items():
            if key1 == key2:
                # print(value1 + " Got " + str(value2) + " marks.")
    #     if maximum < value:
    #         maximum = value
    #         key = key1
                ans.update({value1: value2})
    return ans
    
dict1 =  {
   "1" : "name1",
   "2" : "name2",
   "3" : "name3",
}
dict2 =  {
   "1" : 50,
   "2" : 60,
   "3" : 70,
}

answer = count_one(dict1,dict2)
print(answer)