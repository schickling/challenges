package main

import "fmt"

func main() {
	x := 1
	for {
		r := 1000000 % x
		if r == 0 {
			y := 1000000 / x
			if x%10 != 0 && y%10 != 0 {
				fmt.Println(x, y)
				break
			}
		}
		x++

	}
}
