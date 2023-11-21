// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract Ownable {
    constructor() { owner = msg.sender; }
    address owner;
	modifier onlyOwner {
		require(msg.sender == owner);
		_;
	}
}

contract Transferable is Ownable{
	function transfer(address _to) external onlyOwner{
		owner = _to;
	}
}