__author__ = 'Martin'

class KVDT_Reader:
    """
    Liest den Inhalt einer KVDT-Datei und erzeugt daraus eine Liste
    von Wertenpaaren <Feldkennung, Feldwert>
    """

    def __init__(self, file_name):
        self.file_name_ = file_name
        self.tuples_ = []
        self.pos_ = 0
        f = open(file_name, "r")
        for line in f.readlines():
            self.tuples_.append([line[3:7], line[7:len(line)-1]])
        f.close()

    def tuples(self):
        return self.tuples_

    def advance(self):
        if self.pos_ < len(self.tuples_):
            self.pos_ += 1
        return self.current_tuple()

    def current_tuple(self):
        return self.tuples_[self.pos_] if self.pos_ < len(self.tuples_) else None




