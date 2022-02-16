import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

if __name__ == '__main__':
    data = pd.read_csv('wr_stats/cfb_nfl_wr.csv')


    ### 0.5 FP ###
    # OK correlation - decent predictive power

    data = data.drop(["player", "school", "conf", "team", 'g', 'avg', 'dyar'], axis=1)
    x = data[['yds', 'rec', 'td']]
    y = data['points']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

    #Correlation
    print(data.corr(method='pearson')) # Pearson's r - look at last row

    # Regression
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    coeff_df = pd.DataFrame(regressor.coef_, x.columns, columns=['Coefficient'])
    print(coeff_df)

    # Prediction
    y_pred = regressor.predict(x_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(df)

    # Analysis
    print(data.describe())
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    '''
    ### Per Game ###
    # Least predictive - bad correlation
    
    data = data.drop(["player", "school", "conf", "team", 'g', 'avg', 'yds', 'rec', 'td'], axis=1)
    x = data[['ypg', 'rpg', 'tdpg']]
    y = data['points']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # Correlation
    print(data.corr(method='pearson'))  # Pearson's r - look at last row

    # Regression
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    coeff_df = pd.DataFrame(regressor.coef_, x.columns, columns=['Coefficient'])
    print(coeff_df)

    # Prediction
    y_pred = regressor.predict(x_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(df)
    '''

    '''
    ##### DYAR #####
    # Better correlation - worse RMSE for prediction
    
    data = pd.read_csv('wr_stats/cfb_nfl_wr.csv')

    data = data.drop(["player", "school", "conf", "team", 'g', 'avg', 'points'], axis=1)
    data = data.drop(data[data.dyar == 0].index)
    x = data[['yds', 'rec', 'td']]
    y = data['dyar']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

    # Correlation
    print(data.corr(method='pearson'))  # Pearson's r - look at last row

    # Regression
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    coeff_df = pd.DataFrame(regressor.coef_, x.columns, columns=['Coefficient'])
    print(coeff_df)

    # Prediction
    y_pred = regressor.predict(x_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(df)

    # Analysis
    print(data.describe())
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    '''



