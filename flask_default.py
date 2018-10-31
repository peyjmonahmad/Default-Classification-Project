

from flask import Flask
from flask_restplus import Api
from flask_restplus import fields
from sklearn.externals import joblib

app = Flask(__name__) # create instance of Flask class

# runs as default if you $python app.py, instead of a module: http://thepythonguru.com/what-is-if-__name__-__main__/
api = Api(app,title='Loan Default Predictor',description='Type in some basic information to see if you are more likely to default or honor your loan!')

ns = api.namespace('Please enter the following information',description='Default or no default')

# Add all the features that we want to input a number
parser= api.parser()
parser.add_argument('Duration',type=int,required=True,help='Duration of loan in months',location='form')

parser.add_argument('Savings',type=int,required=True,help='Balance of savings account at the time of receiving the loan',location='form')

parser.add_argument('Years at Job',type=float,required=True,help='Number of years at current employment',location='form')

parser.add_argument('Age',type=int,required=True,help='Age of loan applicant',location='form')

resource_fields = api.model('Resource',{'result':fields.String,})

from flask_restplus import Resource

#initialize the route so we can post here.
@ns.route('/',methods=['POST'])
class CreditApi(Resource):
	@api.doc(parser=parser)
	@api.marshal_with(resource_fields)
	def post(self):
		args = parser.parse_args()
		result = self.get_result(args)

		return result

#We can upload the model and made predictions based on the data given
	def get_result(self,args):
		duration = args['Duration']
		savings_acc = args['Savings']
		years_employed = args['Years at Job']
		age = args['Age']

		from pandas import DataFrame
		df = DataFrame([[duration,savings_acc,years_employed,age]])

		clf = joblib.load('DataScience/metis/knn_model')
		print('Made it here')



		result = clf.predict(df)
		if(result[0] == 1):
			result = 'DEFAULT...No more loans for you buddy.'

		else: 
			result = "NO DEFAULT.  You're all good!"

		return {'result':result}

if __name__ == '__main__':
	app.run(debug=True)