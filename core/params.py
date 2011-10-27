from datetime import datetime
from datetime import date
from dateutil import relativedelta
import numpy as np

start = datetime(1990, 2, 1)
end = datetime(2005, 12, 31)

def get_portfolio_params():
    return {
        'expected_returns': {
            'AA': 0.03,
            'AAPL': 0.03,
            'AXP': 0.03,
            'BA': 0.03,
            'BAC': 0.03,
            'BP': 0.03,
            'CAT': 0.03,
            'CVX': 0.03,
            'DD': 0.03,
            'DIS': 0.03,
            'GE': 0.03,
            'HD': 0.03,
            'HPQ': 0.03,
            'IBM': 0.03,
            'INTC': 0.03,
            'JNJ': 0.03,
            'JPM': 0.03,
            'KO': 0.03,
            'MCD': 0.03,
            'MMM': 0.03,
            'MRK': 0.03,
            'MSFT': 0.03,
            'PFE': 0.03,
            'PG': 0.03,
            'T': 0.03,
            'TGT': 0.03,
            'UTX': 0.03,
            'VZ': 0.03,
            'WMT': 0.03,
            'XOM': 0.03
        },
        'holding_periods': {
            'AA': {'start': start, 'end': end},
            'AAPL': {'start': start, 'end': end},
            'AXP': {'start': start, 'end': end},
            'BA': {'start': start, 'end': end},
            'BAC': {'start': start, 'end': end},
            'BP': {'start': start, 'end': end},
            'CAT': {'start': start, 'end': end},
            'CVX': {'start': start, 'end': end},
            'DD': {'start': start, 'end': end},
            'DIS': {'start': start, 'end': end},
            'GE': {'start': start, 'end': end},
            'HD': {'start': start, 'end': end},
            'HPQ': {'start': start, 'end': end},
            'IBM': {'start': start, 'end': end},
            'INTC': {'start': start, 'end': end},
            'JNJ': {'start': start, 'end': end},
            'JPM': {'start': start, 'end': end},
            'KO': {'start': start, 'end': end},
            'MCD': {'start': start, 'end': end},
            'MMM': {'start': start, 'end': end},
            'MRK': {'start': start, 'end': end},
            'MSFT': {'start': start, 'end': end},
            'PFE': {'start': start, 'end': end},
            'PG': {'start': start, 'end': end},
            'T': {'start': start, 'end': end},
            'TGT': {'start': start, 'end': end},
            'UTX': {'start': start, 'end': end},
            'VZ': {'start': start, 'end': end},
            'WMT': {'start': start, 'end': end},
            'XOM': {'start': start, 'end': end}
        },
        'shares': {
            'AA': 55,
            'AAPL': 15,
            'AXP': 17,
            'BA': 56,
            'BAC': 110,
            'BP': 10,
            'CAT': 50,
            'CVX': 40,
            'DD': 20,
            'DIS': 15,
            'GE': 17,
            'HD': 66,
            'HPQ': 11,
            'IBM': 45,
            'INTC': 75,
            'JNJ': 60,
            'JPM': 37,
            'KO': 15,
            'MCD': 55,
            'MMM': 25,
            'MRK': 35,
            'MSFT': 27,
            'PFE': 65,
            'PG': 45,
            'T': 95,
            'TGT': 85,
            'UTX': 22,
            'VZ': 11,
            'WMT': 66,
            'XOM': 25
        },
        'constraints': {
            'min_position': 0.05,
            'max_position': 0.15,
            'target_gain': 0.03
        },
        'defaults': {
            'frequency': 'm',
            'start': start,
            'end': end
        }
    }

# s&p 500 weights as of 9/28/2011
def get_bench_params():
    return {
        'AA': 0.00272032219920074,
        'AAPL': 0.0962451656611796,
        'AXP': 0.0143484526998522,
        'BA': 0.012146633471393,
        'BAC': 0.016939408927395,
        'BP': 0.033484485435158,
        'CAT': 0.0140354286118044,
        'CVX': 0.0531751293140174,
        'DD': 0.0106196993721854,
        'DIS': 0.0162045166908081,
        'GE': 0.0454079755939924,
        'HD': 0.0143972896530083,
        'HPQ': 0.0128677578435264,
        'IBM': 0.0551493891224519,
        'INTC': 0.0329909204830494,
        'JNJ': 0.0444468227925178,
        'JPM': 0.0324454013254557,
        'KO': 0.0400566924290254,
        'MCD': 0.0240467442377591,
        'MMM': 0.0143029927700528,
        'MRK': 0.0260550340507863,
        'MSFT': 0.0590979087393208,
        'PFE': 0.038134386826076,
        'PG': 0.0461872886762692,
        'T': 0.044784525128171,
        'TGT': 0.00590875178982238,
        'UTX': 0.0172864630200356,
        'VZ': 0.027249980776944,
        'WMT': 0.0503696022178211,
        'XOM': 0.0988948301409206
    }