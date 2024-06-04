from flask import Flask, request, jsonify
import webscrape
import asyncio

app = Flask("scrape")

@app.route('/scrape_data', methods=["GET", "POST"])
def scrape_and_return():
    try:
        data = webscrape.web_scrape()
        print("-----------------------------------------api:",data)
        response =  jsonify(data)
        response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5500'
        return response
    except Exception as e:
        return jsonify({'error' : str(e)}), 500
    
@app.route('/corse-preflight', methods=['OPTIONS'])
def cors_preflight():
    response = jsonify({})
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5500'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    
if __name__ == '__main__':
    app.run(debug=True)


