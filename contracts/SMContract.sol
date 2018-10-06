pragma solidity ^0.4.16;

contract SMContract {

    struct Reading{
      uint power;
      uint voltage;
      uint current;
      uint energy;
      uint readingNo;
    }

    Reading[] public readingsArr;

    function enterParams(uint power, uint voltage, uint current, uint energy) public {
    Reading memory newReading = Reading({
      power: power,
      voltage: voltage,
      current: current,
      energy: energy,
      readingNo: readingsArr.length
      });
    readingsArr.push(newReading);
    }

    function getData(uint readingNo) public constant returns(uint, uint, uint, uint) {
        return (readingsArr[readingNo].power, readingsArr[readingNo].voltage, readingsArr[readingNo].current, readingsArr[readingNo].energy);
    }
  }
