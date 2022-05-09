/* eslint-disable no-unused-vars */
import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(amount) {
    if (typeof amount !== 'number') {
      throw TypeError('amount must be a number');
    }
    this._amount = amount;
  }

  get currency() {
    return this._currency;
  }

  set currency(currency) {
    if (currency.constructor.name !== 'Currency') {
      throw TypeError('currency must be a Currency');
    }
    this._currency = currency;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw TypeError('amount must be a number');
    }
    if (typeof conversionRate !== 'number') {
      throw TypeError('conversionRate must be a number');
    }
    return amount * conversionRate;
  }
}
