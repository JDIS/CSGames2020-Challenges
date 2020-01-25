from app import app
from app.helpers import compare_query_output, execute_query
from app.flags import level_1_data, level_2_data, level_3_data
from flask import jsonify, render_template, request
from sqlite3 import Error as sqlite_Error


import json


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/schema', methods=['GET'])
def schema():
    return render_template('/static')


@app.route('/level_1', methods=['GET'])
def level_1():
    description = "On cherche à obtenir les produits d'une certaine catégorie."
    return render_template('level.html', title="Niveau 1", description=description, data=level_1_data)


@app.route('/level_2', methods=['GET'])
def level_2():
    description = "On cherche à savoir les produits vendus par un employé précis. De plus, nous voulons savoir combien de fois est-ce qu'il a vendu chacun d'eux."
    return render_template('level.html', title="Niveau 2", description=description, data=level_2_data)


@app.route('/level_3', methods=['GET'])
def level_3():
    description = "On cherche à savoir le montant dépensé par compagnies envers chaques fournisseurs, arrondi vers le bas."
    return render_template('level.html', title="Niveau 3", description=description, data=level_3_data)


@app.route('/query', methods=['POST'])
def data():
    query = request.values.get('q')
    level = request.values.get('level')

    try:
        if not query:
            return jsonify({"error": f"Missing query parameter."})

        output = execute_query(query)
        
        if level == "Niveau 1" and compare_query_output(level_1_data, output):
            output["flag"] = "FLAG{DamnTheseCondimentsAreGettingExpensive}"
        if level == "Niveau 2" and compare_query_output(level_2_data, output): 
            output["flag"] = "FLAG{ThatSQLThingIsMuchEasierThanExpected}"
        if level == "Niveau 3" and compare_query_output(level_3_data, output):
            output["flag"] = "FLAG{SQLIsTheNewMatlab}"

        return jsonify(output)
    except sqlite_Error as e:
        return jsonify({"error": f"{e}"})
