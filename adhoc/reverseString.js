//  Various Approaches to reversing a string
// ===============================================

function reverse_string(word) {
  let reversed = new Array(word.length);
  let idx = word.length - 1;

  for (let letter of word) {
    reversed[idx] = letter;
    idx -= 1;
  }

  return reversed.join('');
}

// ===============================================

function reverseString2(word) {
  return word.split('').reverse().join('');
}

// ===============================================

function reverseString3(word) {
  let reversed = '';

  for (let letter of word) {
    reversed = letter + reversed;
  }

  return reversed;
}

// ===============================================

function reverseString4(word) {
  return word.split('').reduce((reversed, character) => {
    return character + reversed;
  }, '');
}

console.log(reverseString4('apple'));

// ===============================================

function reverseString_HR(word) {
  let chars = word.split('');

  function reverseString_helper(chars) {
    if (chars.length === 1) return chars.pop();

    const letter = chars.pop();

    return letter.concat(reverseString_helper(chars));
  }

  console.log(reverseString_helper(chars));
}

// ===============================================

function reverseString_R() {}
