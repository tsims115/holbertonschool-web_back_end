const assert = require('assert');
const calculateNumber = require('./0-calcul');
describe('calculateNumber', function () {
  it('should return 5 from 1.5 and 2.5', function () {
      assert.equal(calculateNumber(1.5, 2.5), 5);
  });
  it('should return 4 from 1.2 and 2.7', function () {
    assert.equal(calculateNumber(1.2, 2.7), 4);
  });
  it('should return 139 from 100.5 and 38.2', function () {
    assert.equal(calculateNumber(100.5, 38.2), 139);
  });
  it('should return -4 from -1.2 and -3.5', function () {
    assert.equal(calculateNumber(-1.2, -3.5), -4);
  });
  it('should return -7 from -108.2 and 100.7', function () {
    assert.equal(calculateNumber(-108.2, 100.7), -7);
  });
});
