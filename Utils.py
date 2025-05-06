import random

def fetch_tokens():
    # Simulated fetch from pump.fun (replace with real API later)
    sample = [{
        "name": f"CN Meme {i}",
        "symbol": f"CNM{i}",
        "address": f"token{i}",
        "market_cap": random.randint(4000, 15000),
        "volume": random.randint(1000, 8000),
        "url": f"https://pump.fun/{i}",
        "creator": f"user{i}"
    } for i in range(1, 21)]
    return sample

def filter_tokens(tokens, known):
    new_tokens = []
    trending_tokens = []
    for token in tokens:
        if token["address"] not in known:
            if "CN" in token["name"] or "cn" in token["name"]:
                if token["market_cap"] >= 4000 and token["volume"] >= 1000:
                    new_tokens.append(token)
        else:
            # Example: Trending logic (volume jump or price move)
            old = known[token["address"]]
            if token["market_cap"] > old["market_cap"] * 1.5 or token["volume"] > old["volume"] * 2:
                trending_tokens.append(token)
    return new_tokens, trending_tokens

def track_token_growth(known):
    growth_alerts = []
    for address, token in known.items():
        if "initial_mc" not in token:
            token["initial_mc"] = token["market_cap"]
        else:
            growth = token["market_cap"] / token["initial_mc"]
            if growth >= 2:
                growth_alerts.append((token, round(growth, 2)))
                token["initial_mc"] = token["market_cap"]  # reset after alert
    return growth_alerts
