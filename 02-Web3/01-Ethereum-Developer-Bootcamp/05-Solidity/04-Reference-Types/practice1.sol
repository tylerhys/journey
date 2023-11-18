// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract Contract {
	function sum(uint[5] calldata x) external pure returns(uint total) {
		for(uint i = 0; i < 5; i++) {
			total += x[i];
		}
	}
}