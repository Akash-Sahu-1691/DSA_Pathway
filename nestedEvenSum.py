'''

'''


obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

# print(obj2["a"])

'''
BRO, you were checking type and not using type() instead you directly used
like -> if obj[key] == int:     -----> obj[key] gives value like obj2[d]=1
You were correct in second or third attempt but that damn type(), crushed all hope..!!
'''

def nestedEvenSum(obj,s=0):
    for key in obj:
        if type(obj[key]) is int:
            if obj[key]%2==0:
                s=s+obj[key]
        elif type(obj[key]) is dict:
            s=s+nestedEvenSum(obj[key])
    return s
# def nestedEvenSum(obj, sum=0):
#     for key in obj:
#         if type(obj[key]) is dict:
#             sum += nestedEvenSum(obj[key])
#         elif type(obj[key]) is int and obj[key]%2==0:
#             sum+=obj[key]
#     return sum
print(nestedEvenSum(obj1))
print(nestedEvenSum(obj2))