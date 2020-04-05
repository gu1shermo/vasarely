def my_insert(listA,n):
    try:
        assert type(n) is int, "pas le bon type"
    
        
        for index,_ in enumerate(listA):
            if index > len(listA) - 2:
                break
            if n < listA[0]:
                listA.insert(0,n)
            if n > listA[len(listA)-1]:
                listA.append(n)
            if n > listA[index] and n < listA[index+1]:
                listA.insert(index+1,n)
        return listA
    except AssertionError as error:
        print(error)


lst = [1,5,78]
print(my_insert(lst,'a'))