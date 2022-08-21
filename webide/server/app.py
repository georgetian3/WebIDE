from flask import Flask, request, render_template
from projectmanager import ProjectManager


app = Flask(__name__)
mgr = ProjectManager()


@app.route('/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'POST':
        return mgr.parse_request(request.get_json())
    else:
        # TODO: serves the projects main page
        return render_template('index.html')

@app.route('/<path:u_path>')
def catch_all(u_path):
    print('catch all ' + u_path)
    # TODO: route to code-server
    return 'catch all ' + u_path

if __name__ == '__main__':
    app.run()
