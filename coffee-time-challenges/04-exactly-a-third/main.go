package main

import (
	"fmt"

	"github.com/fighterlyt/permutation"
)

func main() {

	digits := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 'x'}

	permutation, err := permutation.NewPerm(digits, nil)
	if err != nil {
		fmt.Println(err)
		return
	}

	for s, err := permutation.Next(); err == nil; s, err = permutation.Next() {

		permutatedDigits := s.([]int)
		a, b := 0, 0
		beforeMark := true

		// optimization: permutation not possible since denominator has to be 4 digits long
		if permutatedDigits[4] != 'x' {
			continue
		}

		for i := 0; i < 10; i++ {

			if i == 4 {
				beforeMark = false
			} else {
				if beforeMark {
					a = a*10 + permutatedDigits[i]
				} else {
					b = b*10 + permutatedDigits[i]
				}
			}

		}

		if a > 0 && b > 0 && float32(b)/float32(a) == 3 {
			fmt.Println(a, b)
		}

	}

}
