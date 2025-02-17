from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    csv_file = '../data/weather_data.csv'
    if not os.path.exists(csv_file):
        return "Error: CSV file not found. Please run the scraper script first."

    try:
        df = pd.read_csv(csv_file)
        if df.empty:
            return "Error: CSV file is empty. Please run the scraper script to collect data."

        df.plot(kind='bar', x='Condition', y='Temperature', legend=None)
        plt.ylabel('Temperature')
        plt.title('Weather Data')
        plt.savefig('../static/plot.png')
        plt.close()
    except Exception as e:
        return f"An error occurred: {e}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)