const { loadFixture } = require('@nomicfoundation/hardhat-network-helpers');
const { assert } = require('chai');

describe('Game4', function () {
  async function deployContractAndSetVariables() {
    const Game = await ethers.getContractFactory('Game4');
    const game = await Game.deploy();


    return { game };
  }
  it('should be a winner', async function () {
    const { game } = await loadFixture(deployContractAndSetVariables);
    
    const signer = ethers.provider.getSigner(0);
    const signer2 = ethers.provider.getSigner(1);
    const address = await signer.getAddress();
    const address2 = await signer2.getAddress()
    // nested mappings are rough :}
    game.connect(signer).write(address2)

    await game.connect(signer2).win(address);

    // leave this assertion as-is
    assert(await game.isWon(), 'You did not win the game');
  });
});
