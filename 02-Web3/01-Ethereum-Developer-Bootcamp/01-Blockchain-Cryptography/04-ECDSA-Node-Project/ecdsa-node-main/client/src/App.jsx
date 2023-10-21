import Wallet from "./Wallet";
import Transfer from "./Transfer";
import "./App.scss";
import InfoPanel from "./InfoPanel";"./InfoPanel";
import { useState } from "react";

function App() {
  const [balance, setBalance] = useState(0);
  const [address, setAddress] = useState("");
  const [privateKey, setPrivateKey] = useState("");
  const [sendAmount, setSendAmount] = useState("");
  const [recipient, setRecipient] = useState("");
  const [balanceChanged, setBalanceChanged] = useState(false);
  const msg = `Transfer ${sendAmount} $TYL to ${recipient}`;

  const handleBalanceChange = () => {
    setBalanceChanged(prev => !prev);
  }
  return (
    <div className="app">
      <div className="content">
        <Wallet
          balance={balance}
          privateKey={privateKey}
          setPrivateKey={setPrivateKey}
          setBalance={setBalance}
          address={address}
          setAddress={setAddress}
        />
        <Transfer 
          setBalance={setBalance} 
          address={address}
          sendAmount={sendAmount}
          setSendAmount={setSendAmount}
          recipient={recipient}
          setRecipient={setRecipient}
          privateKey={privateKey}
          handleBalanceChange={handleBalanceChange}
        />
      </div>
      <div className="content">
        <InfoPanel balanceChanged={balanceChanged}
        />
      </div>

    </div>
  );
}

export default App;
