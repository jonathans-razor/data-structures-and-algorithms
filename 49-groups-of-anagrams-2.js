/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  let map = {};

  for (let str of strs) {
    let frankenString = str.split('').sort().join('');
    if (!map[frankenString]) map[frankenString] = [];
    map[frankenString].push(str);
  }
  return Object.values(map);
};

// Step 1: Parse Command Line Arguments
const args = process.argv.slice(2);

// Step 2: Group Anagrams using the provided function
const groupedAnagrams = groupAnagrams(args);

// Step 3: Display the Result
groupedAnagrams.forEach((group, index) => {
  console.log(`Anagram Group ${index + 1}: ${group.join(', ')}`);
});
