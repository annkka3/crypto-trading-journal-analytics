# Crypto Trading Journal Analytics

    **Role:** Trading Data Analyst / Freelance Dashboard Specialist  
    **Dataset:** Synthetic / anonymized demo data created for portfolio use.  
    **Stack:** Python, pandas, Excel/Google Sheets dashboard, trading metrics

    ## Business problem

    A trader needs to understand whether their strategy is profitable and where the performance comes from: symbols, setups, long/short direction, timeframes, win rate and drawdown.

    ## What was built

    Built a trading journal analytics pipeline that calculates equity curve, total PnL, win rate, average win/loss, profit factor, max drawdown, symbol performance and setup performance.

    ## Key outputs

    - `results/trading_summary.csv` — high-level trading KPIs
- `results/performance_by_symbol.csv` — symbol-level analysis
- `results/performance_by_setup.csv` — setup-level analysis
- `results/equity_curve.png` and `pnl_by_symbol.png` — visual outputs
- optional workbook copy with Excel/Sheets dashboard portfolio

    ## How to run

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python src/main.py
    ```

    ## Resume-ready bullets

    - Built a crypto trading journal analytics project with PnL, win rate, profit factor, drawdown, equity curve and symbol/setup performance breakdowns.
- Created a dashboard-ready structure suitable for Excel, Google Sheets and freelance trading analytics projects.
