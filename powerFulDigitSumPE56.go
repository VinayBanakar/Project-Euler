package main

import (
	"fmt"
	"math"
)

func digitSum(num float64) float64 {
	tmp := num
	var sum float64
	for tmp > 0 {
		remainder := math.Mod(tmp, 10)
		sum += remainder
		tmp = tmp - remainder
		tmp = tmp / 10
	}
	//fmt.Println(num, sum)
	return sum
}

//TODO: When you find time reimpliment this with modular exponentiation.
func main() {
	limit := 100
	var result float64
	result = 0

	for x := limit - 1; x > 0; x-- {
		for y := limit - 1; y > 0; y-- {
			val := float64(math.Pow(float64(x), float64(y)))
			if float64(math.Log10(float64(val))*9) < result {
				break
			}
			sum := digitSum(val)
			if sum > result {
				result = sum
			}
		}
	}
	fmt.Println("Max sum found under a,b < 100 is: ", result)
}
