export default function appendToEachArrayValue(array, appendString) {
  const newList = []
  for (let idx of array) {
    let value = idx;
    idx = appendString + value;
    newList.push(idx)
  }

  return newList;
}
