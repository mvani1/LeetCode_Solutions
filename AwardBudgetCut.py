'''
Award Budget Cuts
The awards committee of your alma mater (i.e. your college/university) asked for 
your assistance with a budget allocation problem they’re facing. Originally, the
committee planned to give N research grants this year. However, due to spending
cutbacks, the budget was reduced to newBudget dollars and now they need to
reallocate the grants. The committee made a decision that they’d like to impact
as few grant recipients as possible by applying a maximum cap on all grants.
Every grant initially planned to be higher than cap will now be exactly cap dollars.
 Grants less or equal to cap, obviously, won’t be impacted.

Given an array grantsArray of the original grants and the reduced budget newBudget,
write a function findGrantsCap that finds in the most efficient manner a cap such
that the least number of recipients is impacted and that the new budget constraint
is met (i.e. sum of the N reallocated grants equals to newBudget).

Analyze the time and space complexities of your solution.
'''
def find_grants_cap(grantsArray, newBudget):
    '''
    APPROACH 1
        Time Complexity = O(n^2)
        Space Complecity = O(1)
    
    grantsArray.append(0)
    grantsArray.sort(reverse=True)
    n = len(grantsArray)

    for i in range(n):
        maxx = (i+1)*grantsArray[i]
        if maxx <= newBudget and maxx+sum(grantsArray[i+1:]) <=newBudget:
            break
            
    newBudget -= sum(grantsArray[i:])
    new_length = n - len(grantsArray[i:-1]) - 1
    return (float(newBudget)/new_length)
    '''

    '''
    APPROACH 2
        Time Complexity = O(n)
        Space Complexity = O(n)
    '''
    grantsArray.append(0)
    grantsArray.sort(reverse=True)
    n = len(grantsArray)
    right_sum = [0 for _ in range(n)]
    
    for i in range(n-2,-1,-1):
        right_sum[i] = right_sum[i+1]+grantsArray[i+1]

    for i in range(n):
        maxx = (i+1)*grantsArray[i]
        if maxx <= newBudget and maxx+right_sum[i] <=newBudget:
            break
            
    newBudget -= right_sum[i-1]
    new_length = n - len(grantsArray[i:-1]) - 1
    return (float(newBudget)/new_length)
  

print(find_grants_cap([100, 300, 200, 400], 800))                       #250
print(find_grants_cap([2,100,50,120,167], 400))                         #128
print(find_grants_cap([2,100,50,120,1000], 190))                        #47
print(find_grants_cap([21,100,50,120,130,110], 140))                    #23
print(find_grants_cap([210,200,150,193,130,110,209,342,117], 1530))     #211

  