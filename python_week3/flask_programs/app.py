from flask import Flask, jsonify, request
from person_dao import Person, Db_operations

persons = Db_operations()
persons.create_table()

app = Flask(__name__)

@app.route('/persons', methods=['POST'])
def persons_create():
    body = request.get_json()
    # FIXED: Correct parameter order: name, gender, dob, location
    new_person = Person(body['name'], body['gender'], body['dob'], body['location'])
    id = persons.insert_row(new_person)
    person = persons.search_row(id)
    person_dict = {
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'dob': str(person[3]),
        'location': person[4]
    }
    return jsonify(person_dict)

@app.route('/persons/<id>', methods=['GET'])
def persons_read_by_id(id):
    person = persons.search_row(id)
    if person is None:
        return jsonify({'message': 'Person not found'})
    person_dict = {
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'dob': str(person[3]),
        'location': person[4]
    }
    return jsonify(person_dict)

@app.route('/persons', methods=['GET'])
def persons_read_all():
    persons_list = persons.list_all_rows()
    persons_dict = []
    for person in persons_list:
        persons_dict.append({
            'id': person[0],
            'name': person[1],
            'gender': person[2],
            'dob': str(person[3]),
            'location': person[4]
        })
    return jsonify(persons_dict)

@app.route('/persons/<id>', methods=['PUT'])
def persons_update(id):
    body = request.get_json()
    old_person = persons.search_row(id)
    if old_person is None:
        return jsonify({'message': 'Person not found'})
    updated_person = (
        body['name'],
        body['gender'],
        body['dob'],       # FIXED: dob before location
        body['location'],
        id
    )
    persons.update_row(updated_person)
    person = persons.search_row(id)
    person_dict = {
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'dob': str(person[3]),
        'location': person[4]
    }
    return jsonify(person_dict)

@app.route('/persons/<id>', methods=['DELETE'])
def persons_delete(id):
    old_person = persons.search_row(id)
    if old_person is None:
        return jsonify({'message': 'Person not found', 'is_error': 1})
    persons.delete_row(id)
    return jsonify({'message': 'Person is deleted', 'is_error': 0})

if __name__ == '__main__':
    app.run(debug=True)
