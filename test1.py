# 初始化参数
initial_capital = 100000  # 初始本金
growth_rate_A = 0.175  # 策略A的年增长率
growth_rate_B = 0.175  # 策略B主账户的年增长率
speculative_growth_rate = 0.60  # 投机账户的年增长率
speculative_addition_annual = 10000  # 每年加入投机账户的金额
years = 30  # 投资年数

# 策略A计算
capital_A = initial_capital
results_A = []
for year in range(years):
    capital_A *= (1 + growth_rate_A)
    results_A.append(capital_A)

# 策略B计算
capital_B = initial_capital
speculative_capital = 0  # 投机账户初始本金
results_B = []
for year in range(1, years + 1):
    if year > 1:
        # 从第二年开始，每年从主账户中扣除1万美元用于投机
        capital_B -= speculative_addition_annual
        # 投机账户的收益
        speculative_profit = speculative_capital * speculative_growth_rate
        # 投机账户收益并入主账户
        capital_B += speculative_profit
        # 更新投机账户本金
        speculative_capital += speculative_addition_annual
    capital_B *= (1 + growth_rate_B)
    results_B.append(capital_B)

# 打印结果
print("策略A的结果：")
for year, capital in enumerate(results_A, 1):
    print(f"第{year}年: ${capital:,.2f}")

print("\n策略B的结果：")
for year, capital in enumerate(results_B, 1):
    print(f"第{year}年: ${capital:,.2f}")
