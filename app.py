from flask import Flask,request
from MongoUtils import MongoDBConnection


mycoll =  MongoDBConnection('uniqueRecipe','food-items','mongodb://localhost:27017/').create_connection()

app = Flask(__name__)


env = {
    'name' : 'foodenv',
    'version': 'V1.0'
}




@app.route('/')
def greet():
    return f"{env['name']} is UP & RUNNING with version : {env['version']}"

@app.get('/api/food/<int:id>')
def get_food_item(id):
    if mycoll is not None:
        data = mycoll.find_one({'id':id})
        if data:
            return data
        return 'Food item not found.'
    return 'Service is not available.'


@app.get('/api/foods/')
def get_food_items():
    if mycoll is not None:
        data = list(mycoll.find())
        return {'foods': data}
    return 'Service is not available.'


@app.post('/api/food/')
def save_food_item():
    if mycoll is not None:
        data = request.json
        response = mycoll.insert_one(data)
        return f' data inserted successfully {response.acknowledged} {response.inserted_id}'
    return f'Service is not avaiable....'

@app.post('/api/foods/')
def save_food_items():
    if mycoll is not None:
        data = request.json
        response = mycoll.insert_many(data)
        return f'Data inserted successfully: {response.acknowledged} {response.inserted_ids}'
    return 'Service is not available.'

@app.put('/api/food/<int:id>')
def update_food_item():
    if mycoll is not None:
        data = request.json
        response = mycoll.update_one({'id': id}, {'$set': data})
        if response.modified_count > 0:
            return f'Food item updated successfully.'
        return 'Food item not found.'
    return 'Service is not available.'

@app.delete('/api/food/<int:id>')
def delete_food_item():
    if mycoll is not None:
        response = mycoll.delete_one({'id': id})
        if response.deleted_count > 0:
            return f'Food item deleted successfully.'
        return 'Food item not found.'
    return 'Service is not available.'


if __name__ == '__main__':
    # create db connection..

    app.run(debug=True,port=1333)