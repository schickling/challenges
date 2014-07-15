package main

import (
	"fmt"
	"math"
)

func main() {
	x := 1
	y := 0
	z := 0
	for x < 9 && y < 9 && z < 9 {
		if assemble(x, y, z) == asBase9(assemble(z, y, x)) {
			fmt.Println(x, y, z)
			break
		}
		x++
		condInc(&x, &y)
		condInc(&y, &z)
	}
}

func asBase9(v int) int {
	x := 0
	i := 0
	for v > 0 {
		x += int(math.Pow10(i)) * (v % 9)
		v /= 9
		i++
	}
	return x
}

func assemble(x, y, z int) int {
	return x*100 + y*10 + z
}

func condInc(a, b *int) {
	if *a == 8 {
		*b++
		*a = 0
	}
}
