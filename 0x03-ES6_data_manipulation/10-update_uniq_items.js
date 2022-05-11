export default function updateUniqueItems(map) {
  if (typeof map !== 'map') {
    throw new Error('Cannot process');
  }
  map.forEach((v, k) => {
    if (v === 1) {
      try {
        map.set(k, 100);
      } catch (e) {
        throw new Error('Cannot process');
      }
    }
  });
}
