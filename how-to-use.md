How to Use dex-arbitrage
This guide explains how to use the dex-arbitrage project to find and exploit arbitrage opportunities on decentralized exchanges (DEXs).

Prerequisites
Before you can use dex-arbitrage, you need to have the following installed on your system:

Python 3.6 or higher
The project dependencies (listed in the requirements.txt file)

Collecting Data
The first step in using dex-arbitrage is to collect price data from DEXs. This is done using the collect-data.py script.
To run the script, open a terminal and navigate to the project directory, then run the following command:

python scripts/collect-data.py

This will collect the latest prices for a set of assets (e.g. ETH/USDT, BTC/USDT, etc.) on multiple DEXs. The collected data will be saved to the data directory in the project root.

Analyzing Data
The next step is to analyze the collected data to find potential arbitrage opportunities. This is done using the analyze-data.py script.

To run the script, open a terminal and navigate to the project directory, then run the following command:

python scripts/analyze-data.py
This will analyze the data and output a list of potential arbitrage opportunities. The output will look something like this:

[    {        "asset": "ETH/USDT",        "dex1": "Uniswap",        "dex1_price": 225.36,        "dex2": "Sushiswap",        "dex2_price": 222.11,        "profit": 3.25    },    {        "asset": "BTC/USDT",        "dex1": "Uniswap",        "dex1_price": 23145.63,        "dex2": "Kyber",        "dex2_price": 23124.21,        "profit": 21.42    }]
Each item in the list represents a potential arbitrage opportunity, with the following information:

asset: The asset pair (e.g. ETH/USDT)
dex1: The name of the first DEX
dex1_price: The price of the asset on the first DEX
dex2: The name of the second DEX
dex2_price: The price of the asset on the second DEX
profit: The potential profit from exploiting the arbitrage opportunity
Exploiting Opportunities
Once you have identified a potential arbitrage opportunity, you can exploit it by buying the asset on the DEX with the lower price and selling it on the DEX with the higher price.

Keep in mind that arbitrage opportunities can be fleeting, so you will need to act quickly to take advantage of them.

Conclusion
dex-arbitrage is a powerful tool for finding and exploiting arbitrage opportunities on DEXs.
