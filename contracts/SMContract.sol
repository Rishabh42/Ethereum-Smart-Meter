pragma solidity ^0.4.16;

contract SMContract {

    address private utility;

    struct Reading{
      address uAddr;
      uint256 power;
      uint256 voltage;
      uint256 current;
      uint256 energy;
      uint256 readingNo;
    }

    mapping (uint256=> Reading) public _readings;
    uint256[] public readingsArr;

    constructor() public {
        utility = msg.sender;
    }

    function newReading(uint256 readingNo, uint256 power, uint256 voltage, uint256 current, uint256 energy) public {
    Reading storage _newReading = _readings[readingNo++];

      _newReading.uAddr = msg.sender;
      _newReading.power = power;
      _newReading.voltage = voltage;
      _newReading.current = current;
      _newReading.energy = energy;
      _newReading.readingNo = readingsArr.length++;
      
    readingsArr.push(readingNo);
    }

    /*function getData(uint readingNo) public constant returns(uint, uint, uint, uint) {
        return (readingsArr[readingNo].power, readingsArr[readingNo].voltage, readingsArr[readingNo].current, readingsArr[readingNo].energy);
    }*/
  }
