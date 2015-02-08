# -*- coding: utf-8 -*-
# čžřě+áýčíáý+í
"""
name: voctohtml -- vocabulary HTML generator in Python 
autor: Černý Jan
email: cerny.jan@hotmail.com
version: 0.1
"""
#import - own packages
#import - system packages
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
    print "\r"
    print "*********************************************"
    print "voctohtml v0.1 \t autor: Černý Jan \t 2015"
    print "*********************************************"
    print "\r"
    #check the parameters
    if len(argv) < 2:
        print "program musi byt spusten s parametry !!"
        print "pro nápovědu zadejte -help"
        print "app down"
        exit()

    #help
    if argv[1] == "-help":
        print "HELP"
        print "===="
        print "přiklad spuštění -> python main.py -N ukazka01 10000 urls.txt -S -H -C -ST -F -dg"
        print "\n"
        print "-N"
        print "-R"
        print "-P"
        print "-E"
        print "\n"
        print "ukazka01 >> nazev vytvorene DB"
        print "\n"
        print "urls.txt >> soubor s URL adresami ze kterých se začíná pracovat"
        print "\n"
        print "volitelne prepinace pro zjistovani informaci o webu, minimalne jeden zvolte (-dg se do toho nepocita)"
        print "-S >> server"
        print "-H >> značkovací jazyk"
        print "-C >> CSS"
        print "-ST >> skriptovací jazyk"
        print "-F >> JavaScript framework"
        print "-dg >> vypis na konzoli"
        exit()

    #location
    try:
        file_of_vocabularies = codecs.open(argv[1], "r", "utf-8")
    except IOError:
        print "wrong input file"
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
        
    try:
        fh = codecs.open(argv[1], "r", "utf-8")
        gap = "&nbsp; – &nbsp;"
        gap = gap.decode("utf-8")
        doc_end = r"""
        </table>
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
            line = fh.readline().strip()
            line = line.encode('utf-8')
            line = line.decode("utf-8")
            if not line:
                break
            if line[(len(line)-2):] == "##":
                doc = r"""</i></td></tr>
                <tr class="header">
                    <td>original</td>
                    <td class="center">&nbsp;</td>
                    <td>translated</td>
                </tr>
                """
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
                COUNTER = 16
        fh.close() 
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
    #change name of running process
    LIBC = ctypes.CDLL('libc.so.6')
    PROC_NAME = "voctohtml"
    LIBC.prctl(15, '%s\0' %PROC_NAME, 0, 0, 0)
    #sleep for 1s
    sleep(1)

    FILE_NAME = "slovicka-en"
    COUNTER = 17
    
    #main thread
    main()