import server from "./server";
import { secp256k1 } from 'ethereum-cryptography/secp256k1';
import { utf8ToBytes } from "ethereum-cryptography/utils";
import { keccak256 } from "ethereum-cryptography/keccak"

function Transfer({ address, setBalance, sendAmount, setSendAmount, recipient, setRecipient, privateKey, handleBalanceChange}) {

  const msg = `Transfer ${sendAmount} $TYL to ${recipient}`
  const setValue = (setter) => (evt) => setter(evt.target.value);

  async function transfer(evt) {
    evt.preventDefault();

    const msgHash = keccak256(utf8ToBytes(msg));
    const signature = secp256k1.sign(msgHash,privateKey);

    const signatureData = {
      r: signature.r.toString(),
      s: signature.s.toString(),
      recovery: signature.recovery
   };
    
    try {
      const {
        data: { balance },
      } = await server.post(`send`, {
        sender: address,
        amount: parseInt(sendAmount),
        recipient,
        msg: msgHash,
        signatureData,
      });
      setBalance(balance);
      handleBalanceChange();
    } catch (ex) {
      if (ex.response && ex.response.data && ex.response.data.message) {
        console.error(ex)
        alert(ex.response.data.message);
      } else {
        console.error(ex)
        alert("An unexpected error occurred.");
      }
    }
  }

  return (
    <form className="container transfer" onSubmit={transfer}>
      <h1>Send Transaction</h1>

      <label>
        Send Amount
        <input
          placeholder="1, 2, 3..."
          value={sendAmount}
          onChange={setValue(setSendAmount)}
        ></input>
      </label>

      <label>
        Recipient
        <input
          placeholder="Type an address"
          value={recipient}
          onChange={setValue(setRecipient)}
        ></input>
      </label>

      <div className="message">
        {sendAmount && recipient ? msg : "Message to sign..."}
      </div>
      <input type="submit" className="button" value="Sign & Transfer" />
      
    </form>
  );
}

export default Transfer;
