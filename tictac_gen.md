# tictac_gen(n=3, d=2, coords=True)

The generator of all possible winning templates for TicTac game on *d*-dimentional field *n*×..×*n*. 

For example for *n*=2, *d*=2 there are 6 possibilities:

1. 1 0  
1 0
1. 0 1  
0 1
1. 1 1  
0 0
1. 0 0  
1 1
1. 1 0  
0 1
1. 0 1  
1 0

In the classical case *n*=3, *d*=2 there are 8 possibilities:

1. 1 0 0  
1 0 0  
1 0 0  
1. 0 1 0  
0 1 0  
0 1 0  
1. 0 0 1  
0 0 1  
0 0 1  
1. 1 1 1  
0 0 0  
0 0 0  
1. 0 0 0  
1 1 1  
0 0 0  
1. 0 0 0  
0 0 0  
1 1 1  
1. 1 0 0  
0 1 0  
0 0 1  
1. 0 0 1  
0 1 0  
1 0 0  

In general case the total number of possible positions is given by the formula (cf. [Sloane A102728](https://oeis.org/A102728)):

![\frac{(n+2)^d - n^d}{2}](https://latex.codecogs.com/svg.latex?\frac{(n&plus;2)^d-n^d}{2})

By default the generator returns an *n*×*d*-array with coordinates of ones. To generate 0,1-matrices use `coords=False`.
