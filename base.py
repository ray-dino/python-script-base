from __future__ import print_function
import sys, getopt


def start(script_name, argv):
    '''
    Usage: python script.py -e 'Example String'
    '''
    try:
        opts, args = getopt.getopt(
            argv,
            'he:',
            [
                'help',
                'example='
            ])
    except getopt.GetoptError:
        usage(script_name)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage(script_name)
            sys.exit()
        elif opt in ('-e', '--example'):
            example(arg)
                

def example(arg):
    print('Example {}'.format(arg))

def usage(script_name):
    print('Usage: python {}'.format(script_name))

if __name__=='__main__':
    start(sys.argv[0], sys.argv[1:])
