from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

class Athlete():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.birthday = data['birthday']
        self.nationality = data['nationality']
        self.home_state = data['home_state']
        self.weight = data['weight']
        self.sex = data['sex']
        self.user_id = session['user_id']
        # self.user = None
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_athlete(cls, data):

        query = 'INSERT INTO athletes (first_name, last_name, birthday, nationality, home_state, weight, sex, user_id) VALUES (%(first_name)s, %(last_name)s, %(birthday)s, %(nationality)s, %(home_state)s, %(weight)s, %(sex)s, %(user_id)s);'

        result = connectToMySQL('goats_schema').query_db(query, data)

        return result

    @staticmethod
    def validate_athlete(data):

        is_valid = True

        if len(data['first_name']) < 1:
            flash("Athlete should have a first name.")
            is_valid = False

        if len(data['last_name']) < 1:
            flash("Athlete should have a last name.")
            is_valid = False

        return is_valid