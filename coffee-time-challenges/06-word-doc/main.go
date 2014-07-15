package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	start, end := 1, 10000

	str := ""
	for i := start; i < end+1; i++ {
		str += fmt.Sprintf("%d ", i)
	}
	parts := strings.Split(strings.Replace(str, "0", " ", -1), " ")
	sum := sum(parts)
	fmt.Println(sum)
}

func sum(slice []string) (sum int) {
	for _, v := range slice {
		i, _ := strconv.Atoi(v)
		sum += i
	}
	return sum
}
