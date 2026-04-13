# A/B_testing_for_checkout_optimization
## Problem Statement
- This project checks the statistical significance of the newly created checkout page and its effect on conversion rate by performing A/B testing in Python.

## Dataset
- Kaggle [A/B testing dataset](https://www.kaggle.com/code/ramzanzdemir/ab-testing/input) (~290k users)

## Steps Performed
- Data cleaning (mismatch removal, duplicates)
- Data merging (country segmentation)
- Conversion rate analysis
- Hypothesis testing (Z-test)
- Confidence interval estimation

## Key Findings
- Conversion difference: ~ -0.15%
- p-value: ~0.19 (not significant)
- CI: (-0.00394 , 0.000781)
- CI includes 0 → inconclusive

## Business Conclusion
- New checkout page does NOT improve conversions → rollout not recommended

## Tools Used
- Python (Pandas, NumPy, Statsmodels)
- PyCharm IDE
