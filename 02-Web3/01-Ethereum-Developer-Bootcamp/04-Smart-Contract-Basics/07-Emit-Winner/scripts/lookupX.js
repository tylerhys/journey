const hre = require("hardhat");
const CONTRACT_ADDR = "0x2459529F0B251Ad16751ccD378F46b3d1c887321";

async function main() {
  // hardhat-ethers
  const contract = await hre.ethers.getContractAt("Contract",CONTRACT_ADDR);

  console.log(await contract.x());

}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
