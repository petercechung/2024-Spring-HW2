# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

> Profitalbe path: tokenB->tokenA->tokenD->tokenC->tokenB.
In swap (tokenB, tokenA), amountIn = 5, amountOut = 5.655321988655323.
In swap (tokenA, tokenD), amountIn = 5.655321988655323, amountOut = 2.458781317097934.
In swap (tokenD, tokenC), amountIn = 2.458781317097934, amountOut = 5.0889272933015155.
In swap (tokenC, tokenB), amountIn = 5.0889272933015155, amountOut = 20.129888944077447, tokenB balance=20.129888944077447.
final reward (tokenB balance)=20.129888944077447.

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
The difference between the expected price and the actual price of a trade rimarily caused by volatility and other factors like the size of the trade and the speed of the chain.
 While slippage is unavoidable, it can be minimized through Slippage tolerance. The function is to limit the maximum price change.


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

> It can ensure there is enough liqidity  for further trading, and prevent malicious minting. In the initial liquidity minting, if there is no minimum liquidity amount, users may manipulate the system by adding very small liquidity, then they can receive a large amount of the liquidity provider(LP) tokens.  We can prevent LP tokens from being too inflated by subtracting a minimum liquidity amount.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
The specific formula is
$$ x * y = k$$
Which $x, y$ is the two token balances of the pool respectively, $k$ is a constant value. This formula can mantain liqidity and reflect the price fluctuations of market without using order books, acheiving the goal of decentralization.


## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
In a sandwich attack, the attacker detects your buy transaction and buy before you. The price will rise after buying, so the attacker then sell at higt price to get profits. If you trade get squzzed by the sandwich attack, you may end up paying a higher and manipulated price.
