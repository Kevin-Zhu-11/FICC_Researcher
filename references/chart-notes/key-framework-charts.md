# Key Framework Charts

This file reconstructs important visual frameworks in text so the skill can still use them when image URLs expire.

## 中金债券组合构建框架

- Source report: `cicc-bond-principles-strategy-2025`
- Original image URL: Source Markdown uses MinerU CDN image links; verify the exact URL in the source report before quoting.
- Core message: Bond portfolio construction links macro, liquidity, regulation, supply, investor demand, yield curve, credit spreads, leverage, and portfolio constraints into one decision chain.
- Use when: The user asks how to build a bond portfolio, choose duration, compare rates and credit, or explain why investor demand matters.
- Do not use when: The user needs live holdings, current yield levels, or trade execution without current data.
- Text reconstruction:

```text
economic fundamentals / inflation / liquidity / regulation
+ product supply / bond issuance / fiscal supply
+ investor demand / liability constraints / risk appetite
-> yield-curve level and slope
-> credit spread and liquidity premium
-> duration, curve, leverage, and credit allocation
-> portfolio return, drawdown, liquidity, and mandate fit
```

## 华泰投资者行为图谱

- Source report: `huatai-institution-behavior-2025`
- Original image URL: Source Markdown uses MinerU CDN image links; verify the exact URL in the source report before quoting.
- Core message: Financing demand and policy conditions reshape bank balance sheets and non-bank liabilities, then feed into bond-market demand across rates, credit, short-end, and long-end assets.
- Use when: The user asks why banks, wealth management, funds, insurance, or foreign investors move rates or credit spreads.
- Do not use when: The user needs an institution's exact current holdings or flows without data.
- Text reconstruction:

```text
financing demand and macro policy
-> bank deposits, loan demand, NCD funding, balance-sheet pressure
-> wealth management, funds, insurance, broker books, foreign investors
-> allocation demand by tenor, rating, liquidity, accounting category
-> rates, credit spreads, repo leverage, redemption feedback
```

## 华泰信用债品种演化图

- Source report: `huatai-credit-bond-framework-2025`
- Original image URL: Source Markdown uses MinerU CDN image links; verify the exact URL in the source report before quoting.
- Core message: China's credit-bond market evolved from enterprise bonds and commercial paper toward ABS, corporate bonds, MTNs, SCP, PPN, private company bonds, public REITs, TLAC, and technology-board instruments.
- Use when: The user asks what counts as credit bonds, why instruments have different investor bases, or how product evolution affects credit strategy.
- Do not use when: The task requires current issuance size by product without a data source.
- Text reconstruction:

```text
early enterprise bonds and short-term financing bills
-> corporate bonds, MTN, SCP, PPN, ABS
-> private placement and exchange products
-> public REITs, TLAC, technology and innovation bonds
-> differentiated credit risk, liquidity, regulation, and investor demand
```

## 华泰 IS-LM 利率理论图

- Source report: `huatai-bond-market-framework-2025`
- Original image URL: Source Markdown uses MinerU CDN image links; verify the exact URL in the source report before quoting.
- Core message: Rates can be understood as the internal price of funds, but practical bond analysis must translate theory into observable growth, inflation, policy, funding, and supply-demand indicators.
- Use when: The user asks for a theoretical explanation of interest rates or how macro theory maps to bond trading.
- Do not use when: The question is purely about credit issuer risk or convertible terms.
- Text reconstruction:

```text
goods market and money market equilibrium
-> aggregate demand, money supply, funding preference, policy reaction
-> short-rate anchor and long-rate expectation
-> observable indicators: growth, inflation, credit, repo, policy rates, bond supply, investor demand
```

## 转债条款/估值/择券框架图

- Source report: `cicc-convertible-bonds-framework-2025`, `huatai-convertible-framework-2025`
- Original image URL: Source Markdown uses MinerU CDN image links; verify the exact URL in the source report before quoting.
- Core message: Convertible value comes from underlying equity, bond floor, conversion premium, implied option value, and clauses such as redemption, put, and downward revision.
- Use when: The user asks whether to focus on parity premium, bond floor, clauses, or equity beta.
- Do not use when: The instrument terms are unknown or the asset is not actually convertible/exchangeable.
- Text reconstruction:

