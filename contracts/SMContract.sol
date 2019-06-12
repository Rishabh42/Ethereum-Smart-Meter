pragma solidity >=0.4.22 <0.6.0;

contract SMContract {

    address private utility;
    uint private counter;

    struct Reading{
      address uAddr;
      uint256 energy_consumed;
      uint256 readingNo;
    }

    event readingEvent(address _user, uint256 _reading);

    mapping (uint256=> Reading) public _readings;
    uint256[] public readingsArr;

    constructor() public {
        utility = msg.sender;
        counter = 1;
    }

    function newReading(uint256 energy) public {

      _readings[counter].uAddr = msg.sender;
      _readings[counter].energy_consumed = energy;
      _readings[counter].readingNo = readingsArr.length++;

    readingsArr.push(counter);
    counter++;
    emit readingEvent(msg.sender, energy);
    }

    function returnCarbonCredits() public view returns(uint)  {
        uint carbonCredits = 0;
        if(readingsArr.length >= 10){
            for(uint256 i = 0; i < readingsArr.length; i++){
                carbonCredits += readingsArr[i]*2;
            }
        }
        return carbonCredits;
    }

  }
