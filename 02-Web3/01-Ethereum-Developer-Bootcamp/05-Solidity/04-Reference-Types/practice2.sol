// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract Contract {
    function sum(uint[] calldata _x) pure external returns(uint total){
        for(uint i = 0; i < _x.length; i++){
            total += _x[i];
        }
    }
}