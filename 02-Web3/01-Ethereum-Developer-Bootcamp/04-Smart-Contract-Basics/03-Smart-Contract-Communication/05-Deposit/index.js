const ethers = require('ethers');

async function deposit(contract) {
    await contract.deposit({value: ethers.utils.parseEther("6.9")})
}

module.exports = deposit;