# Unicode-to-Basic
A simple piece of software written in Python that converts non-Basic Latin alphabetical characters to the Basic Latin block.

While I found very many converters that did the one-to-many step in this chain. Generating unicode in fancier / less common blocks? I could not find one doing the opposite. It was a harsh day, so I set about making my own.

Currently supporting the following blocks alphabetical characaters:
        #	    Basic Latin, U+0000 to U+007F
        #	    Mathematical Alphanumeric Symbols, U+1D400 to U+1D7FF
        #	    Enclosed Alphanumeric Supplement, U+1F100 to U+1F1FF
        #	    IPA Extensions, U+0250 to U+02AF
        #	    Letterlike Symbols, U+2100 to U+214F
        #	    Enclosed Alphanumerics, U+2460 to U+24FF
        #	    Halfwidth and Fullwidth Forms, U+FF00 to U+FFEF
