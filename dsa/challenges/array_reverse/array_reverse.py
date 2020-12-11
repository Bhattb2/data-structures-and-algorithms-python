def reverseArray(list):
      new_list=[]
  for i in range((len(list)),0,-1):
    new_list.append(list[i-1])
  return new_list

def reverseArray2(list):
    for i in range(len(list)//2):
        list[i], list[-1-i] = list[-1-i], list[i]
    return list

def reverseArray3(list):
    list.reverse()
    return list