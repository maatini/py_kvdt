
#
#	Minimal token class.
#

class Token:
    def __init__(self, type, attr=None):
        self.type = type
        self.attr = attr

    #
    #  Not all these may be needed:
    #
    #  __cmp__	required for GenericParser, required for
    #			GenericASTMatcher only if your ASTs are
    #			heterogeneous (i.e., AST nodes and tokens)
    #  __repr__	recommended for nice error messages in GenericParser
    #  __getitem__	only if you have heterogeneous ASTs
    #
    def __cmp__(self, o):
        return cmp(self.type, o)
    def __repr__(self):
        return self.attr or self.type
    #def __getitem__(self, i):
    #	raise IndexError

    def match(self, type, attr=None):
        return self.type == type and (attr is None or self.attr == attr)
