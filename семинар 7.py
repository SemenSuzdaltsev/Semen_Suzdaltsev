class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

from collections import deque

a = deque()

a.append(1)
a.appendleft(3)
a.pop()
a.popleft()
a.extend("123")

class Node: #узел
    def __init__(self, val = None):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.len = 0

    def __contains__(self,val):
        cur = self.head
        while cur:
            if cur.val == val:
                return True
            else:
                cur = cur.next()
        return False

    def append(self, new):
        cur = self.head
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            self.len+=1
        else:
            while(cur.next):
                cur = cur.next()
            cur.next = new_node
            self.len +=1

    def remove(self,val):
        cur = self.head
        last = None
        while cur:
            if cur.val ==val:
                if last is None:
                    self.head = cur.next
                else:
                    last.next = cur.next
                len-=1
                return
            last = cur
            cur = cur.next

#теперь если хотим легко проворачивать операции с элементами из конца просто делаем self.tail

def functions(*args): #можем подать числа, строки
    pass

def function(**kwargs): #любое количество именовованных аргументов (a = "a", b = "b", c = 1)
    pass

sum = lambda x,y: x+y #краткое задание функций
num = [1,2,3,4,5]
print(list(map(lambda x: x**2,num)))

def even_fn(x):
    return x%2 ==0

print(list(filter(even_fn,[1,2,3,4,5]))) #filter применит функцию и оставить трушные

def bin_search(arr,target):
    if not arr:
        return -1
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            right = mid -1
        else:
            left = mid+1
    return -1

def fibonacci(N, cache = {0:0,1:1}):
    if N in cache:
        return cache[N]
    else:
        cache[N] = fibonacci[N-1,cache]+fibonacci[N-2, cache]
        return cache[N]

import random

def bubble_sort(a):
    for j in range(len(a)-1):
        for i in range(len(a)-j-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1],a[i]
    return a

print(bubble_sort(random.sample(range(1,101),10)))

def insertion_sort(a):
    for i in range(1,len(a)):
        key_item = a[i]
        j = i-1
        while j>=0 and a[j] >key_item:
            a[j+1] = a[j]
            j-=1
        a[j+1] = key_item    
    return a

def choice_sort(a):
    for i in range(len(a)-1):
        min_index = i
        for j in range(i+1,len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        #или a.insert(i,a.pop(min_index))
     
    return a

def levenshtein_distance(word1,word2):
    len1,len2 = len(word1),len(word2)
    dp = [[0]*(len2+1) for _ in range(len1+1)]

    for i in range(len1+1):
        dp[i][0] = i
    for j in range(len2+1):
        dp[0][j] = j

    for i in range(1,len1+1):
        for j in range(1,len2+1):
            dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1, dp[i-1][j-1]+(word1[i-1] != word2[j-1]))

    return dp[len1][len2]


def lcs(a,b):
    dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]
    for i in range(len(a)+1):
        dp[i][0] = i
    for j in range(len(b)+1):
        dp[0][j] = j
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])

    res =[]
    i,j = len(a),len(b)
    while i>0 and j>0:
        if a[i-1] == b[j-1]:
            res.append(a[i-1])
            i-=1
            j-=1
        else:
            if dp[i][j-1] > dp[i-1][j]:
                j-=1
            else:
                i-=1
    return dp[len(a)][len(b)], res[::-1]

def lis(a,b):
    dp = []
    pos = []
    prev = [-1]*len(a)

    for i,x in enumerate(a):
        left,right = 0,len(dp)

        while left<right:
            mid = (left+right)//2
            if dp[mid]<x:
                left=mid+1
            else:
                right = mid

        j = left
        if j>0:
            prev[i] = pos[j-1]

        if j ==len(dp):
            dp.append(x)
            pos.append(i)
        else:
            dp[j] = x
            pos[j] = i


    ans = []
    if pos:
        p = pos[-1]
        while p!=-1:
            ans.append(a[p])
            p = prev[p]
    return dp,ans[::-1]