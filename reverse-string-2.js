// Prompt Used: I want to pass the string in at the command line.
// Check if a command-line argument is provided
if (process.argv.length < 3) {
  console.error("Please provide a string to reverse.");
  process.exit(1); // Exit with an error code
}

// Get the string to reverse from the command-line arguments
var inputString = process.argv[2];

function reverseString(str) {
  // Split the string into an array of characters
  var strArray = str.split('');

  // Reverse the array
  var reversedArray = strArray.reverse();

  // Join the array back into a string
  var reversedStr = reversedArray.join('');

  return reversedStr;
}

var reversedString = reverseString(inputString);
console.log("Original: " + inputString);
console.log("Reversed: " + reversedString);