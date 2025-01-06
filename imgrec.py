from clarifai.rest import ClarifaiApp
from flask import Flask, jsonify, request, render_template, redirect , url_for
import random
import requests,json
import webbrowser
app = Flask(  
    __name__,
    template_folder='templates',  
    static_folder='static'  
)

headers = {'Authorization': 'Key 60a5431c7d054eec8ba38fd33f83381f'}
api_url = "https://api.clarifai.com/v2/models/e0be3b9d6a454f0493ac3a30784001ff/outputs"

@app.route('/', methods=['GET', 'POST'])  
def img_link():
    if request.method == 'POST':
        if request.url:
            py_link = request.form['link']
            data ={"inputs": [
            {
            "data": {
            "image": {
            "url": py_link
            }
            }
            }
            ]}

                
            response = requests.post(api_url, headers=headers, data=json.dumps(data))
            response_dict=json.loads(response.content)
            test2=response_dict["outputs"][0]["data"]["concepts"][0]['name']
            webbrowser.get('firefox').open('amazon.com/s?k='+test2)
            return render_template('temp.html')
            
    else:
        return render_template("temp.html")



if __name__ == "__main__":  
    app.run( 
        host='0.0.0.0',  
        port=random.randint(2000, 9000),  
    debug=True
    )






'''
app = ClarifaiApp(api_key='60a5431c7d054eec8ba38fd33f83381f')

model = app.models.get(model_id="e0be3b9d6a454f0493ac3a30784001ff")

response=model.predict_by_url(url='https://cdn.webshopapp.com/shops/178199/files/168782699/1000x1300x2/giaro-black-giaro-ultra-fetish-platform-pumps-with.jpg',max_concepts=3)
test2=response["outputs"][0]["data"]["concepts"]
print(test2)


#model = app.models.get('Apparel_Detection')

#print(model.predict_by_url(url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shoebidooshoes.com%2Fen%2Fblack-giaro-gold-heel-fetish-platform-pumps.html&psig=AOvVaw3wHqYN0E8EJWfRPriNaAbX&ust=1604250668710000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPC63s6p3-wCFQAAAAAdAAAAABAJ', max_concepts=1))
#test=model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg', max_concepts=1)

#test2=test["outputs"][0]["data"]["concepts"]
#print(test2)



#from __future__ import unicode_literals
import ast
import requests, json
# you can use the headers to pass in hidden info, here we are sending a secret Key (think of it as a password)
headers = {'Authorization': 'Key 2ebb08a507be48d99185a2b0905a0ef0'}

# this is the url of where your request will go
api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"

# this is content of the message(data) you are sending to clarifai
data ={"inputs": [
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      }
    ]}

# putting everything together; sending the request!
response = requests.post(api_url, headers=headers, data=json.dumps(data))
response_dict = json.loads(response.content)
print(str(ast.literal_eval(response_dict["outputs"][0]["data"]["concepts"])))
print(response.status_code)
'''






