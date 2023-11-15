const hre = require("hardhat");

async function main() {
  // hardhat-ethers
  const Contract = await hre.ethers.getContractFactory("Mod");
  const contract = await Contract.deploy();

  await contract.waitForDeployment();

  console.log(
    `Deployed to ${contract.target}`
  );
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
