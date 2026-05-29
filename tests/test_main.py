# test_roman_to_decimal.py
import pytest
from roman_to_decimal import roman_to_decimal

def test_roman_to_decimal():
    assert roman_to_decimal("I") == 1
    assert roman_to_decimal("V") == 5
    assert roman_to_decimal("X") == 10
    assert roman_to_decimal("L") == 50
    assert roman_to_decimal("C") == 100
    assert roman_to_decimal("D") == 500
    assert roman_to_decimal("M") == 1000

def test_roman_to_decimal_multiple():
    assert roman_to_decimal("II") == 2
    assert roman_to_decimal("III") == 3
    assert roman_to_decimal("IV") == 4
    assert roman_to_decimal("IX") == 9
    assert roman_to_decimal("XL") == 40
    assert roman_to_decimal("XC") == 90
    assert roman_to_decimal("CD") == 400
    assert roman_to_decimal("CM") == 900

def test_roman_to_decimal_invalid():
    with pytest.raises(ValueError):
        roman_to_decimal("ABC")
    with pytest.raises(ValueError):
        roman_to_decimal("")

def test_roman_to_decimal_edge():
    assert roman_to_decimal("") == 0
    assert roman_to_decimal("MCMXCIX") == 1999
```

```javascript
// romanToDecimal.test.js
import romanToDecimal from './romanToDecimal';

describe('romanToDecimal', () => {
  it('should convert I to 1', () => {
    expect(romanToDecimal('I')).toBe(1);
  });

  it('should convert V to 5', () => {
    expect(romanToDecimal('V')).toBe(5);
  });

  it('should convert X to 10', () => {
    expect(romanToDecimal('X')).toBe(10);
  });

  it('should convert L to 50', () => {
    expect(romanToDecimal('L')).toBe(50);
  });

  it('should convert C to 100', () => {
    expect(romanToDecimal('C')).toBe(100);
  });

  it('should convert D to 500', () => {
    expect(romanToDecimal('D')).toBe(500);
  });

  it('should convert M to 1000', () => {
    expect(romanToDecimal('M')).toBe(1000);
  });

  it('should convert II to 2', () => {
    expect(romanToDecimal('II')).toBe(2);
  });

  it('should convert III to 3', () => {
    expect(romanToDecimal('III')).toBe(3);
  });

  it('should convert IV to 4', () => {
    expect(romanToDecimal('IV')).toBe(4);
  });

  it('should convert IX to 9', () => {
    expect(romanToDecimal('IX')).toBe(9);
  });

  it('should convert XL to 40', () => {
    expect(romanToDecimal('XL')).toBe(40);
  });

  it('should convert XC to 90', () => {
    expect(romanToDecimal('XC')).toBe(90);
  });

  it('should convert CD to 400', () => {
    expect(romanToDecimal('CD')).toBe(400);
  });

  it('should convert CM to 900', () => {
    expect(romanToDecimal('CM')).toBe(900);
  });

  it('should throw error for invalid input', () => {
    expect(() => romanToDecimal('ABC')).toThrowError();
  });

  it('should throw error for empty input', () => {
    expect(() => romanToDecimal('')).toThrowError();
  });

  it('should convert empty string to 0', () => {
    expect(romanToDecimal('')).toBe(0);
  });

  it('should convert MCMXCIX to 1999', () => {
    expect(romanToDecimal('MCMXCIX')).toBe(1999);
  });
});
