const hre = require("hardhat");
const CONTRACT_ADDR = "0xcFcdcb171E99c37D2f2e6959c97c5e6140D087f9";

async function main() {
  // hardhat-ethers
  const contract = await hre.ethers.getContractAt("Mod",CONTRACT_ADDR);

  await contract.attempt();

}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
