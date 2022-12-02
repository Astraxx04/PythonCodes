def DishPrepareOrder(order_list):
    (d,d_new)=({},{})
    for order in order_list:
        if order in d:
            d[order]+=1
        else:
            d[order]=1
    for key in d:
        if d[key] in d_new:
          d_new[d[key]].append(key)
        else:
          d_new[d[key]]=[key]
    print(d)
    print(d_new)
    #store the max occurance in a list and sort it
    order_no_list=[]
    [order_no_list.append(key) for key in d_new.keys()]
    order_no_list.sort()
    new_order_list=[]
    while len(order_no_list)>0:
      new_array=d_new[order_no_list[-1]]
      new_array.sort()
      [new_order_list.append(order) for order in new_array]
      order_no_list=order_no_list[0:len(order_no_list)-1]
    return new_order_list
nums = eval(input())
print(DishPrepareOrder(nums))
nums = eval(input())
print(DishPrepareOrder(nums))