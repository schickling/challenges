package main

import (
	"fmt"
	"sort"
)

func main() {
	// Idea: the product will be max. if the factors are max. To achieve this,
	// we ensure that the factors will be as big as possible, but in a balanced way.
	digits := []int{9, 8, 7, 6, 5, 4, 3, 2, 1, 0}
	x, y := 0, 0

	sort.Sort(sort.Reverse(sort.IntSlice(digits)))
	for len(digits) > 0 {
		digit := digits[0]
		digits = digits[1:]
		if x < y {
			x = x*10 + digit
		} else {
			y = y*10 + digit
		}
	}

	fmt.Printf("%d * %d = %d\n", x, y, x*y)
}
