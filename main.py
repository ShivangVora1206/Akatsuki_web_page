from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
# import os
app = Flask(__name__)

@app.route('/')
def alpha():
    print('-------------------------')
    return render_template('index.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

# -----------UPLOADER_SETUP-----------------------
# @app.route("/upload")
# def upload_file():
#     return render_template("upload.html")
# @app.route('/uploader', methods = ['GET', 'POST'])
# def _upload_file():
#     if request.method == 'POST':
#         global f
#         f = request.files['file']
#         os.chdir(r"C:\Users\Asus\Desktop\python\AKATSUKI\Uploads")
#         f.save(secure_filename(f.filename))
#         page='done'
#         return render_template('home.html', page=page)
