# Hackerrank Scrachpad
# Solutions from various hackerrank.com exercises.

import numpy as np
import math as math

def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = 0
    for i in range(len(candles)):
        if(candles[i] == tallest):
            count += 1
    print(count)

###########################################

def miniMaxSum(arr):
    n = len(arr)
    arr_max = max(arr)
    arr_min = min(arr)
    max_sum = sum(arr) - arr_min
    min_sum = sum(arr) - arr_max
    print(str(max_sum) + " " + str(min_sum))	

###########################################

def staircase(n):
	ans = ""
	m = 1
	
	for i in range(n):	
		for j in range(n-m):
			ans += " "
		for k in range(m):
			ans += "#"
		print(ans + "\n")
		ans = ""
		m += 1

###########################################

def timeConversion(s):
	if(s[-2] == 'A'):
		s = s.split('A')
		s = s[0].split(':')
		if(int(s[0]) == 12):
			s[0] = '00' 
		s = (s[0] + ':' + s[1] + ':' + s[2])
		print(s)
		
	else:
		s = s.split('P')
		s = s[0].split(':')
		if(s[0] == '12'):
			s = (s[0] + ':' + s[1] + ':' + s[2])
		else:
			hr = int(s[0]) + 12
			s[0] = str(hr)
			s = (s[0] + ':' + s[1] + ':' + s[2])
		print(s)		

###########################################

# Failing a couple test cases...
def candies(n, arr):
    candies_total = n
    extra = 0
    
    for i in range(1, n):
        if arr[i-1] < arr[i]:
            extra += 1
        else:
            extra = 0
        candies_total += extra
    return candies_total         

###########################################
    
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_hits = 0
    orange_hits = 0
    
    for i in range(len(apples)):
        if((apples[i] + a) in range(s, t + 1)):
            apple_hits += 1
        
    for i in range(len(oranges)):
        if((b + oranges[i]) in range(s, t + 1)):
            orange_hits += 1
    
    print(apple_hits)
    print(orange_hits)    

###########################################    
    
def kangaroo(x1, v1, x2, v2):
    ans = "NO"
    for i in range(1, 1000000):
        if((x2 + (v2*i)) == (x1 + (v1*i))):
            ans = "YES"
                
    return ans

###########################################
# Return to this one, still not working.
def getTotalX(a, b):
    x = range(a[-1], b[0])
    print(x)    
    a_facts = []
    b_facts = []
    ans = 0
    for i in range(a[-1], b[0]):
        for j in range(len(a)):
            if i % a[j] == 0:
                a_facts.append([i])
    
    for i in range(a[-1], b[0]):
        for k in range(len(b)):
            if b[k] % i== 0:
                b_facts.append([i])

    for i in a_facts:
        for j in b_facts:
            if i == j:
                print(i, j)
                ans += 1
    print(ans)            
    return ans


#a = [2, 4]
#b = [16, 32, 96]
#getTotalX(a, b)

###########################################
# New Years Chaos
# This works locally, not on HR.com :(
def minimumBribes(q):

    bribes_total = 0
    chaos = False
    q_sorted = sorted(q)

    for i in range(len(q)):
        bribes_turn = 0
        if(q[i] > q_sorted[i]):
            while(q[i] > q_sorted[i+bribes_turn]):            
                bribes_turn += 1
                #bribes_turn = q[i] - q_sorted[i]
                if(q[i] > q_sorted[i + bribes_turn]):            
                    bribes_total += bribes_turn
                            
                if(bribes_turn > 2):
                    chaos = True
        
    if(chaos):
        print("Too chaotic")
    else:
        print(bribes_total)
    


#q = [1, 2, 5, 3, 7, 8, 6, 4]
#minimumBribes(q)
	
###########################################
# Gaming Array

def gamingArray(arr):
    max_val = 0
    even = True
    for i in arr:
        if i > max_val:
            even = not even
            max_val = i
    if(even):
        return "ANDY"
    else:
        return "BOB"


###########################################


def bonAppetit(bill, k, b):
    bill[k] = 0;
    bill = sum(bill) / 2    
    anna = b - bill
    if anna > 0:
        print(int(anna))
    else:
        print("Bon Appetit")


###########################################


def sockMerchant(n, ar):
    arranged = []
    pairs = 0
    for i in ar:
        if i not in arranged:
            arranged.append(i)
    print(arranged)

    for i in arranged:
        print("i = " + str(i))
        count = 0
        for j in ar:
            if j == i:
                ar.remove(j)
                count += 1
                print(ar)
        pairs += (count/2) - (count % 2)
        print(pairs)
    print(pairs)            


#ar = [1,2,1,2,1,3,2]
#sockMerchant(len(ar), ar)

#ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
#sockMerchant(len(ar), ar)


###########################################

# n = page length
# p = target page

def pageCount(n, p):
    flip_count = 0    
    
    if (n > 2) and (n % 2 == 0) and (n - p) == 1:    
        flip_count = 1

    elif p > (n/2):
        a = (n-p)/2
        flip_count = math.floor(a)
        
    else:
        a = p/2
        flip_count = math.floor(a) 
        
    print(flip_count)


#pageCount(6, 2)   
#pageCount(96993, 70030) 
# expected ans: flip_count = 13481
#pageCount(6, 5)
# expected ans: flip_count = 1


###########################################


def countingValleys(steps, path):
    level = 0
    valleys = 0
    for i in range(0, steps):
        if path[i] == 'D':
            level = level - 1
        if path[i] == 'U':
            level += 1
        if (i > 2) and path[i-1] == "U" and (level == 0):
            valleys += 1
            print("valleys = " + str(valleys))
        #print(level)
    print(valleys)
    return valleys


countingValleys(8, "UDDDUDUU")
countingValleys(12, "DDUUDDUDUUUD")



###########################################


def getMoneySpent(keyboards, drives, b):
    cost = 0
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if (keyboards[i] + drives[j]) <= b and (keyboards[i] + drives[j]) > cost):
                cost = keyboards[i] + drives[j]
    if cost == 0:
        return -1
    else:
        return cost










