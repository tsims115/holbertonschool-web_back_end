export default function updateUniqueItems(map) {
  console.log();
  if (map.constructor.name !== 'Map') {
    throw new Error('Cannot process');
  }
  map.forEach((v, k) => {
    if (v === 1) {
      map.set(k, 100);
    }
  });
}
