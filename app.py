from flask import Flask, render_template, request
from rdflib import Graph

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        results = execute_sparql_query(query)
        return render_template('index.html', results=results)
    return render_template('index.html')

def execute_sparql_query(query):
    # Load the OWL file
    g = Graph()
    g.parse('LibrarySystemProject.owl', format='xml')
    
    # Execute the SPARQL query
    results = g.query(query)
    print(results)
    # Convert the results to a list of dictionaries
    bindings = results.bindings
    rows = []
    for binding in bindings:
        row = {}
        for var in results.vars:
            row[var] = binding[var].toPython()
        rows.append(row)

    return rows


if __name__ == '__main__':
    app.run()
