package main

import (
	"fmt"
)

func sandi_geometri(N int, arr [][]int) int {
	max := -1

	for i := 0; i < N; i++ {
		x1 := arr[i][0]
		y1 := arr[i][1]

		for j := i + 1; j < N; j++ {
			x2 := arr[j][0]
			y2 := arr[j][1]

			if x1 != x2 && y1 != y2 {
				found1 := false
				found2 := false
				for k := 0; k < N; k++ {
					x3 := arr[k][0]
					y3 := arr[k][1]

					if x3 == x1 && y3 == y2 {
						found1 = true
					}

					if x3 == x2 && y3 == y1 {
						found2 = true
					}

					if found1 && found2 {
						break
					}
				}

				if found1 && found2 {
					x := x2 - x1
					y := y2 - y1

					if x < 0 {
						x = -x
					}
					if y < 0 {
						y = -y
					}

					luas := x * y

					if max < luas {
						max = luas
					}
				}
			}
		}
	}

	return max
}

func main() {
	var N int
	fmt.Scan(&N)

	P := make([][]int, N)

	for i := 0; i < N; i++ {
		var x, y int
		fmt.Scan(&x, &y)
		P[i] = []int{x, y}
	}

	fmt.Println(sandi_geometri(N, P))
}