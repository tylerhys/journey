// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract StackClub {
	address[] members;

	constructor() {
		members.push(msg.sender);
	}

	function isMember(address member) public view returns(bool) {
		for(uint i = 0; i < members.length; i++) {
			if(members[i] == member) {
				return true;
			}
		}
		return false;
	}

	function removeLastMember() external {
		require(isMember(msg.sender));
		members.pop();
	}

	function addMember(address member) external {
		require(isMember(msg.sender));
		members.push(member);
	}
}
