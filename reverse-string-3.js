function reverseString(str) {
    return str.split("").reverse().join("");
}
var inputString = process.argv[2];
var reversedString = reverseString(inputString);
console.log("The reversed string of \"" + inputString + "\" is \"" + reversedString + "\".");
