from flask import Flask, request, jsonify, abort
from models import setup_db, Actor, Movie, setup_migrations
from flask_cors import CORS
from auth import requires_auth, AuthError


def create_app():
    app = Flask(__name__)
    # connect flask application with sqlalchemy db (postgres)
    setup_db(app)
    setup_migrations(app)

    # Index/base route
    @app.route('/')
    def health_check():
        return jsonify({"success": True, "message": "Healthy"})

    # Actor routes

    # Route : Get all actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_all_actors():
        try:
            actors = Actor.query.all()
            f_actors = [a.serialized_actor() for a in actors]
        except Exception as e:
            print(e)
        if len(f_actors) == 0:
            abort(404)
        return jsonify({"success": True, "actors": f_actors})

    # Route : Add a new actor
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_new_actor():
        req_body = request.get_json()
        name = req_body.get("name", None)
        age = req_body.get("age", None)
        gender = req_body.get("gender", None)
        if name is None or age is None or gender is None:
            abort(400)
        else:
            try:
                actor = Actor(
                    name=name, age=age, gender=gender)
                actor.insert()
            except Exception as e:
                print(e)
                abort(422)
        return jsonify(
            {
                "success": True, "actors": actor.serialized_actor()
            }
        )

    # Route : Delete an actor
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(id):
        del_actor = Actor.query.get(id)
        if del_actor is None:
            abort(404)
        try:
            del_actor.delete()
        except Exception as e:
            print(e)
            abort(422)
        return jsonify({"success": True, "id": id})

    # Route : Update an actor
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(id):
        upd_actor = Actor.query.get(id)
        if upd_actor is None:
            abort(404)
        try:
            req_body = request.get_json()
            name = req_body.get("name", None)
            age = req_body.get("age", None)
            gender = req_body.get("gender", None)
            if name is not None:
                upd_actor.name = name
            if age is not None:
                upd_actor.age = age
            if gender is not None:
                upd_actor.gender = gender
            upd_actor.update()
        except Exception as e:
            print(e)
            abort(422)
        return jsonify({"success": True, "actor": upd_actor.serialized_actor()})

    # Movie routes
    # Route : Get all movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_all_movies():
        try:
            movies = Movie.query.all()
            f_movies = [m.serialized_movie() for m in movies]
        except Exception as e:
            print(e)
        if len(f_movies) == 0:
            abort(404)
        return jsonify({"success": True, "movies": f_movies})

    # Route : Add a new movie
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_new_movie():
        req_body = request.get_json()
        title = req_body.get("title", None)
        release_date = req_body.get("release_date", None)
        if release_date is None or title is None:
            abort(400)
        else:
            try:
                f_movie = Movie(
                    #title=title, release_date=date.fromisoformat(release_date))
                    title=title, release_date=release_date)
                f_movie.insert()
            except Exception as e:
                print(e)
                abort(422)
        return jsonify(
            {
                "success": True, "movies": f_movie.serialized_movie()
            }
        )

    # Route : Delete a movie
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(id):
        del_movie = Movie.query.get(id)
        if del_movie is None:
            abort(404)
        try:
            del_movie.delete()
        except Exception as e:
            print(e)
            abort(422)
        return jsonify({"success": True, "id": id})

    # Route : Update a movie
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(id):
        upd_movie = Movie.query.get(id)
        if upd_movie is None:
            abort(404)
        try:
            req_body = request.get_json()
            title = req_body.get("title", None)
            release_date = req_body.get("release_date", None)
            if title is not None:
                upd_movie.title = title
            if release_date is not None:
                upd_movie.release_date = release_date
            upd_movie.update()
        except Exception as e:
            print(e)
            abort(422)
        return jsonify({"success": True, "movie": upd_movie.serialized_movie()})

    # Error Handlers

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False,
                        "error": 404,
                        "message": "Resource Not Found"
                        })

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(401)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Not Authorized"
        }), 401


    @app.errorhandler(404)
    def error_resource_not_found(error):
        return jsonify({
            "success": False,
            "message": "Resource not found",
            "error": 404
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "message": "Internal server error",
            "error": 500
        }), 500

    @app.errorhandler(422)
    def not_processable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Request cannot be processed"
        }), 422

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @app.errorhandler(403)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden"
        }), 403
    
    @app.errorhandler(AuthError)
    def auth_error(error):
        print(error)
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
