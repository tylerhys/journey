// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

contract Contract {
	struct User {
		uint balance;
		bool isActive;
	}

	mapping(address => User) public users;

	function createUser() external {
		require(!users[msg.sender].isActive);
		users[msg.sender] = User(100, true);
	}

	function transfer(address to, uint amount) external {
		require(users[msg.sender].isActive);
		require(users[to].isActive);
		require(users[msg.sender].balance >= amount);
		users[msg.sender].balance -= amount;
		users[to].balance += amount;
	}
}