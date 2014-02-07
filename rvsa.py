import kvdt_reader

__author__ = 'Martin'
RVSA = 'rvsa'

def prozess(reader):
    res = []
    t = reader.current_tuple()
    t = reader.advance()
    while t[0] == '0201':
        bsnr = [t[1]]



