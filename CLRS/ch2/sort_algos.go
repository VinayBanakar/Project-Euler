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

	fmt.Printf("SIZE ======== %v\n", SIZE)
	fmt.Printf("Insertion\t %dms\n", elapsedI.Nanoseconds()/1000)
	fmt.Printf("Selection\t %dms\n", elapsedS.Nanoseconds()/1000)
	fmt.Printf("Merge\t\t %dms\n", elapsedM.Nanoseconds()/1000)
	fmt.Printf("Bubble\t\t %dms\n", elapsedB.Nanoseconds()/1000)
}
