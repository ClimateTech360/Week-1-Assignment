TradePal: Rule-Based Crypto Advisor
TradePal is a Python-based chatbot that provides cryptocurrency investment advice using simple rule-based logic. 
It analyzes a small dataset of five cryptocurrencies and helps users make informed decisions based on profitability (price trend) and sustainability (energy efficiency and project viability).
Features
•	Provides advice on the most profitable cryptocurrencies.
•	Identifies the most sustainable crypto options.
•	Recommends coins with a balance of profitability and sustainability.
•	Understands basic user inputs and keywords.
•	Offers custom advice on specific cryptocurrencies.
•	Works entirely offline using a predefined dataset.

Dataset
TradePal uses dummy data stored in a Pandas DataFrame. Each crypto entry includes:
•	Price Trend (% change)
•	Energy Efficiency (score from 1 to 10)
•	Viability Score (score from 1 to 10)
Example entries include Bitcoin, Ethereum, Dogecoin, Solana, and Cardano.

How It Works
TradePal uses keyword matching to interpret user queries. It has three main types of logic:
1.	Profitability Advice: Responds to keywords related to price trend and investment.
2.	Sustainability Advice: Responds to keywords related to eco-friendliness and energy use.
3.	Balanced Recommendation: Calculates and returns the best crypto based on combined scores.
Users can also enter the name of a specific cryptocurrency to receive detailed advice.

Example Questions
•	Which crypto is trending up?
•	What’s the most sustainable coin?
•	Which one is best for the environment?
•	Tell me about Solana.
•	Which crypto has both good returns and is eco-friendly?

How to Run
Requirements
•	Python 3.x
•	Pandas

Steps
1.	Save the script as tradepal.py.
2.	Install Pandas if not already installed
3.	Run the script
4.	Interact with TradePal in the terminal. Type exit to end the session.
Disclaimer
This chatbot uses fictional data for learning purposes. It does not provide real financial advice. Always conduct your own research before making any investment decisions.

