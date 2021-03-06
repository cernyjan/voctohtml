# -*- coding: utf-8 -*-
# čžřě+áýčíáý+í
"""
name: voctohtml -- vocabulary HTML generator in Python 
autor: Černý Jan
email: cerny.jan@hotmail.com
version: 0.2
"""
#import - own packages
#import - system packages
import platform
import ctypes
from time import sleep
from sys import argv
from sys import exit
#import - others packages
import codecs


def main():
    """
    Main process of the voctohtml
    """
    global FILE_NAME
    global COUNTER
    def_counter = COUNTER
    print "\r"
    print "*********************************************"
    print unicode("voctohtml v0.2 \t autor: Černý Jan \t 2015", 'utf-8')
    print "*********************************************"
    print "\r"
    #check the parameters
    if len(argv) < 2:
        print "application have to run with some parameters !!"
        print "for help put -help parameter"
        print "\n"
        exit()

    #help
    if argv[1] == "-help":
        print "HELP"
        print "===="
        print "example of use: python main.py example_db.txt 7"
        print "example_db.txt >> file with vocabularies"
        print "7 >> quantity of vocabularies per table (optional parameter)"
        print "\n"
        exit()

    #location
    try:
        file_of_vocabularies = codecs.open(argv[1], "r", "utf-8")
        line = file_of_vocabularies.readline().strip()
        line = line.encode('utf-8')
        line = line.decode("utf-8")
        if line[(len(line)-2):] == "##":
            FILE_NAME = line[:-2]
    except IOError:
        print "wrong input file"
        print "\n"
        exit()
    
    doc = r"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>"""

    doc = doc.decode("utf-8");
    handler_to_file = codecs.open(FILE_NAME + ".html", "w", "utf-8")
    handler_to_file.write(doc + FILE_NAME)
    
    doc = r"""</title>
    <style type="text/css">
    body {
        margin: 0px 0px; padding: 0px;
        text-align: center;
        }
        
    .Content {
        width: 700px;
        margin: 0px auto;
        text-align: left;
        padding: 10px;
        border: 1px dashed #333;
        background-color: #eee;
        }

    table {
        width: 100%;
        border: 0px;
        font-size: 1.4em;;
    }
    
    td {
        padding: 10px;
        width: 45%;
    }
    
    .center {
        text-align: center;
        width: 10%;
    }
    
    .header {
        font-weight: bold;
        text-align: center;
    }
    </style>
    </head>
    <body>

    <div class="Content">
    <table border="1">
    <tr><td colspan="3"><i>"""

    doc = doc.decode("utf-8");
    handler_to_file.write(doc)

    #set user counter
    if len(argv) == 3:
        if argv[2].isdigit():
            def_counter = int(argv[2])
            COUNTER = def_counter

        
    try:
        file_of_vocabularies = codecs.open(argv[1], "r", "utf-8")
        gap = "&nbsp; – &nbsp;"
        gap = gap.decode("utf-8")
        doc_end = r"""</table>
        <br />
        <br />
        <br />
        <br />
        <br />
        </div>
        <div class="Content">
        <table border="1">
    
        <tr class="header">
        <td>original</td>
        <td class="center">&nbsp;</td>
        <td>translated</td>
        </tr>
        """
        
        while 1:
            line = file_of_vocabularies.readline().strip()
            line = line.encode('utf-8')
            line = line.decode("utf-8")
            if not line:
                break
            #name of the set of vocabularies
            if line[(len(line)-2):] == "##":
                doc = r"""</i></td></tr>
                <tr class="header">
                    <td>original</td>
                    <td class="center">&nbsp;</td>
                    <td>translated</td>
                </tr>"""
                doc = doc.decode("utf-8");
                handler_to_file.write(line[:-2] + doc + "\n")
                continue    
            line = line.split("#")
            if COUNTER > 0:
                handler_to_file.write("<tr><td>" + line[0] + "</td><td class='center'>" + gap + "</td><td>" + line[1] + "</td></tr>" + "\n")
                COUNTER -= 1
            else:
                handler_to_file.write(doc_end+"\n")
                handler_to_file.write("<tr><td>" + line[0] + "</td><td class='center'>" + gap + "</td><td>" + line[1] + "</td></tr>" + "\n")
                COUNTER = (def_counter - 1)
        file_of_vocabularies.close() 
    except IOError:
        pass

    doc = r"""
    </table>
    </div>
    </body>
    </html>
    """
    handler_to_file.write(doc)
    handler_to_file.close()


if __name__ == '__main__':
    #changing the name of a running process for a better overview of the means utilized
    if platform.system() == "Linux":
        LIBC = ctypes.CDLL('libc.so.6')
        PROC_NAME = "voctohtml"
        LIBC.prctl(15, '%s\0' %PROC_NAME, 0, 0, 0)
        #a delay of 1s
        sleep(1)

    FILE_NAME = "vocabularies-in-html"
    COUNTER = 100
    
    #main thread
    main()
