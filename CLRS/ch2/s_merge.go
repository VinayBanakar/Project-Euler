package main

import (
	"fmt"
)

func mergeSort(A []int, p, r int) {
	if p < r {
		q := (p + r) / 2
		mergeSort(A, p, q)
		mergeSort(A, q+1, r)
		//merge(A, p, q, r)
		merge2(A, p, r)
	}
}

func merge(A []int, p, q, r int) {
	n1 := q - p + 1
	n2 := r - q
	L := make([]int, n1)
	R := make([]int, n2)

	for i := 0; i < n1; i++ {
		L[i] = A[p+i]
	}
	for j := 0; j < n2; j++ {
		R[j] = A[q+1+j]
	}
	fmt.Println(L, R)
	i, j := 0, 0
	k := p
	for i < n1 && j < n2 {
		if L[i] <= R[j] {
			A[k] = L[i]
			i++
		} else {
			A[k] = R[j]
			j++
		}
		k++
	}
	for i < n1 {
		A[k] = L[i]
		i++
		j++
	}
	for j < n2 {
		A[k] = R[j]
		i++
		j++
	}
}

func merge2(sorted []int, leftStart int, rightEnd int) {
	temp := make([]int, len(sorted))
	copy(temp, sorted)

	leftEnd := (leftStart + rightEnd) / 2
	rightStart := leftEnd + 1

	left := leftStart
	right := rightStart
	index := leftStart

	for left <= leftEnd && right <= rightEnd {
		if sorted[left] < sorted[right] {
			temp[index] = sorted[left]
			left++
		} else {
			temp[index] = sorted[right]
			right++
		}
		index++
	}

	copy(temp[index:rightEnd+1], sorted[right:rightEnd+1])
	copy(temp[index:rightEnd+1], sorted[left:leftEnd+1])
	copy(sorted, temp)
}
