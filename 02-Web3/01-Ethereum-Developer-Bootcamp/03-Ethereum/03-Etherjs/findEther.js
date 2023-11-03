const { providers } = require('ethers');
const { ganacheProvider } = require('./config');

const provider = new providers.Web3Provider(ganacheProvider);

async function findEther(address) {
    const addresses = [];
    const blockNumber = await provider.getBlockNumber();
    for (let i = 0; i <= blockNumber; i++) {
        const block = await provider.getBlockWithTransactions(i);
        block.transactions.forEach((tx) => {
            if(tx.from === address) {
                addresses.push(tx.to);
            }
        });
    }
    return addresses;
}

module.exports = findEther;