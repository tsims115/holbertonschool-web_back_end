export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  get size() {
    return this._size;
  }

  set size(size) {
    if (typeof size !== 'number') {
      throw TypeError('size must be a numebr');
    }
    this._size = size;
  }

  get location() {
    return this._location;
  }

  set location(location) {
    if (typeof location !== 'string') {
      throw TypeError('location must be a string');
    }
    this._location = location;
  }

  toString() {
    return this.location;
  }

  valueOf() {
    return this.size;
  }
}
