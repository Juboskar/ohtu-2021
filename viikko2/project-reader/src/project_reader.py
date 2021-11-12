from urllib import request
from project import Project
from toml import loads

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # toml kirjastolla dictionary
        content_dict = loads(content, _dict=dict)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        name = content_dict['tool']['poetry']['name']
        description = content_dict['tool']['poetry']['description']
        dependencies = list(content_dict['tool']['poetry']['dependencies'].keys())
        dev_dependencies = list(content_dict['tool']['poetry']['dev-dependencies'].keys())

        return Project(name, description, dependencies, dev_dependencies)
