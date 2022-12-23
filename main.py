from flask import Flask , render_template ,request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'white_kia_seltos'
    return app


app = create_app()


@app.route("/",methods = ["GET","POST"])
def home():
    return render_template("home.html")
    
@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/ans",methods = ["POST","GET"])
def ans():
    content_choice = request.form.get("content_choice")
    content_file = ''
    main_file = ''
    if content_choice == 'txt':
        from reading_txt import read_txt
        txt_text = read_txt(request.form.get("content_file_name"))
        content_file = txt_text
    
    if content_choice == 'docx':
        from reading_doc import doc_to_text
        doc_text = doc_to_text(request.form.get("content_file_name"))
        content_file = doc_text
    
    
    elif content_choice == 'Text':
        Text_text = request.form.get("text_rn")
        Text_text = Text_text.lower()

        file_list = Text_text.split()
        conjunctions = ['after','although','as','because', 'before', 
        "for","if","since","unless",
        "until","when","whenever","where","wherever",'while','is',
        'a','the','an','of','to','that','on','are','but','and','from','also','the','so']
        
        try:
            for a in (file_list):
                for b in conjunctions:
                    if(a==b):
                        file_list.remove(a)
        except Exception:
            pass
        file_string_new = ""
        for c in file_list:
            file_string_new = file_string_new + c + " " 
        
        content_file = file_string_new
    

    main_choice = request.form.get("main_choice")
    if main_choice == 'TXT':
        from reading_txt import read_txt
        TXT_text = read_txt(request.form.get("main_file"))
        main_file = TXT_text
        from compare_str import compare
        percentage = compare(content_file,main_file)
        return render_template("ans.html",answer = percentage)

    if main_choice == "TEXT":
        Text_text = request.form.get("main_text")
        Text_text = Text_text.lower()

        file_list = Text_text.split()
        conjunctions = ['after','although','as','because', 'before', 
        "for","if","since","unless",
        "until","when","whenever","where","wherever",'while','is',
        'a','the','an','of','to','that','on','are','but','and','from','also','the','so']
        try:
            for i in (file_list):
                for m in conjunctions:
                    if(m==i):
                        file_list.remove(i)
        except Exception:
            pass
        file_string_new = ""
        for j in file_list:
            file_string_new = file_string_new + j + " " 
        
        main_file = file_string_new
        from compare_str import compare
        percentage = compare(content_file,main_file)
        return render_template("ans.html",answer = percentage)

    
    if main_choice == 'DOCX':
        from reading_doc import doc_to_text
        DOC_text = doc_to_text(request.form.get("main_file"))
        main_file = DOC_text
        from compare_str import compare
        percentage = compare(content_file,main_file)
        return render_template("ans.html",answer = percentage)
    
    if main_choice == 'URL':
        from getting_url import read_url
        url_text = read_url(request.form.get("main_url"))
        main_file = url_text
        from compare_str import compare
        percentage = compare(content_file,main_file)
        return render_template("ans.html",answer = percentage)
    

    

if __name__ == '__main__':
    app.run(debug=True)