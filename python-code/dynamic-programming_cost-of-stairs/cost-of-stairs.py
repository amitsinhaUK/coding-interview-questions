#
# Interview question: For a given staircase, the i-th step is assigned a non-negative cost indicated by a cost array.
#                     Once you pay the cost for a step, you can either climb one or two steps. Find the minimum cost to reach the 
#                     top of the staircase. Your first step can either be the first or second step.
#
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#



def _recursive_func(stairs: list, memo: list, step: int):
    print(f"Current step is: {step}")
    
    if step < 0:
        return 0
    elif step == 0:
        return stairs[0]
    elif step == 1:
        return stairs[1]
    elif memo[step] != None:
        return memo[step]
    else:
        one_step = step - 1
        two_step = step - 2
        if (one_step >= 0) and (two_step >= 0):
            memo[step] = stairs[step] + min(_recursive_func(stairs=stairs, memo = memo, step=one_step), _recursive_func(stairs=stairs, memo = memo, step=two_step))
            return memo[step]


def min_cost(stairs: list) -> int:
    
    memoization = [None]*len(stairs)
    return min(_recursive_func(stairs, memoization, len(stairs)-1), _recursive_func(stairs, memoization, len(stairs)-2))


def main():
    stairs = [30, 15, 30, 5]
    print(min_cost(stairs))
    

main()







