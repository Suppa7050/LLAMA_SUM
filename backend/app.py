from flask import Flask, render_template, request
# import kaggle
import subprocess
import PyPDF2
import json
from flask_cors import CORS, cross_origin
import asyncio
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId
import nbformat
load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
    </html>
    """
    return html_content

@app.route('/summary', methods=['GET', 'POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        flag=request.form.get("flag")
        print(flag)
        connection_string=os.getenv("DB_URL")
        client = MongoClient(connection_string)
        db = client.Llama2
        collection = db.summary
        if(flag=="true"):
            try:
                os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
                os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")
                inp=request.files
                print(inp)
                documents=[]
                pdf_text=""
                for i in inp.getlist("file"):
                    doctext=read_pdf(i)
                    pdf_text = pdf_text+doctext+"\n"
                    documents.append(doctext)
                # Create a TF-IDF vectorizer
                vectorizer = TfidfVectorizer()
                # Fit and transform the documents
                tfidf_matrix = vectorizer.fit_transform(documents)
                # Calculate cosine similarity
                cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
                error={
                    "headers":{
                        "Access-Control-Allow-Origin": "*"
                    },
                    "mongoid":"SimErr"
                }
                for i in range(len(documents)):
                    for j in range(len(documents)):
                        print(cosine_similarities[i][j])
                        if cosine_similarities[i][j]<0.65:
                            return json.dumps(error)
                with open("notebook/kaggleint3cpy.ipynb","r") as file:
                    notebook=nbformat.read(file, as_version=4)
                target_cell_index = 10
                insert_result = collection.insert_one({"summary":""})
                client.close()
                id=str(insert_result.inserted_id)
                # x=x.replace('id=\\n',f'id=\\"{id}\\"',1)
                # x=x.replace('data=',f'data=\\"\\"\\"{pdf_text}\\"\\"\\"',1)
                code_cell = notebook.cells[target_cell_index]
                code_cell['source'] += f'id = "{id}"\ntext = """{pdf_text}"""'
                with open("notebook/kaggleint3.ipynb","w",errors='ignore') as file:
                    nbformat.write(notebook, file)
                result=subprocess.run(["kaggle", "kernels", "push", "-p", "notebook"])
                print(result)
                d={
                    "headers":{
                        "Access-Control-Allow-Origin": "*"
                    },
                    "mongoid":id
                }
                return json.dumps(d)
            except Exception as e:
                err={
                    "headers":{
                        "Access-Control-Allow-Origin": "*"
                    },
                    "mongoid":"Error",
                    "message":f"Something went wrong ({e})"
                }
                return json.dumps(err)
        else:
            ntbk_ref=f'{os.getenv("KAGGLE_USERNAME")}/kaggleiniti2'
            response = subprocess.run(["kaggle", "kernels", "status", ntbk_ref], capture_output=True)
            resp_text = response.stdout.decode("utf-8")
            if resp_text.startswith("403 - Forbidden"):
                print("Notebook", ntbk_ref, " probably does not exists. Response of Kaggle API CLI:", resp_text)
            print(resp_text)
            new_status = resp_text.split('"')[1]  # status test is between ""
            fg=False
            if new_status=="running":
                print(datetime.now(), resp_text)
                fg=True
            id=request.form.get("mongoid")
            # print(id)
            print(new_status)
            print(fg)
            summary=collection.find_one({"_id": ObjectId(id)})["summary"]
            if not fg:
                collection.delete_one({"_id": ObjectId(id)})
            client.close()
            d={
                "headers":{
                    "Access-Control-Allow-Origin": "*"
                },
                "summary":summary,
                "status":fg
            }
            return json.dumps(d)
        # await wait_for_ntbk_completion(f'{os.getenv("USER")}/kaggleiniti2')
        # asyncio.run(wait_for_ntbk_completion(f'{os.getenv("USER")}/kaggleiniti2'))
        # subprocess.run(["kaggle", "kernels", "output", f'{os.getenv("USER")}/kaggleiniti2', "-p", "./"])
        # with open('result.json', 'r') as file:
        #     data = json.load(file)
        # print(data)
        # data=data["summary"]
        # data="rohith is a good boy"
        

    return json.dumps("Post request is not called")


def read_pdf(file):
    # with open(file, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

# async def wait_for_ntbk_completion(ntbk_ref: str) -> None:
#     # until status of notebook is "complete" stay in while loop
#     # if status is not changed, wait for DELAY seconds
#     DELAY = 60  # seconds
#     status = ""
#     while status != "complete":
#         response = subprocess.run(["kaggle", "kernels", "status", ntbk_ref], capture_output=True)
#         resp_text = response.stdout.decode("utf-8")
#         if resp_text.startswith("403 - Forbidden"):
#             print("Notebook", ntbk_ref, " probably does not exists. Response of Kaggle API CLI:", resp_text)
#             return
#         new_status = resp_text.split('"')[1]  # status test is between ""
#         if status != new_status:
#             print(datetime.now(), resp_text)
#             status = new_status
#         else:
#             await asyncio.sleep(DELAY)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)



# if 'file' not in request.files:
#             return json.dumps('No file part')

#         file = request.files['file']

#         if file.filename == '':
#             return json.dumps('No selected file')

#         if not file.filename.endswith('.pdf'):
#             return json.dumps('Please upload a PDF file')