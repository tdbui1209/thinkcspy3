import sys

def test(did_pass):
    '''Print the result of a test.'''
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} OK.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED.'.format(linenum)
    print(msg)
