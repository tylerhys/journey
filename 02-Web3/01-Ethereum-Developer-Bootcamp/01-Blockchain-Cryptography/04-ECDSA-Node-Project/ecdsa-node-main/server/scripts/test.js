import { secp256k1 } from 'ethereum-cryptography/secp256k1';
import { toHex, utf8ToBytes } from "ethereum-cryptography/utils";
import { keccak256 } from "ethereum-cryptography/keccak"
// import * as secp from '@noble/secp256k1';

// Store Private Key
const privateKey="4dbe89d16f6ad6dd08ebdc2efb8132704f0e4f2a527df81010dd3b7a6a6b5ab3";
// const recipient = "0x62f9454d2c107065b6c5df3b4f30c855b74fd2d3";
// const amount = 5;
const msg = `Transfer 10 $TYL to 0x62f9454d2c107065b6c5df3b4f30c855b74fd2d3`
const msgHash = keccak256(utf8ToBytes(msg));
const signature = secp256k1.sign(msgHash,privateKey);
const recoveredKey = signature.recoverPublicKey(msgHash);
const hexPb = recoveredKey.toHex();

const isValid = secp256k1.verify(signature,msgHash,hexPb);

if (isValid !== true) {
  console.log("Signature verification failed." );
}
else {
    console.log("Signature verification success..." );
}