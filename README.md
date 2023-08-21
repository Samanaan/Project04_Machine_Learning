# Retail Price Optimization

*Contributors: Greer Inns, Sarah Kim, Nolan Tonthat, Sam Spillane, Nazeli Mnatsakanyan, Jing Sy*

![image](https://github.com/Samanaan/Project04_Machine_Learning/assets/125831024/873bc642-17a4-4938-b41a-b205d3b3f066)


### Problem/Objective: 

Setting the right price for products is essential to maximize profits and meet business goals. However, determining the optimal price for each product can be a very complex and time-consuming task. The challenge that many businesses face is being able to efficiently leverage the data to make informed pricing decisions that finds the balance between profitability and market demand.

### Solution:

We plan to address this problem by utilizing a linear regression model to analyze products and categories, competitive pricing, and customer ratings from the Amazon Product Sales Dataset to  accurately recommend optimal prices for various products. This will enable retailers to make strategic business decisions.

### Process:

1. ETL/EDA
   - Utilize `Pandas`: Load data, basic exploration (data stucture), data cleaning (e.g., `df.isnull()`), data transformation (e.g., `df.drop`. `pd.to_datetime`, `df.sort()`),
   - Utilize `Matplotlib`, `Seaborn`: Visualize and idenitfy overall trends and patterns before building models

      <img width="655" alt="image" src="https://github.com/Samanaan/Project04_Machine_Learning/assets/125831024/065dd698-0f09-493b-a3e9-b2f9c1e70802">
<img width="497" alt="Screenshot 2023-08-21 at 11 55 52 AM" src="https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/b2eb40a8-1e3b-462b-9aa2-3e70185e975d">

2. Build, Train, Test, Evaluate ML Models (`Linear Regression` (Sliding Window, Cumulative Training), `Random Forest`, `XGBoost`)

Sliding Window Optimization:


<img width="467" alt="Screenshot 2023-08-21 at 11 57 06 AM" src="https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/bcde7ca7-6195-44d9-83e2-d641d9dd4b2e">


Cumulative Training Structure:


<img width="640" alt="Screenshot 2023-08-21 at 11 56 54 AM" src="https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/8263e1e0-8cce-4adf-835d-cf9bc0f0c0d9">

    **Linear Regression Models:**
   - Step 1: Define Window Size (5)
   - Step 2: Group by product and set features/target variable
   - Step 3: Sliding Window training and testing to predict data points
   - Step 4: **Linear Regression Model Training** using training data (features_train, target_train)
   - Step 5: Unit price predictions (features_test)
   - Step 6: Evaluate using Mean Squared Error (MSE) - actual vs. predicted
   - Step 7: Calculate avg predicted price and MSE and loop to find price with min MSE
        → Optimal Price

    **Random Forest Model:**
    - Step 1: Define Window Size (5)
    - Step 2: Group by product and set features/target variable
    - Step 3: Sliding Window training and testing to predict data points
    - Step 4: **Random Forest Regressor Model Training** using training data (features_train, target_train)
    - Step 5: Unit price predictions (features_test)
    - Step 6: Evaluate using Mean Squared Error (MSE) - actual vs. predicted
    - Step 7: Calculate avg predicted price and MSE and loop to find price with min MSE
        → Optimal Model for Predicting Price

      Random Forest Structure:
<img width="417" alt="Screenshot 2023-08-21 at 11 59 43 AM" src="https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/18b0b2df-9d4e-45ef-b97d-ec3da3493460">

    **XGBoost Model:**
    - Step 1: Define Window Size (5)
    - Step 2: Group by product and set features/target variable
    - Step 3: Sliding Window training and testing to predict data points
    - Step 4: Create an **XGBoost regression model** with 50 estimators and a fixed random state
    - Step 5: Unit price predictions (features_test)
    - Step 6: Evaluate using Mean Squared Error (MSE) - actual vs. predicted
    - Step 7: Calculate avg predicted price and MSE and loop to find price with min MSE
        → Optimal Model for Predicting Price

      XGBoost Structure:
  <img width="922" alt="Screenshot 2023-08-21 at 11 59 54 AM" src="https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/4e130edf-0d3a-40d6-92e7-150317d3604e">

4. Export all data and visualize Model Performance/Evaluation
      - Visualize overall EDA process
      - Visualize and compare Model accuracy accross all 4 methods
      - Visualize Model performace across iterations/samples
     
   <img width="1072" alt="Screenshot 2023-08-21 at 12 00 18 PM" src="https://github.com/Samanaan/Project04_Machine_Learning/assets/47437697/63732e85-4809-4631-9cf8-e72ac8bd47f2">

