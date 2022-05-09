export default class Building {
  constructor(sqft) {
    this.sqft = sqft;
    if (this.constructor.name !== 'Building' && this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(sqft) {
    this._sqft = sqft;
  }
}
