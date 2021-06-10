/**
 * @param {string[]} words
 * @return {number}
 */
var longestStrChain = function(words) {
    let cache = {};
    words.sort((a,b)=>a.length - b.length);
    let max =0;
    for(let word of words)
    {
        let longest = 0;
        for (let i = 0;i<word.length;i++){
            let subWord = word.slice(0,i) + word.slice(i+1);
            longest = Math.max(longest,(cache[subWord] || 0)+1);
        }
        cache[word] = longest ;
        max = Math.max(max,longest);
    
    }
    return max
};