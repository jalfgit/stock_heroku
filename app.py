from flask import Flask,render_template,jsonify,url_for
import pandas as pd
import json
# from flask_sqlalchemy import SQLAlchemy # db enabled
from sqlalchemy import create_engine
# import yfinance as yf

# db enabling the app.py
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)

# engine = create_engine(db)

# results=engine.execute('select * from sales')

# sales_df=pd.read_sql('select * from sales',engine)

# sales_stats={
#     'rows':sales_df,
#     'total':sales_df['revenue'].sum(),
#     'num_clients':sales_df['client'].unique()
# }

@app.route('/')
def hello_world():
    return '<h1>Hi there!</h2>Hello, <b>World</b>!'

@app.route('/welcome/')
def render_index():
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["A", "B"])
    a=100
    return render_template('index.html',a=a,df=df)

@app.route('/json/')
def return_json():
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["A", "B"])
    return jsonify(df.to_dict())
    # return jsonify(df_yf.to_dict())


@app.route('/csv/read')
def return_csv_data():
    names=pd.read_csv('./static/data/data.csv')
    return jsonify(names.to_dict())


@app.route('/csv/read2')
def return_csv_data2():
    names=pd.read_csv('./static/data/data.csv')
    custom_names={
        "names":list(names['name'].values),
        "qty":[float(x) for x in names['qty'].values]
    }
    return jsonify(custom_names)


@app.route('/db_2/<table>/<n>')
def return_db_tables(table):
    sql_code="select * from " + table + " limit " + n
    df=pd.read_sql(sql_code)
    return jsonify(df.to_dict())

@app.route('/db/<table>/<n>')
def return_dynamic_route(table,n):
    return f'<h1>You have selected</h2><b>{table} with {n} rows limit</b>!'

@app.route('/json/pd')
def return_pd():
    return jsonify(sales_df.to_dict())

@app.route('/json/custom')
def return_custom():
    return jsonify(sales_stats)    


if __name__ == "__main__":
    app.run(debug=True)