from matchers import *

class QueryBuilder:
    def __init__(self, build = All()):
        self.builder = build
    
    def playsIn(self, team):
        return QueryBuilder(And(self.builder, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.builder, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.builder, HasFewerThan(value, attr)))

    def build(self):
        return self.builder