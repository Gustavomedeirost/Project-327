from flask import Flask, render_template, jsonify
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

# Carregar dados
data_path = os.path.join('data', 'sample_data.csv')
data = pd.read_csv(data_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Retornar dados em formato JSON
    return jsonify(data.to_dict(orient='records'))

@app.route('/plot')
def plot():
    # Criar um gráfico com Plotly
    fig = px.line(data, x='Date', y='Value', title='Gráfico de Valores ao Longo do Tempo')
    graph_html = fig.to_html(full_html=False)
    return render_template('graph.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
