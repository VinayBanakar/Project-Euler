package main

import (
	"fmt"
	"os"
	"strconv"
	"time"
)

func main() {
	SIZE, _ := strconv.Atoi(os.Args[1])
	a := GenPrngArray(SIZE)

	slcS, slcI, slcM, slcB := make([]int, len(a)), make([]int, len(a)),
		make([]int, len(a)), make([]int, len(a))

	copy(slcS, a)
	startI := time.Now()
	insertion(slcS)
	elapsedI := time.Since(startI)

	copy(slcI, a)
	startS := time.Now()
	selection(slcI)
	elapsedS := time.Since(startS)

	copy(slcM, a)
	startM := time.Now()
	mergeSort(slcM, 0, len(slcM)-1)
	elapsedM := time.Since(startM)

	copy(slcB, a)
	startB := time.Now()
	bubble(slcB)
	elapsedB := time.Since(startB)

	fmt.Printf("SIZE ======= %v\n", SIZE)
	fmt.Printf("Insertion\t %dns\n", elapsedI.Nanoseconds())
	fmt.Printf("Selection\t %dns\n", elapsedS.Nanoseconds())
	fmt.Printf("Merge\t\t %dns\n", elapsedM.Nanoseconds())
	fmt.Printf("Bubble\t\t %dns\n", elapsedB.Nanoseconds())
}
