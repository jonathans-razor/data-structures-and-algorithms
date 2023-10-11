#!/usr/bin/env node

// Step 1: Parse Command Line Arguments
const args = process.argv.slice(2);

// Step 2: Group Anagrams
function groupAnagrams(strings) {
  const anagramGroups = new Map();

  for (const str of strings) {
    // Sort the characters in the string to create a unique key for anagrams
    const sortedStr = str.split('').sort().join('');
    
    if (anagramGroups.has(sortedStr)) {
      anagramGroups.get(sortedStr).push(str);
    } else {
      anagramGroups.set(sortedStr, [str]);
    }
  }

  return Array.from(anagramGroups.values());
}

const groupedAnagrams = groupAnagrams(args);

// Step 3: Display the Result
groupedAnagrams.forEach((group, index) => {
  console.log(`Anagram Group ${index + 1}: ${group.join(', ')}`);
});