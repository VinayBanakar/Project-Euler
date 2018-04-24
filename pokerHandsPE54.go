package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}


func didPlayerOneWin(hand1 string[], hand2 string[]) bool
{
	if royalFlush(hand1) > royalFlush(hand2) {return true}
	if straightFlush(hand1) > straightFlush(hand2) {return true}
	if fourOfaKind(hand1) > fourOfaKind(hand2) {return true}
	if fullHouse(hand1) > fullHouse(hand2) {return true}
	if flush(hand1) > flush(hand2) {return true}
	if straight(hand1) > straight(hand2) {return true}
	if threeOfaKind(hand1) > threeOfaKind(hand2) {return true}
	if twoPair(hand1) > twoPair(hand2) {return true}
	if onePair(hand1) > onePair(hand2) {return true}
	if hightCard(hand1, hand2) == "player1" {return true}
	
	return false
}


func main() {

	file, err := os.Open("./p054_poker.txt")
	check(err)
	defer file.Close()
	playerOneCount := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		r := regexp.MustCompile("[^\\s]+")
		fmt.Print(r.FindAllString(scanner.Text(), -1)[:5])
		fmt.Print(" vs ")
		fmt.Print(r.FindAllString(scanner.Text(), -1)[5:])
		if didPlayerOneWin(r.FindAllString(scanner.Text(), -1)[:5], r.FindAllString(scanner.Text(), -1)[5:]) {playerOneCount++}
	}
	fmt.Println("Player 1 won: "+ playerOneCount)
}
