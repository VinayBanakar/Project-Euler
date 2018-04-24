package main

import (
	"fmt"
	"math"
)

// To calculate N/D for square root of 2, these below principals hold strong:
//	* N(k+1) = N(k) + 2D(k)
// 	* D(k+1) = N(k) + D(k)
func main() {
	limit := 1000
	total := 0
	nume := int64(3)
	deno := int64(2)

	for i := 1; i < limit; i++ {
		nume += 2 * deno
		deno = nume - deno // D(k+1) = N(k+1) - D(k)
		fmt.Println("Num: ", nume, "Den: ", deno)
		if int(math.Log10(float64(nume))) > int(math.Log10(float64(deno))) {
			total++
		}
	}
	fmt.Println("Total number of numerators bigger in number than denomenator of root 2: ", total)
}

//GO IS THE WORST FOR NUMBER CRUNCHING!!!!!!!!!!
// Integer is overflowing at different stages causing inconsistencies in answers.
// func main() {
// 	limit := 1000
// 	total := 0
// 	nume := big.NewInt(3)
// 	deno := big.NewInt(2)

// 	for i := 1; i < limit; i++ {
// 		nume.Add(nume, deno.Mul(deno, big.NewInt(2)))
// 		deno.Sub(nume, deno) // D(k+1) = N(k+1) - D(k)
// 		if int(Pow(10*nume.Int64())) > int(Pow(10*deno.Int64())) {
// 			total++
// 		}
// 	}
// 	fmt.Println("Total number of numerators bigger in number than denomenator of root 2: ", total)
// }
