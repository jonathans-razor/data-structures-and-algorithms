package main

import "fmt"

func main() {
    for i := 1; i <= 100; i++ {
        output := ""
        if i%3 == 0 {
            output += "Fizz"
        }
        if i%5 == 0 {
            output += "Buzz"
        }
        if i%7 == 0 {
            output += "Bazz"
        }
        if output == "" {
            fmt.Println(i)
        } else {
            fmt.Println(output)
        }
    }
}
