package main

import (
	"fmt"
)

func reverseNum(num int) int {
	rev_num := 0
	for num > 0 {
		remainder := num % 10
		rev_num *= 10
		rev_num += remainder
		num /= 10
	}
	return rev_num
}

func isPalindrome(num int) bool {
	tmp := num
	if num == reverseNum(tmp) {
		return true
	}
	return false
}

func main() {
	limit := 100
	lychSum := 0
	notLychrel := 0
	track := false
	for n := 11; n <= limit; n++ {
		iter := 1
		sum := n + reverseNum(n)
		for iter <= 49 {
			fmt.Println(sum)
			if isPalindrome(sum) {
				fmt.Println("-----", sum, iter, n)
				track = true
				notLychrel++
				break
			}
			sum += reverseNum(sum)
			iter++
		}
		if !track {
			fmt.Println(n)
			lychSum += n
		}
	}
	fmt.Print("Total Lychrel numbers bellow 10k: ")
	fmt.Print(100-notLychrel, lychSum)
}
