import pandas as pd

# 加载数据
file_path = '/Users/jiachengding/PycharmProjects/quant/IDCBY.csv'
df = pd.read_csv(file_path)

# 将日期列转换为DateTime对象
df['Date'] = pd.to_datetime(df['Date'])

# 计算布林带
df['Middle_Band'] = df['Close'].rolling(window=20).mean()
df['STD'] = df['Close'].rolling(window=20).std()
df['Upper_Band'] = df['Middle_Band'] + (df['STD'] * 1)
df['Lower_Band'] = df['Middle_Band'] - (df['STD'] * 1)

# 初始化变量
initial_capital = 10000
capital = initial_capital
shares = 0
buy_price = 0

# 遍历每一行数据
for index, row in df.iterrows():
    # 买入条件：收盘价低于布林下沿且当前无仓位
    if row['Close'] < row['Lower_Band'] and shares == 0:
        shares = capital / row['Close']
        buy_price = row['Close']
        print(f"Bought at {buy_price} on {row['Date'].date()}")

    # 检查卖出条件：接下来几个交易日内有盈利机会
    if shares > 0:
        sell_signal = False
        for future_index in range(index + 1, min(index + 4, len(df))):
            future_row = df.iloc[future_index]
            # 检查是否有盈利机会：收盘价或开盘价超过买入价
            if future_row['Close'] >= buy_price * 1.02 or future_row['Open'] >= buy_price * 1.02:
                sell_signal = True
                sell_price = max(future_row['Close'], future_row['Open'])  # 选择收盘价或开盘价中更高的一个来卖出
                break

        if sell_signal:
            capital = shares * sell_price
            print(f"Sold at {sell_price} on {future_row['Date'].date()} | New capital: {capital}")
            shares = 0  # 卖出后，等待下一次买入的机会

# 最终资金结果
print(f"Final capital: {capital}, Performance: {(capital - initial_capital) / initial_capital * 100}%")
