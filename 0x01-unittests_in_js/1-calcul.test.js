const assert = require('assert');
const calculateNumber = require('./1-calcul');
describe('calculateNumber', function () {
  it('SUM should return 5 from 1.5 and 2.5', function () {
      assert.equal(calculateNumber("SUM", 1.5, 2.5), 5);
  });
  it('SUM should return 4 from 1.2 and 2.7', function () {
    assert.equal(calculateNumber("SUM", 1.2, 2.7), 4);
  });
  it('SUM should return 139 from 100.5 and 38.2', function () {
    assert.equal(calculateNumber("SUM", 100.5, 38.2), 139);
  });
  it('SUM should return -4 from -1.2 and -3.5', function () {
    assert.equal(calculateNumber("SUM", -1.2, -3.5), -4);
  });
  it('SUM should return -7 from -108.2 and 100.7', function () {
    assert.equal(calculateNumber("SUM", -108.2, 100.7), -7);
  });
  it('SUBTRACT should return -209 from -108.2 and 100.7', function () {
    assert.equal(calculateNumber("SUBTRACT", -108.2, 100.7), -209);
  });
  it('SUBTRACT should return -4 from 5.3 and 8.9', function () {
    assert.equal(calculateNumber("SUBTRACT", 5.3, 8.9), -4);
  });
  it('SUBTRACT should return -78 from -108.5 and -30', function () {
    assert.equal(calculateNumber("SUBTRACT", -108.5, -30), -78);
  });
  it('DIVIDE should return 2 from 4.4 and 2.1', function () {
    assert.equal(calculateNumber("DIVIDE", 4.4, 2.1), 2);
  });
  it('DIVIDE should return 15 from 29.5 and 1.7', function () {
    assert.equal(calculateNumber("DIVIDE", 29.5, 1.7), 15);
  });
  it('DIVIDE should return 12 from 13 and 198', function () {
    assert.equal(calculateNumber("DIVIDE", 13, 198), 0);
  });
  it('DIVIDE should return Error from 13 and 0', function () {
    assert.equal(calculateNumber("DIVIDE", 13, 0), "Error");
  });
  it('DIVIDE should return Error from 5 and 2', function () {
    assert.equal(calculateNumber("DIVIDE", 5, 2), 3);
  });
});
