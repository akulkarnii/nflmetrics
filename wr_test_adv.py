import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

'''
Simple Correlation Calculations

    DYAR           PPA/All       PPA/Pass
REC	0.305848831		
YDS	0.554249513		
TD	0.457924514		
FP		         0.326174444	0.336726373
		         0.486122705	0.481064941

'''

if __name__ == '__main__':
    data = pd.read_csv('wr_stats/cfb_nfl_wr.csv')

    ### 0.5 FP ###
    # OK correlation - decent predictive power

    '''
    data = data.drop(["player", "school", "conf", "team", 'g', 'rec', 'yds', 'avg', 'td', 'dyar'], axis=1)
    x = data[['averagePPA.all', 'averagePPA.pass']]
    y = data['points']
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

    ##### DYAR #####
    # Better correlation - worse RMSE for prediction

    data = pd.read_csv('wr_stats/cfb_nfl_wr.csv')

    data = data.drop(["player", "school", "conf", "team", 'g', 'rec', 'yds', 'avg', 'td', 'points'], axis=1)
    data = data.drop(data[data.dyar == 0].index)
    x = data[['averagePPA.all', 'averagePPA.pass']]
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