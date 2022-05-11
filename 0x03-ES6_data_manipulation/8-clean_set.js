export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  let words = [...set].filter((s) => s.includes(startString, 0));
  words = words.map((s) => s.slice(startString.length));
  return words.join('-');
}
