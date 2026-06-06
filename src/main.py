import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT/'data/trades.csv', parse_dates=['date'])
df = df.sort_values('date')
df['equity_curve'] = df['net_pnl'].cumsum()
df['month'] = df['date'].dt.to_period('M').astype(str)

summary = pd.DataFrame([{
    'trades': len(df),
    'total_pnl': df['net_pnl'].sum(),
    'win_rate': (df['net_pnl']>0).mean(),
    'avg_win': df.loc[df.net_pnl>0,'net_pnl'].mean(),
    'avg_loss': df.loc[df.net_pnl<0,'net_pnl'].mean(),
    'profit_factor': df.loc[df.net_pnl>0,'net_pnl'].sum() / abs(df.loc[df.net_pnl<0,'net_pnl'].sum()),
    'max_drawdown': (df['equity_curve'] - df['equity_curve'].cummax()).min()
}])
by_symbol = df.groupby('symbol').agg(trades=('trade_id','count'), pnl=('net_pnl','sum'), win_rate=('net_pnl', lambda x: (x>0).mean())).reset_index().sort_values('pnl', ascending=False)
by_setup = df.groupby('setup').agg(trades=('trade_id','count'), pnl=('net_pnl','sum'), win_rate=('net_pnl', lambda x: (x>0).mean())).reset_index().sort_values('pnl', ascending=False)

(ROOT/'results').mkdir(exist_ok=True)
df.to_csv(ROOT/'results/trades_with_equity.csv', index=False)
summary.to_csv(ROOT/'results/trading_summary.csv', index=False)
by_symbol.to_csv(ROOT/'results/performance_by_symbol.csv', index=False)
by_setup.to_csv(ROOT/'results/performance_by_setup.csv', index=False)

plt.figure(figsize=(8,4))
plt.plot(df['date'], df['equity_curve'])
plt.title('Trading journal equity curve')
plt.xlabel('Date')
plt.ylabel('Cumulative PnL')
plt.tight_layout()
plt.savefig(ROOT/'results/equity_curve.png', dpi=160)

plt.figure(figsize=(8,4))
plt.bar(by_symbol['symbol'], by_symbol['pnl'])
plt.title('PnL by symbol')
plt.xlabel('Symbol')
plt.ylabel('Net PnL')
plt.tight_layout()
plt.savefig(ROOT/'results/pnl_by_symbol.png', dpi=160)

print(summary.to_string(index=False))
