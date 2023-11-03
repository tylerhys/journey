const { utils, providers, Wallet } = require('ethers');
const { ganacheProvider } = require('./config');

const provider = new providers.Web3Provider(ganacheProvider);

async function donate(privateKey, charities) {
    // TODO: donate to charity!
    const wallet = new Wallet(privateKey,provider);
    const amt = utils.parseEther("1.0");
     for(let i = 0;i<charities.length;i++){
         const charity = charities[i]
         await wallet.sendTransaction({ 
             value: amt,
             to: charity
               })

     }
}

module.exports = donate;