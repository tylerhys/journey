// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract Contract {
    uint[] public evenNumbers;

    function filterEven(uint[] calldata _x) external{
        for(uint i = 0; i < _x.length; i++){
            if(_x[i]%2 == 0){
                evenNumbers.push(_x[i]);
            }
        }
    }
}