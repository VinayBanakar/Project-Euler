package main

import (
	"fmt"
	"sort"
	"strconv"
)

func StringToRuneSlice(s string) []rune {
	var r []rune
	for _, runeValue := range s {
		r = append(r, runeValue)
	}
	return r
}

func SortStringByCharacter(s string) string {
	r := StringToRuneSlice(s)
	sort.Slice(r, func(i, j int) bool {
		return r[i] < r[j]
	})
	return string(r)
}

func sortDigits(num int) int {
	tmp := strconv.Itoa(num)
	tmp = SortStringByCharacter(tmp)
	k, err := strconv.Atoi(tmp)
	if err != nil {
		fmt.Println(err)
	}
	return k
}

func main() {
	num := 10
	for true {
		tmp := sortDigits(num)
		if tmp == sortDigits(num*2) && tmp == sortDigits(num*3) && tmp == sortDigits(num*4) && tmp == sortDigits(num*5) && tmp == sortDigits(num*6) {
			fmt.Println(num)
			break
		} else {
			num++
		}
	}
}
