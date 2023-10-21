import server from "./server";
import { secp256k1 } from 'ethereum-cryptography/secp256k1';
import { toHex } from "ethereum-cryptography/utils";
import { keccak256 } from "ethereum-cryptography/keccak"

function Wallet({ address, setAddress, balance, setBalance, privateKey, setPrivateKey }) {
  async function onChange(evt) {
    const privateKey = evt.target.value;
    setPrivateKey(privateKey);
    const publicKey = secp256k1.getPublicKey(privateKey);
    const address = "0x" + toHex(keccak256(publicKey.slice(1)).slice(-20));
    setAddress(address);
    if (address) {
      const {
        data: { balance },
      } = await server.get(`balance/${address}`);
      setBalance(balance);
    } else {
      setBalance(0);
    }
  }

  return (
    <div className="container wallet">
      <h4>Your Wallet:{address}</h4>
      <label>
        Private Key
        <input placeholder="Enter private key:" value={privateKey} onChange={onChange}></input>
      </label>
      <div className="balance">$TYL Balance: {balance}</div>
    </div>
  );
}

export default Wallet;
