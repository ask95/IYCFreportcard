from flask import Flask, request, redirect, url_for, make_response, render_template, send_from_directory
import csv
import io, os
from werkzeug.utils import secure_filename 
app = Flask(__name__ , static_url_path='/static')
'''
    , static_url_path = os.getcwd() + '/../images/', 
    static_folder = os.getcwd() + '/images/')
'''
ALLOWED_EXTENSIONS = set(['csv', 'pdf'])
UPLOAD_FOLDER = '/upload_csv/'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_file():
    return render_template('form_input.html')


@app.route('/transform', methods=["POST"])
def transform_view():
    print type(request)
    f = request.files['data_file']
    surv_id = str(request.form['survey_id'])

    image_path = os.getcwd() + '/images/'

    target = os.path.join(APP_ROOT, 'images')

    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream, delimiter=',', quotechar='|')
    #print("file contents: ", file_contents)
    #print(type(file_contents))
    print(csv_input)
    image = ''
    for row in csv_input:
        if len(row) > 0:
            print "ROW ----------->", row
            if int(row[0]) < 1:
                imagename = 'red.png'
            else:
                imagename = 'green.png'

            if int(row[1]) < 10:
                image2name = 'red.png'
            else:
                image2name = 'green.png'
            if int(row[2]) < 1:
                image3name = 'red.png'
            else:
                image3name = 'green.png'


    destination = "/".join([target, imagename])
    return render_template("report.html", image_name=imagename, image2_name=image2name, 
        image3_name=image3name)

@app.route('/transform/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

    

        

    #stream.seek(0)
    #result = transform(stream.read())
    #result = stream.read()
    #response = make_response(result)
    #response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    #return html_report
