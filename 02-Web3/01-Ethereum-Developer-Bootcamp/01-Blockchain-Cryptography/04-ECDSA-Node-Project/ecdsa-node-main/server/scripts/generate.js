// Added   "type": "module" in package.json
import { secp256k1 } from 'ethereum-cryptography/secp256k1';
import { toHex } from "ethereum-cryptography/utils";
import { keccak256 } from "ethereum-cryptography/keccak"

const privateKey = secp256k1.utils.randomPrivateKey();
console.log('private key:', toHex(privateKey));

const publicKey = secp256k1.getPublicKey(privateKey);
console.log('public key:', toHex(publicKey));

const walletAddress = keccak256(publicKey.slice(1)).slice(-20)
console.log('wallet address:', "0x" + toHex(walletAddress));