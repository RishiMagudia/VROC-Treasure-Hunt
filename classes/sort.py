class Sort:

    def __init__(self):
        """
        Class for hosting sorting algorightms.
        """
        self.order

    def order(self, x):
        """
        Change the order of the data.
        :return:
        """
        return reversed(x)

    def merge(aList, bList, animation = []):
    
        if len(aList) > 1:
            #---------------- step 1
            #splits list in half
            mid = len(aList)//2
                #stores left side of split list on leftside and right side on rightside
            leftside = aList[:mid]
            rightside = aList[mid:]
                #recursion to itself until split into a single element
                #starting with leftside
            mergeSort(leftside, bList, animation)
            mergeSort(rightside, bList, animation)
            #---------------- step 2
            #holders for element position in l-left side, r-right side, c-aList
            l = 0
            r = 0
            c = 0
            #loop until checked all elements in both sides
            while l<len(leftside) and r<len(rightside):
                #if rightside is bigger, store element from leftside
                #in element c of aList
                if rightside[r] > leftside[l]:
                    bList[c] = leftside[l]
                    aList[c] = leftside[l]
                    l += 1
                #else store rightside in element c of aList
                else:
                    bList[c] = rightside[r]
                    aList[c] = rightside[r]
                    r += 1
                c += 1
            #---------------- step 3
            #if rightside was bigger switch leftside to element c+1
            while l<len(leftside):
                bList[c] = leftside[l]
                aList[c] = leftside[l]
                print "bList:", bList
                animation.append(bList)
                l +=1
                c +=1
            #if leftside was bigger switch rightside to element c+1
            while r<len(rightside):
                bList[c] = rightside[r]
                aList[c] = rightside[r]
                print "bList:",bList
                animation.append(bList)
                r +=1
                c +=1
        return animation

    def quick(self):
     animation = []
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
      
       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   r = []
   for i in alist:
      r.append(i)
   animation.append(r)
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   

   return rightmark

alist = [6,23,5,89,85,52,20,12,36,13,14,16,29]
quickSort(alist)
print(alist)

for i in animation:
   print i

   
   
        """

        :return:
        """

    def insert(self, alist):
        animation = []
        for index in range(1,len(alist)):
            currentvalue = alist[index]
            position = index
            while position>0 and alist[position-1]>currentvalue:
                alist[position]=alist[position-1]
                position = position-1

            r = []
            for i in alist:
                r.append(i)
            animation.append(r)
                
            alist[position]=currentvalue

        return animation

    def bubble(self):
        """

        :return:
        """

    def heap(self, lst):
        animation = []
        def siftdown(lst, s, e):
            i = s
            while True:
                c = i * 2 + 1
                if c > e:
                    break
                if c + 1 <= e and lst[c] < lst[c + 1]:
                    c += 1
                if lst[i] < lst[c]:
                    lst[i], lst[c] = lst[c], lst[i]
                    i = c
                else:
                    break
            r = []
            for i in lst:
                r.append(i)
            animation.append(r)

        for s in range((len(lst) - 2) / 2, -1, -1):
            siftdown(lst, s, len(lst) - 1)

        for e in range(len(lst) - 1, 0, -1):
            lst[e], lst[0] = lst[0], lst[e]
            siftdown(lst, 0, e - 1)

        return animation

    def shellSort(self,lst):
        count = len(lst)//2
        while count > 0:
            for posStart in range(count):
                insertGap(lst,posStart,count)
            count = count //2


    def insertGap(self,lst,start,gap):
        for x in range(start+gap,len(lst),gap):
            current = lst[x]
            pos = x

            while pos >=gap and lst[pos-gap] > current:
                lst[pos] = lst[pos-gap]
                pos = pos-gap
            lst[pos] = current


