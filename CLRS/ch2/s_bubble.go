package main

func bubble(A []int) {
	n, tmp := len(A), 0
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-i-1; j++ {
			if A[j] > A[j+1] {
				tmp = A[j]
				A[j] = A[j+1]
				A[j+1] = tmp
			}
		}
	}
}
