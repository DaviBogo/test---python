from flask import Flask, request
import zipfile, time
app = Flask('application')


@app.route('/zipar', methods=['POST'])
def hello_world():
    number = int(request.form["numero"])

    start = time.time()
    with zipfile.ZipFile('C:\\Users\\Davi\\Downloads\\arq.zip', 'w', zipfile.ZIP_DEFLATED) as zip :
        for i in range(1, number + 1) :
            zip.write('43KB' + str(i) + '.pdf')
        zip.close()
    end = time.time()
    return str((end - start) * 1000) + ' milisegundos'