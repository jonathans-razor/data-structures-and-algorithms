package main

import (
	"fmt"
	"os"
)

func reverseString(str string) string {
	result := ""
	for i := len(str) - 1; i >= 0; i-- {
		result += string(str[i])
	}
	return result
}

func main() {
	args := os.Args[1:]
	if len(args) == 0 {
		fmt.Println("Usage: reverse <string>")
		return
	}

	str := args[0]
	fmt.Println(reverseString(str))
}
