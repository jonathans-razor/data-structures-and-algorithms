/*

383. Ransom Note

Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

*/

/**
 * Determines if ransomNote can be constructed from magazine.
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
const canConstruct = (ransomNote, magazine) => {
    // Initialize an array to store the counts of each character (26 letters for English)
    const count = new Array(26).fill(0);

    // Count the occurrences of each character in the magazine
    for (const char of magazine) {
        count[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }

    // Check if we can construct the ransomNote
    for (const char of ransomNote) {
        const index = char.charCodeAt(0) - 'a'.charCodeAt(0);
        if (count[index] === 0) {
            return false; // Not enough occurrences of this character
        }
        count[index]--;
    }

    return true;
};

// Get command-line arguments
const [_, __, ransomNote, magazine] = process.argv;

// Call the canConstruct function
console.log(canConstruct(ransomNote, magazine));
