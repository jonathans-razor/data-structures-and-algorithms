// Promput Used: Don't use the strArray.reverse method.
// Check if a command-line argument is provided
if (process.argv.length < 3) {
  console.error("- Parameter mssing. Provide a string to reverse.");
  process.exit(1); // Exit with an error code
}

// Get the string to reverse from the command-line arguments
var inputString = process.argv[2];

function reverseString(str) {
  var reversedStr = '';
  for (var i = str.length - 1; i >= 0; i--) {
    reversedStr += str.charAt(i);
  }
  return reversedStr;
}

console.log(reverseString(inputString));
