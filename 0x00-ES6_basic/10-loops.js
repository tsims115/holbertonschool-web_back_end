export default function appendToEachArrayValue(array, appendString) {
  const newList = []
  for (const idx of array) {
    let value = idx;
    value = appendString + idx;
    newList.push(value)
  }

  return newList;
}
