// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract Escrow {
    address public depositor;
    address public beneficiary;
    address public arbiter;
    bool public isApproved = false;
    uint balance = msg.value;
    event Approved(uint);

    constructor(address _arb, address _bene) payable{
        arbiter = _arb;
        beneficiary = _bene;
        depositor = msg.sender;
    }

    function approve() external{
        require (msg.sender == arbiter);
        (bool sent, ) = beneficiary.call{ value: balance }("");
        require(sent, "Failed to send ether");
        isApproved = true;
        emit Approved(balance);
    }
}