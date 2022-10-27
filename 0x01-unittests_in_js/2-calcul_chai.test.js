const assert = require('assert');
const calculateNumber = require('./1-calcul');
const chai = require('chai');
const expect = chai.expect;
describe('calculateNumber', function () {
  it('Testing positive numbers and non-capital letters', () => {
		expect(calculateNumber('SUM', 2, 2)).to.equal(4);
		expect(calculateNumber('SUM', 1.5, 1.5)).to.equal(4);
		expect(calculateNumber('SUM', 1.5, 2)).to.equal(4);
		expect(calculateNumber('SUM', 2, 1.5)).to.equal(4);
	});
	it('Testing negative numbers and non-capital letters', () => {
		expect(calculateNumber('SUM', -2, -2)).to.equal(-4);
		expect(calculateNumber('SUM', -2.5, -2.5)).to.equal(-4);
		expect(calculateNumber('SUM', -2.5, -2)).to.equal(-4);
		expect(calculateNumber('SUM', -2, -2.5)).to.equal(-4);
	});
	it('Testing errors', () => {
		expect(calculateNumber('DIVIDE', 2, 0)).to.equal('Error');
	});
});
