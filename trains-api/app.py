from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# "Databáze" vlaků v paměti
trains = [
  {"type": "RB", "number": 2000, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2001, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2002, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2003, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2004, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2005, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2006, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2007, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2008, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2009, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2010, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2011, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2012, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2013, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2014, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2015, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2016, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2017, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2018, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2019, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2020, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2021, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2022, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2023, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2024, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2025, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2026, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2027, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2028, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2029, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2030, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2031, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2032, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2033, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2034, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2035, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2036, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2037, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2038, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2039, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2040, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2041, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2042, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2043, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2044, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2045, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2046, "line": "RB 1", "from": "Nether Central", "to": "Netherium"},
  {"type": "RB", "number": 2047, "line": "RB 1", "from": "Netherium", "to": "Nether Central"},
  {"type": "RB", "number": 2048, "line": "RB 1", "from": "Nether Central", "to": "Netherium"}
]


@app.get("/gettrain/<int:trainnr>")
def get_train(trainnr):
    for train in trains:
        if train["number"] == trainnr:
            return jsonify(train)
    return jsonify({"error": "Vlak nenalezen"}), 404

@app.get("/gettrains")
def get_trains():
    return jsonify(trains)


CORS(app)
app.run(port=3000)