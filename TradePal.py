import pandas as pd

# Dummy crypto data
data = pd.DataFrame({
    'Name': ['Bitcoin', 'Ethereum', 'Dogecoin', 'Solana', 'Cardano'],
    'Price_Trend': [3.5, 2.1, -1.0, 4.0, -2.5],
    'Energy_Efficiency': [5, 6, 2, 7, 8],
    'Viability_Score': [8, 9, 4, 7, 6]
})

# Greeting keywords
greetings = ["hello", "hi", "hey", "how are you", "greetings", "what's up"]

# Profitability keywords
profit_keywords = [
    "trending", "best coin", "profitable", "short-term", "growing",
    "top-performing", "price", "gain", "returns", "investment", "rise"
]

# Sustainability keywords
sustain_keywords = [
    "sustainable", "least energy", "eco-friendly", "green", "planet",
    "environment", "low energy", "environmentally", "climate", "efficient"
]

# ----- Helper Functions -----


def get_top_profit_crypto():
    top = data.sort_values(by='Price_Trend', ascending=False).iloc[0]
    return f"{top['Name']} is currently the most profitable with a {top['Price_Trend']}% price increase."


def get_top_sustainable_crypto():
    df = data.copy()
    df['Sustainability_Score'] = df['Energy_Efficiency'] + df['Viability_Score']
    top = df.sort_values(by='Sustainability_Score', ascending=False).iloc[0]
    return f"{top['Name']} is the most sustainable crypto with high energy efficiency and viability."


def get_best_balanced_crypto():
    df = data.copy()
    df['Combined_Score'] = df['Price_Trend'] + \
        df['Energy_Efficiency'] + df['Viability_Score']
    top = df.sort_values(by='Combined_Score', ascending=False).iloc[0]
    return f"{top['Name']} offers the best balance between profitability and sustainability."


def advise_crypto(name):
    crypto = data[data['Name'].str.lower() == name.lower()]
    if crypto.empty:
        return "Sorry, I don't have data for that cryptocurrency."

    row = crypto.iloc[0]
    trend, energy, viability = row['Price_Trend'], row['Energy_Efficiency'], row['Viability_Score']

    if trend > 1:
        profit = "The price trend is strong — good short-term potential."
    elif trend > 0:
        profit = "The price is slowly rising — moderate growth."
    else:
        profit = "The price is dropping — currently risky."

    if energy >= 7 and viability >= 7:
        sustain = "Highly sustainable and viable project."
    elif energy >= 5 and viability >= 5:
        sustain = "Moderately sustainable — further analysis recommended."
    else:
        sustain = "Low sustainability — invest with caution."

    return f"""
==============================
TradePal's Advice on {row['Name']}:
==============================
{profit}
{sustain}
    """

# ----- Interpret Question -----


def interpret_question(q):
    q = q.lower().strip()

    if any(greet in q for greet in greetings):
        return "Hello, my name is TradePal. How can I help you?"

    if any(word in q for word in profit_keywords):
        return get_top_profit_crypto()

    if any(word in q for word in sustain_keywords):
        return get_top_sustainable_crypto()

    if "balance" in q or ("profit" in q and "sustain" in q):
        return get_best_balanced_crypto()

    return "I'm not sure how to answer that based on my data. Try asking about profitability or sustainability."

# ----- Chat Loop -----


def start_chatbot():
    print("Welcome to TradePal — your crypto trading assistant!")
    print("Type 'exit' anytime to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Thanks for chatting with TradePal. Happy trading!")
            break
        elif any(user_input.lower() == coin.lower() for coin in data['Name']):
            print(advise_crypto(user_input))
        else:
            print(interpret_question(user_input))


# Start the bot
start_chatbot()
