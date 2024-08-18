from flask import Flask, jsonify
from service.liquibase_service import LiquibaseService
from web.routes import web_blueprint
import logging
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Register Blueprints
app.register_blueprint(web_blueprint)

# Setup logging
logging.basicConfig(filename='logs/app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


# Initialize the LiquibaseService
liquibase_service = LiquibaseService()

@app.route('/update-db', methods=['POST'])
def update_db():
    try:
        output = liquibase_service.update_database()
        return jsonify({"status": "success", "message": output}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/db-status', methods=['GET'])
def db_status():
    try:
        output = liquibase_service.status()
        return jsonify({"status": "success", "message": output}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/rollback-db/<tag>', methods=['POST'])
def rollback_db(tag):
    try:
        output = liquibase_service.rollback(tag)
        return jsonify({"status": "success", "message": output}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    print("Templates folder path:", os.path.join(app.root_path, 'templates'))
    print("--------------------------------------------")
    app.run(debug=True)