```text
underlying stock price and volatility
+ conversion price and parity
+ bond floor and issuer credit
+ conversion premium and implied option value
+ redemption / put / downward revision clauses
-> equity-like, balanced, debt-like, or event-driven strategy
```

## 城投债区域分析框架

- Source report: `cicc-city-investment-bonds-2025`
- Original image URL: See `references/chart-notes/image-url-index.yml` after running `scripts/extract_image_urls.py`.
- Core message: City investment bond analysis should combine regional fiscal capacity, debt pressure, platform function, refinancing path, policy support, and market spread.
- Use when: The user asks about 化债, 区域利差, 城投平台, 隐性债务, or regional credit selection.
- Do not use when: The user needs a live issuer spread or current policy event without data.
- Text reconstruction:

```text
regional fiscal capacity
+ explicit and hidden debt pressure
+ platform public-service function and cash flow
+ refinancing access and policy support
+ market spread and liquidity
-> regional beta, issuer selection, maturity choice, or avoid
```

## 大金融信用债资本工具框架

- Source report: `cicc-financial-credit-bonds-2025`
- Original image URL: See `references/chart-notes/image-url-index.yml` after running `scripts/extract_image_urls.py`.
- Core message: Financial credit requires separate analysis of issuer fundamentals and instrument-level subordination or loss-absorption terms.
- Use when: The user asks about 二永债, TLAC, 银行资本债, 券商债, or 保险资本工具.
- Do not use when: The question only needs generic senior credit spread comparison.
- Text reconstruction:

```text
issuer systemic role and fundamentals
+ capital adequacy and regulatory pressure
+ instrument ranking, extension, coupon, write-down terms
+ investor demand and secondary liquidity
-> spread compensation for financial capital tools
```

## 理财净值化赎回反馈链条

- Source report: `cicc-wealth-management-net-value-2025`, `huatai-institution-behavior-2025`
- Original image URL: See `references/chart-notes/image-url-index.yml` after running `scripts/extract_image_urls.py`.
- Core message: Net-value wealth products transmit market losses into redemption behavior, liquidity management, and bond-market selling pressure.
- Use when: The user asks why wealth-management redemptions affect credit bonds or short-end rates.
- Do not use when: Product NAV, shares, holdings, and liquidity terms are unavailable and the user wants a current conclusion.
- Text reconstruction:

```text
market drawdown
-> product NAV pressure and investor redemption
-> manager raises liquidity and reduces risk
-> sells liquid rates / high-grade credit / NCD / funds
-> spread widening, short-end pressure, and further NAV feedback
```

## 利率衍生品基差/IRR 框架

- Source report: `cicc-interest-rate-derivatives-2025`
- Original image URL: See `references/chart-notes/image-url-index.yml` after running `scripts/extract_image_urls.py`.
- Core message: Futures basis and IRR depend on cash bond, conversion factor, funding, delivery option, and liquidity.
- Use when: The user asks about 国债期货, CTD, 基差, IRR, or hedging.
- Do not use when: The task lacks futures price, cash bond data, or funding cost but asks for trade implementation.
- Text reconstruction:

```text
cash bond price and yield
+ conversion factor and CTD choice
+ futures price and delivery timing
+ repo funding cost and margin
-> basis, implied repo, hedge ratio, and roll/delivery risk
```

## ABS/REITs 现金流与估值框架

- Source report: `cicc-abs-framework-2025`, `cicc-public-reits-strategy-2025`
- Original image URL: See `references/chart-notes/image-url-index.yml` after running `scripts/extract_image_urls.py`.
- Core message: ABS and REITs analysis starts from asset cash flow, structure, enhancement, operation quality, rates, valuation, and liquidity.
- Use when: The user asks about ABS tranche risk, REITs distribution, asset cash flow, or structured-product valuation.
- Do not use when: The user only has headline yield but no asset-pool or project data.
- Text reconstruction:

```text
underlying asset or project cash flow
+ waterfall / tranche priority / enhancement
+ operation quality, prepayment/default, or NOI
+ rates curve, spread, distribution yield, liquidity
-> valuation, drawdown risk, and cash-flow resilience
```
