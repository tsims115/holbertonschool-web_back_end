export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }
  let words = [...set].filter((s) => s.startsWith(startString));
  words = words.map((s) => s.slice(startString.length));
  return words.join('-');
}
