from flask import Flask, request, redirect
from projectmanager import ProjectManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)
mgr = ProjectManager()

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'POST':
        return mgr.parse_request(request.get_json())
    else:
        # TODO: serves the projects main page
        return redirect('http://webide.georgetian.com:18082')



if __name__ == '__main__':
    app.run('0.0.0.0', '18081')
