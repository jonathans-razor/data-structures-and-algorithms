package main

import (
	"flag"
	"fmt"
	"math/rand"
	"time"
)

const (
	letterBytes        = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digitBytes         = "0123456789"
	specialCharBytes   = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
	defaultPasswordLen = 12
)

var (
	length              int
	includeDigits       bool
	includeSpecialChars bool
)

func init() {
	flag.IntVar(&length, "length", defaultPasswordLen, "Length of the password")
	flag.BoolVar(&includeDigits, "include-digits", true, "Include digits in the password")
	flag.BoolVar(&includeSpecialChars, "include-special-chars", true, "Include special characters in the password")
	flag.Parse()

	rand.Seed(time.Now().UnixNano())
}

func generatePassword(length int, includeDigits bool, includeSpecialChars bool) string {
	characters := letterBytes
	if includeDigits {
		characters += digitBytes
	}
	if includeSpecialChars {
		characters += specialCharBytes
	}

	password := make([]byte, length)
	for i := range password {
		password[i] = characters[rand.Intn(len(characters))]
	}

	return string(password)
}

func main() {
	password := generatePassword(length, includeDigits, includeSpecialChars)
	fmt.Println("Generated Password:", password)
}
