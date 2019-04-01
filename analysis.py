iimport time
import random
import matplotlib.pyplot as plt
import math

def mean(inlist):
    sum = 0
    for i in inlist:
        sum += i
    mean = sum / len(inlist)
    return mean

def is_same(data):
    avg = mean(data)
    no = True
    while True:
        for int in data:
            if int != avg:
                no = False
            else:
                continue
        break
    if no == True:
        return True
    else:
        return False

def Daniel_sort(data):
    greater = []
    less_equal = []
    res = []
    one = False
    if len(data) == 1:
        one = True
        res = data
    while one == False:
        same = is_same(data)
        if same == True:
            return data
        avg = mean(data)
        for i in data:
            if i > avg:
                greater.append(i)
            else:
                less_equal.append(i)
        lower_half = Daniel_sort(less_equal)
        upper_half = Daniel_sort(greater)
        res = res + lower_half + upper_half
        break

    return res

def median(inlist):
    for i in range(1,len(inlist)-1):
        if inlist[i] < inlist[i-1]:
            act = False
        else:
            act = True
    while act:
        if len(inlist) % 2 == 0:
            right = inlist[int(len(inlist)/2)]
            left = inlist[int(len(inlist)/2) - 1]
            sum = right + left
            median = int(sum / 2)
            return median
            break
        else:
            median = inlist[int(len(inlist)/2)]
            return median
            break
    if act == False:
        print("Error: Number not sorted")

def mad(inlist):
    sum = 0
    mean = mean(inlist)
    for int in inlist:
        sum += abs(int - mean)
    mad = sum / len(inlist)
    return mad

def list_gen(length,lb,ub,allow_repeat):
    '''
    length: Length of output list
    lb: Lower bound
    ub: Upper bound
    allow_repeat: True / False

    return a random list
    '''
    out = []
    while len(out) < length:
        r = random.randint(lb, ub)
        if allow_repeat:
            out.append(r)
        elif r not in out:
            out.append(r)
    return out

def selection_sort(inlist):
    '''
    inlist: List to be sorted

    return sorted list
    '''
    out = []
    for x in range(len(inlist)):
        min = inlist[0]
        for i in inlist:
            if i < min:
                min = i
        inlist.remove(min)
        out.append(min)
    return(out)


def merge_sort(inlist):
    if len(inlist)>1:
        mid = len(inlist)//2
        lefthalf = inlist[:mid]
        righthalf = inlist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        a=0
        b=0
        c=0
        while a < len(lefthalf) and b < len(righthalf):
            if lefthalf[a] < righthalf[b]:
                inlist[c]=lefthalf[a]
                a += 1
            else:
                inlist[c]=righthalf[b]
                b += 1
            c += 1

        while a < len(lefthalf):
            inlist[c]=lefthalf[a]
            a += 1
            c += 1

        while b < len(righthalf):
            inlist[c]=righthalf[b]
            b=b+1
            c=c+1


def insertion_sort(inlist):
    '''
    inlist: List to be sorted

    return sorted list
    '''
    for i in range(1,len(inlist)):
        val = inlist[i]
        j = i - 1
        while j >= 0:
            if val < inlist[j]:
                inlist[j+1] = inlist[j]
                inlist[j] = val
                j = j - 1
            else:
                break
    return inlist

def bubble_sort(inlist):
    '''
    inlist: unsorted list

    return sorted list
    '''
    for i in range(len(inlist)-1,0,-1): #range(start, stop, step)
        for j in range(i):
            if inlist[j]>inlist[j+1]:
                inlist[j+1],inlist[j] = inlist[j], inlist[j+1] # Swap 2 value
    return inlist

'''
Quick sort
'''
def get_pivot(data,lb,ub):
    median = (lb+ub)//2
    if data[lb] < data[median]:
        # lb < med
        if data[median] < data[ub]:
            # lb < med < ub
            pivot = median
        else:
            if data[lb] < data[ub]:
                # lb < ub < median
                pivot = ub
            else:
                # ub < lb < median
                pivot = lb
    elif data[lb] < data[ub]:
        # median < lb < ub
        pivot = lb
    else:
        if data[median] < data[ub]:
            # median < ub < lb
            pivot = ub
        else:
            # ub < median < lb
            pivot = median
    return pivot

def partition(data,lb,ub):
    pivotIndex = get_pivot(data,lb,ub)
    pivotValue = data[pivotIndex]
    data[pivotIndex], data[lb] = data[lb], data[pivotIndex]
    border = lb
    for i in range(lb+1,ub+1):
        if data[i] < pivotValue:
            border = border + 1
            data[i], data[border] = data[border], data[i]
    data[lb], data[border] = data[border], data[lb]
    return border

def quick_sort_core(inlist, lb, ub):
    if lb < ub:
        p = partition(inlist,lb,ub)
        quick_sort_core(inlist,lb,p-1)
        quick_sort_core(inlist,p+1,ub)

def quick_sort(inlist):
    quick_sort_core(inlist,0,len(inlist)-1)
    return inlist

if __name__ == "__main__":

    trial_list = [10,50,100,500,1000,2000,5000,10000]
    # trial_list = [10,20,30,40,50,60,70,80,90,100]
    t_bubble = []
    t_insertion = []
    t_selection = []
    t_quick = []
    t_merge = []
    t_Daniel = []
    for trial in trial_list:
        inlist = list_gen(trial,1,100,allow_repeat = True)

        start = time.time()
        outlist = bubble_sort(inlist.copy())
        end = time.time()
        t_bubble.append(end-start)
        print('Bubble Sort {} with {} sec'.format(trial,end-start))

        start = time.time()
        outlist = insertion_sort(inlist.copy())
        end = time.time()
        t_insertion.append(end-start)
        print('Insertion Sort {} with {} sec'.format(trial,end-start))

        start = time.time()
        outlist = selection_sort(inlist.copy())
        end = time.time()
        t_selection.append(end-start)
        print('Selection Sort {} with {} sec'.format(trial,end-start))

        start = time.time()
        outlist = quick_sort(inlist.copy())
        end = time.time()
        t_quick.append(end-start)
        print('Quick Sort {} with {} sec'.format(trial,end-start))

        start = time.time()
        outlist = merge_sort(inlist.copy())
        end = time.time()
        t_merge.append(end-start)
        print('Merge Sort {} with {} sec'.format(trial,end-start))

        start = time.time()
        outlist = Daniel_sort(inlist.copy())
        end = time.time()
        t_Daniel.append(end-start)
        print('Daniel Sort {} with {} sec'.format(trial,end-start))
    plt.figure()
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(trial_list,t_bubble,color='green',label='Bubble Sort')
    plt.plot(trial_list,t_insertion,color='yellowgreen',label='Insertion Sort')
    plt.plot(trial_list,t_selection,color='blue',label='Selection Sort')
    plt.plot(trial_list,t_quick,color='orange',label='Quick Sort')
    plt.plot(trial_list,t_merge,color='red',label='Merge Sort')
    plt.plot(trial_list,t_Daniel,color='purple',label='Daniel Sort')
    plt.xlabel('Amount of data')
    plt.ylabel('Time (sec)')
    plt.legend(loc=1)
    plt.grid(True)
    plt.show()

