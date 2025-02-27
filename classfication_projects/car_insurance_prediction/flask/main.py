from flask import Flask,render_template,request,send_file,redirect,url_for,g,session,flash
import pandas as pd
import pickle
import os

UPLODER_FOLDER = 'uploads'

os.makedirs(UPLODER_FOLDER,exist_ok=True)


# init the flask app or creating instance for the class of Flask
app= Flask(__name__)#init
#app.config['UPLODER_FOLDER'] = UPLODER_FOLDER
with open('model.pk1','rb') as file:
    model = pickle.load(file)
feature_names = model.feature_names_in_

@app.route('/',methods=['GET','POST'])
def home():
    message=None
    message_type = None
    file_message=None
    file_message_type=None
    if request.method == 'POST':
        if request.files.get('file',''):
            file= request.files['file']
            if file:
                path = os.path.join(UPLODER_FOLDER,file.filename)
                file.save(path)
                df = pd.read_csv(path)
                #print(df.head())
                if  len(df.columns) == len(feature_names) and all(df.columns == feature_names):
                    result= model.predict(df.values.tolist())
                    path_save = os.path.join(UPLODER_FOLDER,'predicted_'+file.filename)
                    df['y_pred'] = result
                    df.to_csv(path_save,index=False)
                    file_message_type='success'
                    file_message = 'You can check the file in downloads folder'
                    return send_file(path_save,as_attachment=True)
                file_message,file_message_type=f"pls provide valid csv file that should cantian the {feature_names} ","error"
        try:
            predictors = [float(x) for x in request.form.values()]
            result = model.predict([predictors])[0]
            message = "high chance of insurance claim" if result else "less chance of insurance claim"
            message_type="success"
        except ValueError:
            message="pls provide valid numeric values"
            message_type="error"
            
    return render_template('home.html',feature_names=feature_names,message=message,message_type=message_type,file_message=file_message,file_message_type=file_message_type)
app.run(debug=True)