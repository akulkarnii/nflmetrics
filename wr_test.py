import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    data = pd.read_csv('cfb_nfl_wr.csv')
    # data.plot(x='yds', y='points', style='o')
    # plt.title('CFB Yards vs NFL Prod')
    # plt.xlabel('CFB Yards')
    # plt.ylabel('NFL Fantasy Points')
    # plt.show()

    data = data.drop(["player", "school", "conf", "team"], axis=1)
    x = data[['yds', 'rec', 'td']]
    y = data['points']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

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




