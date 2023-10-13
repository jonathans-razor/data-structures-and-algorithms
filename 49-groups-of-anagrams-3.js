/**
 * @param {string[]} strings
 * @return {string[][]}
 */
var groupAnagrams = function (strings) {
  let map = {};
  for (let str of strings) {
    let frankenString = str.split('').sort().join('');
    if (!map[frankenString]) map[frankenString] = [];
    map[frankenString].push(str);
  }
  return Object.values(map);
};

// Step 1: Parse command line arguments.
const commandLineArguments = process.argv.slice(2);

// Step 2: Group Anagrams using the provided function.
const groupedAnagrams = groupAnagrams(commandLineArguments);

// Step 3: Display the results.
groupedAnagrams.forEach((group, index) => {
  console.log(`Anagram Group ${index + 1}: ${group.join(', ')}`);
});
