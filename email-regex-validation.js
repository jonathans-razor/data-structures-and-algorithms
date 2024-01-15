/*
Create a JavaScript program that does email regex validation. The program should accept and 
email address as input and output a boolean as to whether the input was a valid email address. 
Automatically pass in the data from the command line.

::Jan-14-2024
*/
const email = process.argv[2];
const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const isValidEmail = regex.test(email);
console.log(isValidEmail);