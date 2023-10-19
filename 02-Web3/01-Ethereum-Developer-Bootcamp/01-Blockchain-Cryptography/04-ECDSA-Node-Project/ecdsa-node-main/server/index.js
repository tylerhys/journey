import express, { json } from "express";
const app = express();
import cors from "cors";
const port = 3042;

app.use(cors());
app.use(json());

const balances = {
  "0x7f09ebdedabb1af50fb547ed0d7cf23783099950": 100,
  "0x747288eafff87a1605f0ddeed1c7c2bbcabb1ead": 50,
  "0xffc45c61ff3276fe181458fabb18500fbed66457": 75,
};

app.get("/balance/:address", (req, res) => {
  const { address } = req.params;
  const balance = balances[address] || 0;
  res.send({ balance });
});

app.post("/send", (req, res) => {
  // TODO: get a signature from client-side application
  // recover the public addrss from signature
  const { sender, recipient, amount } = req.body;

  setInitialBalance(sender);
  setInitialBalance(recipient);

  if (balances[sender] < amount) {
    res.status(400).send({ message: "Not enough funds!" });
  } else {
    balances[sender] -= amount;
    balances[recipient] += amount;
    res.send({ balance: balances[sender] });
  }
});

app.listen(port, () => {
  console.log(`Listening on port ${port}!`);
});

function setInitialBalance(address) {
  if (!balances[address]) {
    balances[address] = 0;
  }
}
