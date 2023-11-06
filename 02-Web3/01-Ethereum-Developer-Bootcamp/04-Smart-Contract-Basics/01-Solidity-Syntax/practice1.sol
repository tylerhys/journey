// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

contract Contract {
    // Booleans
	bool public a = true;
    bool public b = false;

    // Unsigned Integers
    uint8 public c = 10;
    uint16 public d = 6969;
    uint256 public sum = c + d;

    // Signed Integers
    int8 public e = 25;
    int8 public f = -69;
    int16 public difference = e - f;

    // String Literals
    bytes32 public msg1 = "Hello World";
    string public msg2 = "I need longer than 32 bytes because I'm a stoopid degen";

    // Enum
    enum Foods { Apple, Pizza, Bagel, Banana }

	Foods public food1 = Foods.Apple;
	Foods public food2 = Foods.Pizza;
	Foods public food3 = Foods.Bagel;
	Foods public food4 = Foods.Banana;
}