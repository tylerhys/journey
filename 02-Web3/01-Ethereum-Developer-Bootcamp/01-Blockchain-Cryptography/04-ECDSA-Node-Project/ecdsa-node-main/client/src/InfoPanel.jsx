import server from "./server";
import React, { useState, useEffect } from 'react';
import './App.scss';
import tamaImage from './img/tama.png';
import coffinImage from './img/coffin.png';
import hlImage from './img/hl.png';

function InfoPanel(balanceChanged) {
    const [balances, setBalances] = useState({});
    const [openModal, setOpenModal] = useState(null);

    const user1 = ["Tama",tamaImage,"0xa0d7f4e6b420f475dbc4dd216877e6b6b6e2c32c"];
    const user2 = ["Coffin",coffinImage,"0x62f9454d2c107065b6c5df3b4f30c855b74fd2d3"];
    const user3 = ["HL",hlImage,"0x8f18cedbdaf9e72cfc5480f7c89a5b1d06854fac"];
    // const imageUrl = ;
    // const address = ;
    const addresses = [];
    addresses.push(user1[2]);
    addresses.push(user2[2]);
    addresses.push(user3[2]);

    async function fetchBalance() {
        let balances = {};

        for (let address of addresses) {
            try {
                const response = await server.get(`balance/${address}`);
                balances[address] = response.data.balance;
            } catch (error) {
                console.error(`Error fetching balance for address ${address}: `, error);
            }
        }
        setBalances(balances);
        
    }
    useEffect(() => {
        fetchBalance();
    }, [balanceChanged]);

  return (
    <div className="infoPanel">
    <div>
        {/* Tama */}
        {openModal === 'modal1' && (
            <div className="modalOverlay">
                <div className="modalContent">
                    <h3>Wallet Details (Tama)</h3>
                    <p>Private Key: a832d3d10a0b6b2685c47d59ec56a2251f719e78d4db1d87735d9d1e46b8527e</p>
                    <p>Public Key: 02018faf03328dc9fcb22af5b735b96c08f0a09941195de3ce0bb7d3621ddc611a</p>
                    <p>Wallet Address: 0xa0d7f4e6b420f475dbc4dd216877e6b6b6e2c32c</p>
                    <button onClick={() => setOpenModal(null)}>Close</button>
                </div>
            </div>
        )}

        {/* Coffin */}
        {openModal === 'modal2' && (
            <div className="modalOverlay">
            <div className="modalContent">
                <h3>Wallet Details (Coffin)</h3>
                <p>Private Key: 4dbe89d16f6ad6dd08ebdc2efb8132704f0e4f2a527df81010dd3b7a6a6b5ab3</p>
                <p>Public Key: 03f1cc70b34fff52b5b4e588ef77552a89fd755956eabf2a9d26ec9474befac1ec</p>
                <p>Wallet Address: 0x62f9454d2c107065b6c5df3b4f30c855b74fd2d3</p>
                <button onClick={() => setOpenModal(null)}>Close</button>
            </div>
        </div>
        )}

        {/* HL */}
        {openModal === 'modal3' && (
            <div className="modalOverlay">
            <div className="modalContent">
                <h3>Wallet Details (HL)</h3>
                <p>Private Key: afa3e98ad87473109f673d96f57274828b16e473f3964f90555d7e4fb4908588</p>
                <p>Public Key: 0257243ad5fcb7866ac49020b5b9dc86d6295c985724591fc016d75bd1a3623a0a</p>
                <p>Wallet Address: 0x8f18cedbdaf9e72cfc5480f7c89a5b1d06854fac</p>
                <button onClick={() => setOpenModal(null)}>Close</button>
            </div>
        </div>
        )}

    </div>

        <div>
            <h1>User Balance Dashboard</h1>
        </div>
            <div className="content">
                <div className="info">
                    <div>{user1[0]}</div>
                    <img src={user1[1]} alt={user1[0]} onClick={() => setOpenModal('modal1')}/>
                    <div>Balance: {balances[user1[2]]} $TYL</div>
                </div>
                <div className="info">
                    <div>{user2[0]}</div>
                    <img src={user2[1]} alt={user2[0]} onClick={() => setOpenModal('modal2')} />
                    <div>Balance: {balances[user2[2]]} $TYL</div>
                </div>
                <div className="info"> 
                    <div>{user3[0]}</div>
                    <img src={user3[1]} alt={user3[0]} onClick={() => setOpenModal('modal3')}/>
                    <div>Balance: {balances[user3[2]]} $TYL</div>
                </div>
            </div>
        </div>
  );
}

export default InfoPanel;