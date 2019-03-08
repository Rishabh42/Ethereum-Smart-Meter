pragma solidity >=0.4.22 <0.6.0;

contract SMContract {

    address private utility;
    uint private counter;

    struct Reading{
      address uAddr;
//      uint256 power;
//      uint256 voltage;
//      uint256 current;
      uint256 energy_consumed;
      uint256 readingNo;
    }

    mapping (uint256=> Reading) public _readings;
    uint256[] public readingsArr;

    constructor() public {
        utility = msg.sender;
        counter = 1;
    }

    modifier notUtility{
        require(msg.sender != utility);
        _;
    }

    function newReading(uint256 energy) notUtility public {
    //Reading storage _newReading = _readings[readingNo++];

      _readings[counter].uAddr = msg.sender;
//      _readings[counter].power = power;
//      _readings[counter].voltage = voltage;
//      _readings[counter].current = current;
      _readings[counter].energy_consumed = energy;
      _readings[counter].readingNo = readingsArr.length++;

    readingsArr.push(counter);
    counter++;
    }

    /*function getData(uint readingNo) public constant returns(uint, uint, uint, uint) {
        return (readingsArr[readingNo].power, readingsArr[readingNo].voltage, readingsArr[readingNo].current, readingsArr[readingNo].energy);
    }*/
  }
