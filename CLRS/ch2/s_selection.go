package main

func selection(A []int) {
	var i_min, tmp int
	for i := 0; i < len(A)-1; i++ {
		i_min = i
		for j := i + 1; j < len(A)-1; j++ {
			if A[j] < A[i_min] {
				i_min = j
			}
		}
		if i_min != i {
			tmp = A[i_min]
			A[i_min] = A[i]
			A[i] = tmp
		}
	}
}
