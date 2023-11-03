const ethers = require('ethers');
const { Wallet, utils } = ethers;
const { ganacheProvider, PRIVATE_KEY } = require('./config');

const provider = new ethers.providers.Web3Provider(ganacheProvider);

// create a wallet with a private key and connect it to the ethers provider
const wallet = new Wallet(PRIVATE_KEY, provider);

async function sendEther({ value, to }) {
    // broadcast the transaction to the ethereum network
    return wallet.sendTransaction({ value, to });
}

module.exports = sendEther;