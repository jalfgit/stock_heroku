from flask import Flask,render_template,jsonify,url_for
import pandas as pd
import json
from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy # db enabled
from sqlalchemy import create_engine
# import yfinance as yf

import glob
import os
from string import Template
import sys


# db enabling the app.py
app = Flask(__name__)

password="datascience"

db_path='sqlite:///./data/db.sqlite'

engine=create_engine(db_path)

basedir = os.path.abspath(os.path.dirname(__file__)) # works well
# print(basedir)
print(f'Directory {basedir}', file=sys.stderr)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/db.sqlite'
# db = SQLAlchemy(app)

# engine = create_engine(db)

# sales_df=pd.read_sql('select * from sales',engine)

# sales_stats={
#     'rows':sales_df,
#     'total':sales_df['revenue'].sum(),
#     'num_clients':sales_df['client'].unique()
# }

@app.route('/')
def hello_world():
    if password=="datascience":
        return '<h1>Hi there!</h2>Hello, <b>World</b>!'
    else:
        return '<H1>SERVER UNDER MAINTENANCE</H1>'

@app.route('/welcome/')
def render_index():
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["A", "B"])
    a=100
    if password=="datascience":
        return render_template('index.html',a=a,df=df)
    else:
        return render_template('error.html',a=a,df=df)
    

@app.route('/json/')
def return_json():
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["A", "B"])
    return jsonify(df.to_dict())
    # return jsonify(df_yf.to_dict())


@app.route('/csv/read')
def return_csv_data():
    names=pd.read_csv('./data/data.csv')
    return jsonify(names.to_dict())


@app.route('/csv/read2')
def return_csv_data2():
    names=pd.read_csv('./data/data.csv')
    custom_names={
        "names":list(names['name'].values),
        "qty":[float(x) for x in names['qty'].values]
    }
    return jsonify(custom_names)


@app.route('/db/<table>/<n>')
def return_dynamic_route(table,n):
    print("connecting engine")
    global engine
    conn=engine.connect()
    sql_code=f"""
    insert into db_use
    values ('{datetime.now().strftime("%Y-%m-%d %T")}','{table}')
    """
    # print(sql_code)
    conn.execute(sql_code)
    # conn.commit()
    conn.close()
    return f'<h1>You have selected</h2><b>{table} with {n} rows limit</b>!'

@app.route('/json/pd')
def return_pd():
    return jsonify(sales_df.to_dict())

@app.route('/json/custom')
def return_custom():
    return jsonify(sales_stats)    

@app.route('/sql/<table>/<n>')
def return_sql_report(table,n):
    f_path=basedir+'/static/SQL/'+'*.sql'
    sql_files=read_directory(basedir+'/static/SQL/','*.sql')
    # print(sql_files)
    sql_strings=[]
    df_master=[]
    sql_example=''
    global engine
    conn=engine.connect()

    for sql_f in sql_files:
        print("sqtringsddssfs")
        sql_example=load_SQL(sql_f)
        t=Template(load_SQL(sql_f))
        sql_strings.append(t.substitute(SYMBOL=table,n=n).replace("\n",""))
        
    for sql_s in sql_strings:
        df=pd.read_sql(sql_s,conn)
        df_master.append(df)
    
    conn.close()
    
    return render_template("sqlreport.html",dfs=df_master,sqls=sql_strings)
    # return f"""
    #     returning data for {table} and {n}<br>\nBaseDir:{basedir}\n<br>Other:{app.instance_path}\n{f_path}
    #     <br>
    #     {sql_files}
    #     <br><b>Resulting SQL: </b><br>{sql_example}
    #     <br><b>Replacement SQL: </b><br>{sql_strings}

    # """

def read_directory(path:str,file_types:str="*.sql"):
    """[summary]
    needs glob library to read directory
    Args:
        path (str): [description]
        file_types (str, optional): [description]. Defaults to "*.sql".
    """
    files_in_dir=glob.glob(path+file_types)
    for file in files_in_dir:
        print(f'File found: {file}')
    return files_in_dir

def load_SQL(filename:str):
    """
    input: filename:str
    output: string object
    """
    with open(filename, "r") as file_handle:
        contents=file_handle.read()
        return contents



if __name__ == "__main__":
    app.run(debug=True)