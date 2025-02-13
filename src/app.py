from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('../data/weather_data.csv')
    df.plot(kind='bar', x='Condition', y='Temperature', legend=None)
    plt.ylabel('Temperature')
    plt.title('Weather Data')
    plt.savefig('../static/plot.png')
    plt.close()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)