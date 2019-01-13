from flask import Flask, request, render_template
from flask_restful import Resource, Api
from createDictionary import * 
import copy
# from normalizer import normalize
from functools import reduce
import evaluate 

data = createDictionary()
print(data)

app = Flask(__name__)
api = Api(app)

def applyParams(data_,params):
    table = copy.deepcopy(data_)
    if reduce((lambda x,y:int(x)*int(y)),list(params.values()))==1:
        return table
    for key in table:
        for issue in table[key]:
            table[key][issue] *= float(params[issue])
    return table

class regions(Resource):
    def get(self):
        return data
class regionsApplied(Resource):
    def get(self,paramSafety,paramHealth,paramEconomy):
        params = {'Safety':paramSafety,'Health':paramHealth,'Economy':paramEconomy}
        table = applyParams(data,params)
        return table

class best(Resource):
    def get(self,paramSafety,paramHealth,paramEconomy):
        params = {'Safety':paramSafety,'Health':paramHealth,'Economy':paramEconomy}
        table = applyParams(data,params)
        return evaluate.best(table)

api.add_resource(regions, '/data')
api.add_resource(best,'/best/<paramSafety>/<paramHealth>/<paramEconomy>')
api.add_resource(regionsApplied,'/table/<paramSafety>/<paramHealth>/<paramEconomy>')
@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
     app.run(port='5002')
