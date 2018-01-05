from datetime import datetime
from cryptohist.coinmarketcap import CoinMarketCapFetcher

fetcher = CoinMarketCapFetcher()
print("%s: Started" % datetime.utcnow())
for symbol in fetcher.get_symbols():
    print("%s: Running %s" % (datetime.utcnow(), symbol))
    fetcher.fetch_by_symbol(symbol)
print("%s: Finished" % datetime.utcnow())
