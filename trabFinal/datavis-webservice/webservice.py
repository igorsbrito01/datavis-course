from flask import Flask
from flask_restful import Resource,Api
from flask_restful import reqparse
from pymongo import MongoClient 

app = Flask(__name__)

api = Api(app)

connection = MongoClient('localhost', 27017)

db = connection['ufcdatavis']

#??
parser = reqparse.RequestParser()

#Collections:
#dishes, menus e itens_menu

class Location(Resource):

	# For now return just the restaurants, 
	# Waiting for the database modifications so it can return the restaurant identification with coordenates
	@staticmethod
	def get():

		menu_collection = db['menus']

		data = menu_collection.find({}, {'_id': False})

		restaurents = []

		for element in data:
			if element['name'] != "":
				restaurents.append(element)
		# 	#restaurents.insert({'name':element.name, 'lat':element.lat,'lon':element.lon})	
		# 	restaurents.insert({'name':element.name, 'sponsor': element.sponsor,'location':element.location})

		return restaurents

class ItensRestaurant(Resource):

	#return itens of one restaurante - recive as parameter the restaurant id
	@staticmethod
	def get(id_place):

		print type(id_place)

		itens_menu_collection = db['itens_menu']

		data = itens_menu_collection.find({'menu_id':int(id_place)},{'_id':False})

		print data.count()
		itens = []

		for element  in data:
			itens.append(element)

		return itens

# For now return just the restaurants, 
# Waiting for the database modifications so it can return the restaurant identification with coordenates
api.add_resource(Location, '/locations/', endpoint='get_locations')

#return itens of one restaurante - recive as parameter the restaurant id
api.add_resource(ItensRestaurant, '/restaurant/itens/<string:id_place>/', endpoint='dishes')

app.run(host='0.0.0.0', port=8000, debug=True)