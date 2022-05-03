export default function appendToEachArrayValue(array, appendString) {
  const newList = []
  let value
  for (const idx of array) {
    value = idx;
    value = appendString + idx;
    newList.push(value)
  }

  return newList;
}
