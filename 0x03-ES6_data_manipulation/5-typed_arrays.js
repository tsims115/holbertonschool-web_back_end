export default function createInt8TypedArray(length, position, value) {
  try {
    const buffer = new ArrayBuffer(length);
    const view = new DataView(buffer, 0, length);
    view.setInt8(position, value);
    return view;
  } catch (e) {
    throw new Error('Position outside range');
  }
}
