// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract Token {
    uint public totalSupply = 0;
    string public name = 'Banana';
    string public symbol = 'BAN';
    uint8 public decimals = 18;

    mapping(address => uint256) balances;

    event Transfer(address from,address to, uint value);

    function balanceOf(address _x) external view returns(uint balance){
        balance = balances[_x];
    }

    function transfer(address _to, uint _amt) external returns(bool success){
        require(balances[msg.sender] >= _amt);
        balances[msg.sender] -= _amt;
        balances[_to] += _amt;
        success = true;
        emit Transfer(msg.sender, _to, _amt);

    }

    constructor(){
        totalSupply = 1000 * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
    }
}