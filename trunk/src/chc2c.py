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
    
    syn = options.syntax
    color = options.color
    
    # ugly but useful vim's format code
    setCBLinkToSystem = '-c "set clipboard+=unnamed"'
    pasteFromCB = ' -c ":norm p" '
    setSyntax = ' -c ":syntax on|:set syn=' + syn + '"'
    setColor = ' -c ":color ' + color + '"'
    setLineNumber = ' -c ":set nu' + ('"' if options.isNumber else '!"')
    toHtml =  ' -c ":TOhtml" '
    copyToCB = '-c ":norm ggVGy" '
    saveToFile =  (' -c ":w ' + options.filename + '"') if (options.filename != "") else ''
    quit = ' -c ":qa!"'
    vimCmd = 'gvim ' +  setCBLinkToSystem + pasteFromCB +  setSyntax + setColor\
    		+ setLineNumber + toHtml + copyToCB + saveToFile + quit
    os.system(vimCmd)
    print(vimCmd)
    
if __name__ == '__main__':
    main()
