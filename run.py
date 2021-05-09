from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "staging":
    app.config.from_object("config.StagingConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")


#hello world api
import resources.sample.helloworld as hw
api.add_resource(hw.HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True,port=app.config["API_PORT"])