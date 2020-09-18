#循环for和列表list
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
#notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")

#二维列表 [[1,2,3],[4,5,6]]
#range()函数不包含最后一个数
#列表操作: index 从 0 开始
"""
    create a list:              thislist = ["apple", "banana", "cherry"]
    access items:               thislist[1]
    negative indexing:          thislist[-1]
    range of indexes:           thislist[2:5]   [2,5)
                                thislist[:4]    [0,4)
                                thislist[2:]    [2,end]
                                thislist[-4,-1] [-4,-1)
    change item value:          thislist[1] = "blackcurrant"
    loop through a list:        for x in thislist:
    check if item exists:       if "apple" in thislist:
    list length:                len(thislist)

    To add an item to the end of the list:  thislist.append("orange")            
    To add an item at the specified index:  thislist.insert(1, "orange")
    Remove Item:
        1.remove(): removes the specified item
            thislist.remove("banana")
        2.pop():    removes the specified index, (or the last item if index is not specified)
            thislist.pop()
        3.del:      The del keyword removes the specified index;can also delete the list completely
            del thislist[0] ; del thislist
        4.clear():  empties the list
            thislist.clear()
    Copy a list:
        1.copy():   Make a copy of a list
            mylist = thislist.copy()
        2.list():   Make a copy of a list
            mylist = list(thislist)

    Join two list:
        1.+:        One of the easiest ways are by using the + operator
            list3 = list1 + list2
        2.append():
            for x in list2: 
                list1.append(x)
        3.extend(): add list2 at the end of list1
            list1.extend(list2)

    The list() Constructor: thislist = list(("apple","banana","cherry"))

    List Methods:
        Method	    Description
        append()	Adds an element at the end of the list
        clear()	    Removes all the elements from the list
        copy()	    Returns a copy of the list
        count()	    Returns the number of elements with the specified value
        extend()	Add the elements of a list (or any iterable), to the end of the current list
        index()	    Returns the index of the first element with the specified value
        insert()	Adds an element at the specified position
        pop()	    Removes the element at the specified position
        remove()	Removes the item with the specified value
        reverse()	Reverses the order of the list
        sort()	    Sorts the list
"""
        