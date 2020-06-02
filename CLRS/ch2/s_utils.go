package main

import (
	"math/rand"
)

// Generates an array of random numbers
func GenPrngArray(size int) []int {
	a_rand := make([]int, size)
	for i := 0; i < size; i++ {
		a_rand[i] = rand.Intn(10000)
	}
	return a_rand
}
