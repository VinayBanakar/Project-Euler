package main

import (
	"fmt"
)

const (
	MaxInt = int(^uint(0) >> 1) //Max int value in go
)

//Solution inspired from mathblog
func get5digitPaterns() [][]int {
	val := [][]int{
		[]int{1, 0, 0, 0, 1},
		[]int{0, 1, 0, 0, 1},
		[]int{0, 0, 1, 0, 1},
		[]int{0, 0, 0, 1, 1}}
	return val
}

func get6digitPaterns() [][]int {
	val := [][]int{
		[]int{1, 1, 0, 0, 0, 1},
		[]int{1, 0, 1, 0, 0, 1},
		[]int{1, 0, 0, 1, 0, 1},
		[]int{1, 0, 0, 0, 1, 1},
		[]int{0, 1, 1, 0, 0, 1},
		[]int{0, 1, 0, 1, 0, 1},
		[]int{0, 1, 0, 0, 1, 1},
		[]int{0, 0, 1, 1, 0, 1},
		[]int{0, 0, 1, 0, 1, 1},
		[]int{0, 0, 0, 1, 1, 1}}
	return val
}

func fillPattern(pattern []int, number int) []int {
	filledPattern := make([]int, len(pattern)) //wierdGo: have to use slice for dynamic values
	temp := number
	for i := len(filledPattern) - 1; 0 <= i; i-- {
		if pattern[i] == 1 {
			filledPattern[i] = temp % 10
			temp /= 10
		} else {
			filledPattern[i] = -1
		}
	}
	return filledPattern
}

func generateNumber(repNumber int, filledPattern []int) int {
	temp := 0
	for i := 0; i < len(filledPattern); i++ {
		temp = temp * 10
		if filledPattern[i] == -1 {
			temp += repNumber
		} else {
			temp += filledPattern[i]
		}
	}
	return temp
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	if n < 9 {
		return true
	}
	if n%3 == 0 {
		return false
	}

	counter := 5
	for counter*counter <= n {
		if n%counter == 0 {
			return false
		}
		if n%(counter+2) == 0 {
			return false
		}
		counter += 6
	}
	return true
}

func familySize(repeatingNumber int, pattern []int) int {
	familySize := 1
	for i := repeatingNumber + 1; i < 10; i++ {
		if isPrime(generateNumber(i, pattern)) {
			familySize++
		}
	}
	return familySize
}

func main() {
	fiveDigitPattern := get5digitPaterns()
	sixDigitPattern := get6digitPaterns()
	result := MaxInt
	for i := 11; i < 1000; i += 2 {
		if i%5 == 0 {
			continue
		}
		var patterns [][]int
		if i < 100 {
			patterns = fiveDigitPattern
		} else {
			patterns = sixDigitPattern
		}
		for j := 0; j < len(patterns); j++ {
			for k := 0; k <= 2; k++ {
				if patterns[j][0] == 0 && k == 0 {
					continue
				}
				pattern := fillPattern(patterns[j], i)
				candidate := generateNumber(k, pattern)
				if candidate < result && isPrime(candidate) {
					if familySize(k, pattern) == 8 {
						result = candidate
						fmt.Println(result)
						break
					}
				}
			}
		}
	}
}
