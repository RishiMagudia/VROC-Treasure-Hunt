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

    def merge(aList):
        
        if len(aList) > 1:
        #---------------- step 1
        #splits list in half
        mid = len(aList)//2
            #stores left side of split list on leftside and right side on rightside
        leftside = aList[:mid]
        rightside = aList[mid:]
            #recursion to itself until split into a single element
            #starting with leftside
        mergeSort(leftside)
        mergeSort(rightside)
        #---------------- step 2
        #holders for element position in l-left side, r-right side, c-aList
        l = 0
        r = 0
        c = 0
        print aList
        #loop until checked all elements in both sides
        while l<len(leftside) and r<len(rightside):
            #if rightside is bigger, store element from leftside
            #in element c of aList
            if rightside[r] > leftside[l]:
                aList[c] = leftside[l]
                l += 1
            #else store rightside in element c of aList
            else:
                aList[c] = rightside[r]
                r += 1
            c += 1
        #---------------- step 3
        #if rightside was bigger switch leftside to element c+1
        while l<len(leftside):
            aList[c] = leftside[l]
            print aList
            l +=1
            c +=1
        #if leftside was bigger switch rightside to element c+1
        while r<len(rightside):
            aList[c] = rightside[r]
            print aList
            r +=1
            c +=1

    def quick(self):
        """

        :return:
        """

    def insert(self):
        """
        #Amraiz's Sort 
        :return:
        """

    def bubble(self):
        """

        :return:
        """

    def heap(self):
        """

        :return:
        """
