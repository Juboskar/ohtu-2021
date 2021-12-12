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

    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))

    def build(self):
        return self.builder