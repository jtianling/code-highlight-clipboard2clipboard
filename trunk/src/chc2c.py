from optparse import OptionParser
from distutils.file_util import *
import os
import tempfile

def main():
    
    usage = 'usage: %prog [options]'
    version = '''%prog 0.1 Created By JTianLing
Any Question could be sent to JTianLing{at}Gmail.com,
and any advice or any bug report is appreciated too.'''
    
    parser = OptionParser(usage, version = version)
    parser.add_option('-f', '--filename', metavar = 'FILE', dest = 'filename', 
                      help = 'Write output to FILE and save it.')
    parser.add_option('-t', '--syntax', action = 'store',
                      type = 'string', dest = 'syntax',
                      default = '',
                      help = 'Set the code syntax type')
    parser.add_option('-c', '--color', action = 'store',
                      type = 'string', dest = 'color',
                      default = 'default',
                      help = 'Set the code highlight color template')
    parser.add_option('-n', action= 'store_true', dest = 'isNumber',
                      default = False,
                      help = 'Is output with line number.')
    (options, args) = parser.parse_args()
    
    filename = tempfile.mktemp() + '.tmp'
        
    cboutStr = 'cbout > ' + filename
    os.system(cboutStr)
    
    syn = options.syntax
    color = options.color
    
    # ugly but useful vim's format code
    vimCmd = 'gvim -c ":syntax on|:color ' + color + '|:set syn=' + syn\
     + '|:set nu' + ('' if options.isNumber else '!') + '|TOhtml" -c ":w|:qa" ' + filename
    os.system(vimCmd) 
    #print(vimCmd)
    
    newFilename = filename + '.html'
    cbinStr = 'more ' + newFilename + ' | cbin'
    os.system(cbinStr)           

    # Del the temp file when that's needed
    if options.filename:
        move_file(newFilename, './' + options.filename)
    else:
        os.remove(newFilename)
        
    os.remove(filename)
    
if __name__ == '__main__':
    main()