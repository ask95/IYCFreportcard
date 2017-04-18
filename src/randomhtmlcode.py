html_report = '''
    <html>
    <body>

    <h2>Milk Content</h2>
    '''
    #resp = "<img src=" + image_path + ">"
    #resp = '''<img src="{{ url_for('static', filename = ''' + str("'")+ image_path + str("'") + ''') }}" > '''
    #style='width:304px;height:228px;    width="200" height="85"'
    print url_for('static', filename = image)
    resp = "<img src=" + '"' + url_for('static', filename = image) + '"' + ">"
    print resp

    end = '''
    </body>
    </html>
    '''

    html_report = html_report + resp + end
    