package main

import (
	"log"
	"math"
)

type partition struct {
	a, b []int
}

func main() {
	x := []int{9, 8, 7, 6, 5, 4, 3, 2, 1}
	y := permutate(x)
	//log.Printf("%v\n", y)
	log.Printf("Start:")
	for _, element := range y {
		log.Printf("%d, %d\n", assemble(element.a), assemble(element.b))
	}
}

func permutate(s []int) []partition {
	a := s
	b := make([]int, 0)
	l := make([]partition, 0)

	for len(a) > 1 {
		log.Printf("%v, %v", a, b)
		for j := 0; j < len(a); j++ {
			aa := without(a, j)
			bb := make([]int, len(b))
			copy(bb, b)
			bb = append(bb, a[j])
			l = append(l, partition{aa, bb})
		}
		b = append(b, a[0])
		a = without(a, 0)
	}

	return l
}

func assemble(s []int) int {
	x := 0
	n := len(s)
	for i := 0; i < n; i++ {
		x += int(math.Pow10(n-i-1)) * s[i]
	}

	return x
}

func without(s []int, i int) []int {
	l := make([]int, 0)
	for k := 0; k < len(s); k++ {
		if k != i {
			l = append(l, s[k])
		}
	}

	return l
}
