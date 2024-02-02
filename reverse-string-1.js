// Prompt used: Create a javascript program that reverses a string.
function reverseString(str) {
  // Split the string into an array of characters
  var strArray = str.split('');

  // Reverse the array
  var reversedArray = strArray.reverse();

  // Join the array back into a string
  var reversedStr = reversedArray.join('');

  return reversedStr;
}

// Example usage
var originalString = "Hello, World!";
var reversedString = reverseString(originalString);

console.log("Original: " + originalString);
console.log("Reversed: " + reversedString);
