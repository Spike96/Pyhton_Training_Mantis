
class Project:

    def __init__(self, name=None, description=None, id=None):
        self.name = name
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.description)

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name) \
               or (self.description is None or other.description is None or self.description == other.description)

    def key(self):
        return self.name
