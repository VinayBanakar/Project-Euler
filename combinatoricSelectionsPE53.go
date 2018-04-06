package main

import (
	"fmt"
)

//easy brute force but lets try Binomial coefficient solution (Pascals triangle)
func main() {
	result := 0
	limit := 1000000
	nlimit := 100

	pascalTriangle := make([][]int, nlimit+1)
	for i := range pascalTriangle {
		pascalTriangle[i] = make([]int, nlimit+1)
	}
	for n := 0; n <= nlimit; n++ {
		pascalTriangle[n][0] = 1
	}
	for n := 1; n <= nlimit; n++ {
		for r := 1; r <= n; r++ {
			pascalTriangle[n][r] = pascalTriangle[n-1][r] + pascalTriangle[n-1][r-1]
			if pascalTriangle[n][r] > limit {
				pascalTriangle[n][r] = limit
				//to avoid integer overflow lets just set everything
				//above a million as a million.
				result++
			}
		}
	}

	fmt.Println(pascalTriangle, result)
}
