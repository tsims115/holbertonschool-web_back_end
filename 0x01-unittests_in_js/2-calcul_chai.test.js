const assert = require('assert');
const calculateNumber = require('./1-calcul');
const chai = require('chai');
const expect = chai.expect;
describe('calculateNumber', function () {
  describe('SUM', function () {
      it('SUM should return 5 from 1.5 and 2.5', function () {
        expect(calculateNumber("SUM", 1.5, 2.5)).to.equal(5);
      });
      it('SUM should return 4 from 1.2 and 2.7', function () {
        expect(calculateNumber("SUM", 1.2, 2.7)).to.equal(4);
      });
      it('SUM should return 139 from 100.5 and 38.2', function () {
        expect(calculateNumber("SUM", 100.5, 38.2)).to.equal(139);
      });
      it('SUM should return -4 from -1.2 and -3.5', function () {
        expect(calculateNumber("SUM", -1.2, -3.5)).to.equal(-4);
      });
      it('SUM should return -7 from -108.2 and 100.7', function () {
        expect(calculateNumber("SUM", -108.2, 100.7)).to.equal(-7);
      });
  });
  describe('SUBTRACT', function () {
      it('SUBTRACT should return -209 from -108.2 and 100.7', function () {
        expect(calculateNumber("SUBTRACT", -108.2, 100.7)).to.equal(-209);
      });
      it('SUBTRACT should return -4 from 5.3 and 8.9', function () {
        expect(calculateNumber("SUBTRACT", 5.3, 8.9)).to.equal(-4);
      });
      it('SUBTRACT should return -78 from -108.5 and -30', function () {
        expect(calculateNumber("SUBTRACT", -108.5, -30)).to.equal(-78);
      });
  });
  describe('DIVIDE', function () {
      it('DIVIDE should return 2 from 4.4 and 2.1', function () {
        expect(calculateNumber("DIVIDE", 4.4, 2.1)).to.equal(2);
      });
      it('DIVIDE should return 15 from 29.5 and 1.7', function () {
        expect(calculateNumber("DIVIDE", 29.5, 1.7)).to.equal(15);
      });
      it('DIVIDE should return 6.5 from 13 and 2', function () {
        expect(calculateNumber("DIVIDE", 13, 2)).to.equal(6.5);
      });
      it('DIVIDE should return Error from 13 and 0', function () {
        expect(calculateNumber("DIVIDE", 13, 0)).to.equal("Error");
      });
      it('DIVIDE should return 2.5 from 5 and 2', function () {
        expect(calculateNumber("DIVIDE", 5, 2)).to.equal(2.5);
      });
      it('DIVIDE should return 0.2 from 1.4 and 4.5', function () {
        expect(calculateNumber("DIVIDE", 1.4, 4.5)).to.equal(0.2);
      });
  });
});
