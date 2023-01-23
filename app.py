import os
from flask import Flask, render_template, request
from elasticapm.contrib.flask import ElasticAPM
import logging

app = Flask(__name__)
logging.basicConfig(filename='flask.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


app.config['ELASTIC_APM'] = {

  'SERVICE_NAME': 'app_flask',


  'SECRET_TOKEN': '',
  'DEBUG': True,

# # # Set the custom APM Server URL (default: http://localhost:8200)
  'SERVER_URL': 'http://localhost:8200',

# # # Set the service environment
  'ENVIRONMENT': 'dev',
  }

apm = ElasticAPM(app)
@app.route("/")
def hello_world():
    try:
        return "madruga boladona"
    except Exception as err:
        return app.logger.critical(err)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
