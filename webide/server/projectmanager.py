import pathlib
import time
import shutil
import platform
import re
import os


class ProjectManager:

    def __init__(self, root=pathlib.Path.home() / 'tscode'):

        # root folder in which all projects are stored
        self.__root = pathlib.Path(root)

        # make the root folder if it does not exist
        self.__root.mkdir(exist_ok=True)

        # dict with:
        #   key: name (string) of a function
        #   value: function
        # e.g. {'create': <bound method ProjectManager.create ... >, ...}
        # for use in `parse_request`
        fs = [f for f in dir(self) if f[0] != '_' and f != 'parse_response']
        self.__actions = {name: getattr(self, name) for name in fs}

        # creating a regex object to determine if a name contains an invalid character
        # for use in `__valid_name`
        invalid_chars = '/'
        if platform.system() == 'Windows':
            invalid_chars += '<>:"\\|?*'
        self.__invalid_chars_regex = re.compile(f'[{invalid_chars}]')
    def __valid_name(self, name):
        """
        Checks whether the name of the project is valid, i.e. not a subdirectory
        and doesn't contain invalid characters for the server's OS
        """
        return not self.__invalid_chars_regex.search(name)
    def __project_exists(self, name):
        """
        Checks whether the project, i.e. its corresponding directory, exists
        """
        return (self.__root / name).is_dir()
    def __response(self, status = 'success', data = None):
        return {
            'status': status,
            'data': data
        }
    def create(self, name: str, lang: str='python'):
        """
        Create a new project by creating its corresponding directory
        """
        if not self.__valid_name(name):
            return self.__response('invalid_name')
        if self.__project_exists(name):
            return self.__response('exists')
        (self.__root / name).mkdir()
        with open(self.__root / name / '.proj', 'w', encoding='utf8') as f:
            f.write(str(int(time.time())) + '\n')
            if lang == 'python':
                m = open(self.__root / name / 'main.py','w')
                f.write('python')
                os.system(f'conda create -n "{name}" --clone base')
            elif lang == 'java':
                m = open(self.__root / name / 'main.java','w')
                f.write('java')
            elif lang == 'matlab':
                m = open(self.__root / name / 'main.m','w')
                f.write('matlab')
            else :
                f.write('others')


        return self.__response()
    def upload(self, folder):
        """
        Upload a new project from the client to server
        """

        # TODO: accept upload

        return self.__response(data=None)
    def download(self, name: str):
        """
        Download the project as a zip from server to client
        """
        if not self.__project_exists(name):
            return 'does_not_exist'
        # TODO: zip and send project

        shutil.make_archive(name, 'zip', self.__root / name)
        return self.__response()
    def delete(self, name: str):
        """
        Delete a project by deleting its corresponding directory
        """
        if not self.__project_exists(name):
            return self.__response('does_not_exist')
        with open(self.__root / name / '.proj', encoding='utf8') as f:
            lang = f.readlines()[1].strip()
            if lang == 'python':
                os.system(f'conda env remove --name "{name}" -y')
        shutil.rmtree(self.__root / name)
        return self.__response()
    def rename(self, old: str, new: str):
        """
        Rename a project by renaming its corresponding directory
        """
        if not self.__project_exists(old):
            return self.__response('does_not_exist')
        if not self.__valid_name(new):
            return self.__response('invalid_name')
        (self.__root / old).rename(self.__root / new)
        (pathlib.Path.home() / 'anaconda3' / 'envs' / old).rename(pathlib.Path.home() / 'anaconda3' / 'envs' / new)
        return self.__response()
    def info(self, name: str):
        """
        Return the info of the project named `name`
        """
        project = self.__root / name
        if not project.is_dir() or not (project / '.proj').is_file():
            return self.__response('does_not_exist')
            

        files = 0
        folders = 0

        stat = project.stat()
        # add the size of the project's root dir
        size = stat.st_size
        for inode in project.rglob('*'):
            files += inode.is_file()
            folders += inode.is_dir()
            size += inode.stat().st_size

        with open(project / '.proj') as f:
            info = {
                'files': files,
                'folders': folders,
                'size': size,
                'modified': int(stat.st_mtime),
                'accessed': int(stat.st_atime),
                'created': int(f.readlines()[0])
            }
        return self.__response(data=info)
    def getall(self):
        """
        Get the info of all the projects under the root dir
        """
        projects = {}
        # iterate over direct contents of root dir
        for project in self.__root.iterdir():
            info = self.info(project.name)
            if info['status'] == 'does_not_exist':
                continue
            projects[project.name] = info['data']
        return self.__response(data=projects)
    def parse_request(self, request):
        if ('action' not in request or request['action'] not in self.__actions):
            return self.__response('bad_action')

        action = request.pop('action')

        try:
            # throws TypeError if the args don't match
            return self.__actions[action](**request)
        except TypeError:
            return self.__response('bad_args')
