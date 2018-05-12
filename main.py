'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def quickSort(alist,ser):
   quickSortHelper(alist,0,len(alist)-1,ser)

def quickSortHelper(alist,first,last,ser):
   if first<last:

       splitpoint = partition(alist,first,last,ser)

       quickSortHelper(alist,first,splitpoint-1,ser)
       quickSortHelper(alist,splitpoint+1,last,ser)


def partition(alist,first,last,ser):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = ser[leftmark]
           ser[leftmark]=ser[rightmark]
           ser[rightmark]=temp
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
   temp = ser[first]
   ser[first]=ser[rightmark]
   ser[rightmark]=temp
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
#inputs has to be given here ie sentimental score of each review
a = [10.2,  14.8,  14.4,   14.4,  14.4,  14.5,  14.5,  14.6,  14.7,   14.7,  14.7,  14.9,  15.1,  15.9,   16.4]
ser=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]#can be used to find review no after a sorted list
c = len(a)-1
quickSort(a,ser)#performing quicksort and noting the correponding positions of updated sorted order in ser
print(a)
print(ser)
if c%2 == 0:#no of elements is odd
    j = c/2
    j = int(j)
    q2 = a[j]                          #second quartile
    j1=j/2
    j1=int(j1)
    q1 =(a[j1]+a[j1+1])/2              #first quartile
    q3 = (a[j+j1]+a[j+j1+1])/2         #third quartile
else:                 #no of elements is even
    j = (c/2)-1
    j = int(j)
    q2 = (a[j]+a[j+1])/2
    j1=j/2
    j1=int(j1)
    q1=a[j1]
    q3=a[j+j1]
mi = a[0]                           #minimum value in data
ma = a[c]                           #maximum value in the data
iqr =(q3-q1)                        #IQR = quartile3 -quartile1
p = max(mi,(q1-1.5*iqr))
q = min(ma,(q3+1.5*iqr))
print(q1)
print(q2)
print(q3)
print(p)
print(q)
#the outliers are the values less than p and greater than q
