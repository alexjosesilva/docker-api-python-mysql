from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def favorite_colors() -> List[Dict]:
    config = {
        'user': 'MYSQL_ROOT_USER',
        'password': 'MYSQL_ROOT_PASSWORD',
        'host': 'db',
        'port': '3306',
        'database': 'MYSQL_ROOT_DB'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')