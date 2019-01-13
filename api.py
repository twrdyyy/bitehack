from flask import Flask, request, render_template
from flask_restful import Resource, Api
from createDictionary import * 
import evaluate 

data = createDictionary()

app = Flask(__name__)
api = Api(app)

def applyParams(table,params):
    for key in data:
        for issue in data[key]:
            data[key][issue] *= float(params[issue])
    return table

class regions(Resource):
    def get(self):
        return data
class best(Resource):
    def get(self,paramSafety,paramHealth,paramEconomy):
        params = {'Safety':paramSafety,'Health':paramHealth,'Economy':paramEconomy}
        table = applyParams(data,params)
        return evaluate.best(table)

api.add_resource(regions, '/data')
api.add_resource(best,'/best/<paramSafety>/<paramHealth>/<paramEconomy>')

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
     app.run(port='5002')
