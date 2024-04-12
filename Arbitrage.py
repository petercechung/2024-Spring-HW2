liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

import math
import itertools
def uniswap(x, y, dx):
    return .997*dx*y/(x+.997*dx)
keyss = liquidity.keys()
keys = list(keyss)
for a, b in keys:
    x,y = liquidity[(a,b)]
    liquidity[(b,a)] = y,x
    
tokenset = set()
for tup in liquidity.keys():
    tokenset.update(tup)
    #tokenset.update(tupr)
liquidity.values()
vertexs = list(tokenset)
dis = dict(zip(vertexs,[1000000]*len(vertexs)))
n = len(vertexs)
paths = list(itertools.permutations(vertexs))
best = 20
for patht in paths:
    pathl = list(patht)
    if pathl[0]!="tokenB":
        continue
    for j in range(2, n+1):
        path = pathl[0:j]
        path.append("tokenB")
        amount = 5  
        for i in range(j):
            now = path[i]
            next = path[i+1]
            amount = uniswap(liquidity[(now,next)][0], liquidity[(now,next)][1], amount)
 
        if amount > best:
            bestpath = path
            best = amount
            amountIn = 5
            for i in range(j):
                now = path[i]
                next = path[i+1]
                amountOut = uniswap(liquidity[(now,next)][0], liquidity[(now,next)][1], amountIn)
                # print("In swap ({}, {}), amountIn = {}, amountOut = {}".format(now, next, amountIn, amountOut))
                amountIn = amountOut

def printpath(path, balance):
    print("path: ", end="")
    n = len(path)
    for i in path[0:-1]:
        print("{}->".format(i), end="")
    print("{}, {} balance={}".format(path[-1],path[-1],balance))
printpath(bestpath, best)