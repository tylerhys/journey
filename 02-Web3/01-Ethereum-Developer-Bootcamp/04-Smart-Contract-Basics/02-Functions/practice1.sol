// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

contract Contract {
	uint public x;

	constructor(uint _x) {
		x = _x;
	}

	function increment() external{
		x += 1;
	}

	function add(uint _x) external view returns(uint){
		return x + _x;
	}

        function double(uint _x) public pure returns(uint double){
        double = _x * 2;
    }

    function double(uint _x, uint _y) external pure returns(uint x, uint y){
        x = _x * 2;
        y = _y * 2;
    }
}