import { Alchemy, Network } from 'alchemy-sdk';
import { useEffect, useState } from 'react';


import './App.css';

const settings = {
  apiKey: process.env.REACT_APP_ALCHEMY_API_KEY,
  network: Network.ETH_MAINNET,
};

const alchemy = new Alchemy(settings);

function App() {
  const [blockTxn,setBlockTxn] = useState();
  const [inputValue, setInputValue] = useState('');
  const [transfers, setTransfers] = useState([]);
  const [balance,setBalance] = useState()
  const [inputError, setInputError] = useState('');
  const isValidEthereumAddress = address => /^(0x)?[0-9a-fA-F]{40}$/.test(address);



  // Get latest block txns
  useEffect(() => {
    async function getBlockTxn() {
      const txn = await alchemy.core.getBlockWithTransactions();
      setBlockTxn(txn)
      }
      
    getBlockTxn();
    
  },[]);

  // Hash Formater
  const formatHash = (hash) => {
    if (typeof hash === 'string') {
      return hash.slice(0, 6) + '...' + hash.slice(-4);
    } else {
      // Handle null or undefined hash
      return 'N/A'; // or some other placeholder text
    }
  };

  // Copy to clipboard
  const copyToClipboard = async (text) => {
    if ('clipboard' in navigator) {
      return await navigator.clipboard.writeText(text);
    } else {
      return document.execCommand('copy', true, text);
    }
  };

  const handleHashClick = async (hash) => {
    await copyToClipboard(hash);
  };


    // Render the block txns
    function renderTransactionTable() {
      if (!blockTxn || !blockTxn.transactions) {
        return <div className='container'> <h2>Fetching Latest Block Data...</h2></div>;
      }
      const firstTxn = blockTxn.transactions[0];
      const blockNumber = firstTxn.blockNumber.toString();
      const blockHash = firstTxn.blockHash.toString();
      return (
      <div>
        <div className= 'container'>
        <h4 style={{ margin:10,textAlign: 'left' }}>
          Block Number: {blockNumber}
          <br />
          Block Hash: {blockHash}
          </h4>
        </div>
        <div className= 'container'>
        <h4 style={{ margin:10,textAlign: 'left' }}>Transactions in current block:</h4>
        <table className="table">
          <thead>
            <tr>
              <th>Index</th>
              <th>Hash</th>
              <th>From</th>
              <th>To</th>
              <th>Value</th>
              <th>Gas Price</th>
              <th>Priority Fee</th>
              <th>Max Fee</th>
              <th>Gas Limit</th>
            </tr>
          </thead>
          <tbody>
            {blockTxn.transactions.map((txn, index) => (
              <tr key={index}>
                <td>{txn.transactionIndex.toString()}</td>
                <td onClick={() => handleHashClick(txn.hash)} title="Click to copy" style={{ cursor: 'pointer' }}>
                {formatHash(txn.hash)}
                </td>
                <td onClick={() => handleHashClick(txn.from)} title="Click to copy" style={{ cursor: 'pointer' }}>
                {formatHash(txn.from)}
                </td>
                <td onClick={() => handleHashClick(txn.to)} title="Click to copy" style={{ cursor: 'pointer' }}>
                {formatHash(txn.to)}
                </td>
                <td>{txn.value.toString()}</td> {/* assuming value is a BigNumber */}
                <td>{txn.gasPrice.toString()}</td>
                <td>{txn.maxPriorityFeePerGas?.toString()}</td>
                <td>{txn.maxFeePerGas?.toString()}</td>
                <td>{txn.gasLimit.toString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
        </div>
        </div>
      );
    }

    // Handle input
    const handleInputChange = (e) => {
      const inputValue = e.target.value;
      setInputValue(inputValue);
    
      if (inputValue && !isValidEthereumAddress(inputValue)) {
        setInputError('Please enter a valid Ethereum address');
      } else {
        setInputError(''); // clear error message when the address is valid
      }
    };

    const handleSearch = async () => {
      // Call Alchemy API with the input value
      try {
        const transfersData = await alchemy.core.getAssetTransfers({
          fromAddress: inputValue,
          excludeZeroValue: true,
          category: ["external", "internal", "erc20", "erc721", "erc1155"],
          order: 'desc',
        });
        setTransfers(transfersData.transfers);
      } catch (error) {
        console.error('Error fetching asset transfers:', error);
      }
      console.log(transfers);
      try {
        const balance = await alchemy.core.getBalance(inputValue);
        setBalance(balance);
      }      
       catch (error) {
        console.error('Error fetching balance:', error);
      }
    };

    // Render wallet
    function renderWalletTable() {
      if (!transfers || !balance) {
        return;
      }
      return (
      <div>
        <h2 style={{ margin:10,textAlign: 'left' }}>Wallet Balance: {(parseInt(balance._hex,16)/1e18).toFixed(4).toString()}ETH</h2>
        <div>
        <h4 style={{ margin:10,textAlign: 'left' }}>Latest 1000 transcations:</h4>
        <table className="table">
        <thead>
          <tr>
            <th>Hash</th>
            <th>Block Number</th>
            <th>Category</th>
            <th>Asset</th>
            <th>From</th>
            <th>To</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {transfers.map((transfer, index) => (
            <tr key={index}>
              <td onClick={() => handleHashClick(transfer.hash)} title="Click to copy" style={{ cursor: 'pointer' }}>
                {formatHash(transfer.hash)}
              </td>
              <td>{parseInt(transfer.blockNum, 16).toString()}</td>
              <td>{transfer.category}</td>
              <td>{transfer.asset}</td>
              <td onClick={() => handleHashClick(transfer.from)} title="Click to copy" style={{ cursor: 'pointer' }}>
                {formatHash(transfer.from)}
              </td>
              <td onClick={() => handleHashClick(transfer.to)} title="Click to copy" style={{ cursor: 'pointer' }}>
                {formatHash(transfer.to)}
              </td>
              <td>{transfer.value}</td>
            </tr>
          ))}
        </tbody>
      </table>
        </div>
      </div>
      );
    }

    return (
      <div className="App">
      <button style={{ border: 'none', background: 'none' }}>
        <img src="tylerscan.jpg" alt="Home" style={{ width:500,cursor: 'pointer' }} />
      </button>
        <div style={{display:"flex",justifyContent:"center"}}>
          <div>
          {renderTransactionTable()}
          </div>
          <div className='container'>
            <div>
            {inputError && <div style={{color: 'red'}}>{inputError}</div>}
              <input
              type="text"
              value={inputValue}
              onChange={handleInputChange}
              placeholder="Enter address"
              style={{width:500}}
              />
              <button onClick={handleSearch}>Search</button>
            </div>
            <div>
              {renderWalletTable()}
            </div>
          </div>
        </div>
      </div>
    );
  }

export default App;
