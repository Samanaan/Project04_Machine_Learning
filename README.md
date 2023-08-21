# Retail Price Optimization

**Contributors:** Greer Inns, Sarah Kim, Nolan Tonthat, Sam Spillane, Nazeli Mnatsakanyan, Jing Sy

![image](https://github.com/Samanaan/Project04_Machine_Learning/assets/125831024/873bc642-17a4-4938-b41a-b205d3b3f066)

## Problem/Objective

Setting the right price for products is essential to maximize profits and meet business goals. However, determining the optimal price for each product can be a very complex and time-consuming task. The challenge that many businesses face is being able to efficiently leverage the data to make informed pricing decisions that find the balance between profitability and market demand.

## Solution

We plan to address this problem by utilizing a linear regression model to analyze products and categories, competitive pricing, and customer ratings from the Amazon Product Sales Dataset to accurately recommend optimal prices for various products. This will enable retailers to make strategic business decisions.

## Process

### 1. ETL/EDA

- Utilize `Pandas`:
  - Load data, basic exploration (data structure), data cleaning (e.g., `df.isnull()`), data transformation (e.g., `df.drop`, `pd.to_datetime`, `df.sort`)
- Utilize `Matplotlib`, `Seaborn`:
  - Visualize and identify overall trends and patterns before building models
    - Correlation Heatmap
    - Total Price by Quantity Sold
    - Total Price by Quantity Sold in Garden Tools
    - Sales Volume, Revenue, and Customers Across the Product Categories

![Image 1](https://github.com/Samanaan/Project04_Machine_Learning/assets/125831024/065dd698-0f09-493b-a3e9-b2f9c1e70802)

![Image 2](https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/b2eb40a8-1e3b-462b-9aa2-3e70185e975d)

![Image 3](https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/8a77947b-53d0-44e9-b186-9225e06bfd99)

### 2. Build, Train, Test, Evaluate ML Models

We initially tested both cumulative and moving window train/test selection methods: 


<img width="873" alt="Screenshot 2023-08-21 at 12 47 43 PM" src="https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/765f867f-fcc5-49c8-933d-25df23d24873">

![Cumulative Selection](https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/8263e1e0-8cce-4adf-835d-cf9bc0f0c0d9)


We utilized three supervised machine learning models to evaluate optimal price points:

#### Linear Regression

- Step 1: Define Window Size (5)
- Step 2: Group by product and set features/target variable
- Step 3: Sliding Window training and testing to predict data points
- Step 4: **Linear Regression Model Training** using training data (features_train, target_train)
- Step 5: Unit price predictions (features_test)
- Step 6: Evaluate using Mean Squared Error (MSE) - actual vs. predicted
- Step 7: Calculate avg predicted price and MSE and loop to find price with min MSE (Optimal Price)
![Linear Regression](https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/e06d583d-e1ee-4e3c-9dcf-3e3d638048eb)

#### Random Forest

- Step 1: Define Window Size (5)
- Step 2: Group by product and set features/target variable
- Step 3: Sliding Window training and testing to predict data points
- Step 4: **Random Forest Regressor Model Training** using training data (features_train, target_train)
- Step 5: Unit price predictions (features_test)
- Step 6: Evaluate using Mean Squared Error (MSE) - actual vs. predicted
- Step 7: Calculate avg predicted price and MSE and loop to find price with min MSE (Optimal Model for Predicting Price)

![Random Forest](https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/18b0b2df-9d4e-45ef-b97d-ec3da3493460)

#### XGBoost

- Step 1: Define Window Size (5)
- Step 2: Group by product and set features/target variable
- Step 3: Sliding Window training and testing to predict data points
- Step 4: Create an **XGBoost regression model** with 50 estimators and a fixed random state
- Step 5: Unit price predictions (features_test)
- Step 6: Evaluate using Mean Squared Error (MSE) - actual vs. predicted
- Step 7: Calculate avg predicted price and MSE and loop to find price with min MSE (Optimal Model for Predicting Price)

![XGBoost](https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/4e130edf-0d3a-40d6-92e7-150317d3604e)

### 4. Export all data and visualize Model Performance/Evaluation

- Visualize overall EDA process
- Visualize and compare Model accuracy across all 3 methods
- Visualize Model performance across iterations/samples

![Model Performance](https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/63732e85-4809-4631-9cf8-e72ac8bd47f2)

See Public Dashboard: https://public.tableau.com/app/profile/jing.sy/viz/Price_Optimization_Final/Dashboard1


