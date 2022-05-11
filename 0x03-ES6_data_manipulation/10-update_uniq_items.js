export default function updateUniqueItems(map) {
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
