#a = [[1,2,3,4],[4,5,6,5],[7,8,9,6],[0,2,3,4]]
#   
#def indexing(a):
#    sol1 = [] 
#    for i in range(0,len(a)):
#        sol1.append(a[i][i])
#    print(sum(sol1))
#    sol2 = []
#    for j in range(0,len(a)):
#        sol2.append(a[::-1][j][j])
#    print(sum(sol2))
#    return abs(sum(sol1)-sum(sol2))               
#print(indexing(a))
#arr = [256741038,623958417,467905213,714532089,938071625]
#print(arr+arr)    
#def minmaxsum(arr):
#    narr = arr + arr
#    cumm = [] 
#    for i in range(len(arr)):
#        cumm.append(sum(narr[1:5]))
#        narr.pop(0)
#        print(narr)
#    return min(cumm),max(cumm) 
#print(minmaxsum(arr))

#grades = [73,67,38,36,29]

#def graderounder(grades):
#       for i in grades:
#          for j in range(5,101,5):
#              if abs(i-j) < 3 and 35 < i < j:
#                  grades[grades.index(i)] = j
#                  b = ["Passed" if i>=40 else "failed" for i in grades ]          
#       return grades,b
#          
#        
#print(graderounder(grades))       
   
