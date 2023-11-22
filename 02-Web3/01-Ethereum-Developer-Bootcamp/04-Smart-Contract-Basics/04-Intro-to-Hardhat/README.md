## Hardhat
Work Flow
```
1. Open a terminal
2. Run cd Desktop, then create a new folder via mkdir au-hardhat-practice, then move into that newly-created folder by running cd au-hardhat-practice
3. Once you are in the au-hardhat-practice folder, in your terminal run npm init -y to initialize a package.json
4. Run npm i hardhat
5. Run npm i dotenv
6. Run touch .env in order to create a .env file at the root-level of your project, then populate it with important data and save
7. Run npx hardhat which will initialize a brand new Hardhat project
8. We recommend the following flow: Choose the current root > YES to the .gitignore > YES to install the sample project's dependencies
9. Add require(‘dotenv’).config() at the top of your hardhat.config.js file
10. Add networks flag to hardhat.config.js, add your Alchemy RPC URL under url and your testnet private key under accounts
11. Set up your scripts and contracts, then deploy in a flash!
```

```
npm install --save-dev @nomiclabs/hardhat-etherscan
require("@nomiclabs/hardhat-etherscan");

npm install --save-dev @nomiclabs/hardhat-ethers ethers
require("@nomiclabs/hardhat-ethers");

npx hardhat verify --network goerli --contract contracts/GoofyGoober.sol:GoofyGoober 0x0E27700DA2a01978972164FB225397b753Be2730
```