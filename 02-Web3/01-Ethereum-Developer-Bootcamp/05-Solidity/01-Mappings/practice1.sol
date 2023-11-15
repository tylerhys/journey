// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

contract Contract {
    mapping(address => bool) public members;

    function addMember(address x_) external{
        members[x_] = true;
    }

    function isMember(address x_) external returns(bool){
        return members[x_];
    }

    function removeMember(address x_) external{
        members[x_] = false;
    }
}