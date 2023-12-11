import tkinter as tk
from tkinter import messagebox


class Unicode_to_Basic:

    def __init__(self):
        #Builds sets that can house each permutation of a letter, which can then be compared to.
        #   Blocks to have conversion done on their Letters.
        #	    Basic Latin, U+0000 to U+007F
        #	    Mathematical Alphanumeric Symbols, U+1D400 to U+1D7FF
        #	    Enclosed Alphanumeric Supplement, U+1F100 to U+1F1FF
        #	    IPA Extensions, U+0250 to U+02AF
        #	    Letterlike Symbols, U+2100 to U+214F
        #	    Enclosed Alphanumerics, U+2460 to U+24FF
        #	    Halfwidth and Fullwidth Forms, U+FF00 to U+FFEF
        #
        #   Blocks to consider as potential additions, though - out of scope due to technically introducing translation errors without context checking.
        #       Example. Latin letters are present as genuine language, but sometimes used as a point of graphic design / font.
        #       Another example. Cyrillic. Same thing, some letters are used stylistically / as fonts. But introduces translation errors.
        #       Making definitive selective decisions is beyond my linguistic expertise.
        #	        Latin Extended-A, U+0100 to U+017F
        #	        Cyrillic Supplement, U+0500 to U+052F
        #	        Latin-1 Supplement, U+0080 to U+00FF
        #	        Latin Extended-B, U+A720 to U+A7FF
        #	        Latin Extended-C, U+2C60 to U+2C7F
        #	        Cyrillic, U+0400 to U+04FF
        #	        Greek and Coptic, U+0370 to U+03FF
        #	        Armenian, U+0530 to U+058F
        #	        Georgian Supplement, U+2D00 to U+2D2F
        #	        Coptic, U+2C80 to U+2CFF
        #	        Latin Extended-D, U+A720 to U+A7FF
        #	        Latin Extended-E, U+AB30 to U+AB6F
        #	        Phonetic Extensions, U+1D00 to U+1D7F


        #Build the GUI to take and provide data via a class.
        print("Class Unicode_to_Basic Begin.")

        self.gui_UTB = tk.Tk()

        self.name_UTB = tk.Label(self.gui_UTB, text="Unicode to Basic Text Converter", font=('Arial', 18))
        self.name_UTB.pack(padx=10, pady=10)

        #Build the Interactive Elements; input text, buttons.
        self.inputText_UTB = tk.Text(self.gui_UTB, height=5, font=('Arial', 18))
        self.inputText_UTB.pack(padx=10, pady=10)

        self.plaintext_user = self.inputText_UTB.get("1.0",'end-1c')
        print(self.plaintext_user)
        self.reset_state = 0

        self.button = tk.Button(self.gui_UTB, text="Convert Unicode", font=('Arial', 18), command=lambda: [self.rebuild(), self.convert()])
        self.button.pack(padx=10, pady=10)

        #Build options for counting non-standard unicode characters.
        self.unicodeCounterState_UTB = tk.IntVar()
        self.unicodeCounterCheck_UTB = tk.Checkbutton(self.gui_UTB, text="Show Non-Basic Character Count", font=('Arial', 16), variable=self.unicodeCounterState_UTB)
        self.unicodeCounterCheck_UTB.pack(padx=10, pady=10)
        self.unicodeCounterLabelText_UTB = tk.StringVar()
        self.unicodeCounterLabel_UTB = tk.Label(self.gui_UTB, textvariable=self.unicodeCounterLabelText_UTB, font=('Arial', 8))
        self.unicodeCounterLabel_UTB.pack(padx=10, pady=10)

        #Build the Read Only Output Text element.
        self.outputTextConversion_UTB = tk.StringVar()
        self.outputText_UTB = tk.Text(self.gui_UTB, height=5, font=('Arial', 18))
        self.outputText_UTB.config(state='disabled')
        self.outputText_UTB.pack(padx=10, pady=10)

        # Close class mainloop.
        self.gui_UTB.mainloop()


    def rebuild(self):
        #Primes the outputText_UTB field for repeated use. Prevents buildup of previous queries.

        print("Function rebuild end.")

        #If the outputText field has previously been populated, on next pass's initialization, clear the field.
        if self.reset_state == 1:
            self.outputText_UTB.config(state='normal')
            self.outputText_UTB.delete('1.0',tk.END)
            self.outputText_UTB.config(state='disabled')
            self.reset_state = 0

        print("Function rebuild end.")

    def convert(self):
        #Dictates the logic for conversion for any given letter character.
        #
        #   The goal here would be to instead of using a field of constants, call to into the function.
        #       Same idea, but may help with error checking, and also just keeping things neat.
        #
        #   So, we would accept input from a tkinter window for a string. We would have that in data stored.
        #       In our case, we probably need to run a for or while loop to iterate through each character in set.
        #           This can be next.
        #
        #   This logic can be called while iterating, we run each character through the Match.
        #
        #   53 sets.
        #   Each lowercase and capital case letter corresponds to a Case with an IN check.
        #     Each Case's IN check has each Unicode Block variation to a given lowercase or capitalcase letter.
        #       If character is matched for a special unicode character, convert to the Basic set.
        #       If character is not matched, keep it as is and move to the next.
        #   Non-Leter Symbols need a set for the purposes of determining non-standard unicode count.
        #
        print("Function Convert Begin.")

        #Assemble all relevant blocks of Unicode characters into comparable sets.
        a_Set = ["𝐚","𝑎","𝒂","𝖺","𝗮","𝘢","𝙖","𝒶","𝓪","𝔞","𝖆","𝚊","𝕒","𝕒","ⓐ","ａ"]
        b_Set = ["𝐛","𝑏","𝒃","𝖻","𝗯","𝘣","𝙗","𝒷","𝓫","𝔟","𝖇","𝚋","𝕓","𝕓","ⓑ","ｂ"]
        c_Set = ["𝐜","𝑐","𝒄","𝖼","𝗰","𝘤","𝙘","𝒸","𝓬","𝔠","𝖈","𝚌","𝕔","𝕔","ⓒ","ｃ"]
        d_Set = ["𝐝","𝑑","𝒅","𝖽","𝗱","𝘥","𝙙","𝒹","𝓭","𝔡","𝖉","𝚍","𝕕","𝕕","ⓓ","ｄ"]
        e_Set = ["𝐞","𝑒","𝒆","𝖾","𝗲","𝘦","𝙚","ℯ","𝓮","𝔢","𝖊","𝚎","𝕖","𝕖","ⓔ","ｅ"]
        f_Set = ["𝐟","𝑓","𝒇 ","𝖿","𝗳","𝘧","𝙛","𝒻","𝓯","𝔣","𝖋","𝚏","𝕗","𝕗","ⓕ","ｆ"]
        g_Set = ["𝐠","𝑔","𝒈","𝗀","𝗴","𝘨","𝙜","ℊ","𝓰","𝔤","𝖌","𝚐","𝕘","𝕘","ⓖ","ｇ"]
        h_Set = ["𝐡","ℎ","𝒉","𝗁","𝗵","𝘩","𝙝","𝒽","𝓱","𝔥","𝖍","𝚑","𝕙","𝕙","ⓗ","ｈ"]
        i_Set = ["𝐢","𝑖","𝒊","𝗂","𝗶","𝘪","𝙞","𝒾","𝓲","𝔦","𝖎","𝚒","𝕚","𝚤","𝕚","ⓘ","ｉ"]
        j_Set = ["𝐣","𝑗","𝒋","𝗃","𝗷","𝘫","𝙟","𝒿","𝓳","𝔧","𝖏","𝚓","𝕛","𝚥","𝕛","ⓙ","ｊ"]
        k_Set = ["𝐤","𝑘","𝒌","𝗄","𝗸","𝘬","𝙠","𝓀","𝓴","𝔨","𝖐","𝚔","𝕜","𝕜","ⓚ","ｋ"]
        l_Set = ["𝐥","𝑙","𝒍","𝗅","𝗹","𝘭","𝙡","𝓁","𝓵","𝔩","𝖑","𝚕","𝕝","𝕝","ⓛ","ｌ"]
        m_Set = ["𝐦","𝑚","𝒎","𝗆","𝗺","𝘮","𝙢","𝓂","𝓶","𝔪","𝖒","𝚖","𝕞","𝕞","ⓜ","ｍ"]
        n_Set = ["𝐧","𝑛","𝒏","𝗇","𝗻","𝘯","𝙣","𝓃","𝓷","𝔫","𝖓","𝚗","𝕟","𝕟","ⓝ","ｎ"]
        o_Set = ["𝐨","𝑜","𝒐","𝗈","𝗼","𝘰","𝙤","ℴ","𝓸","𝔬","𝖔","𝚘","𝕠","𝕠","ⓞ","ｏ"]
        p_Set = ["𝐩","𝑝","𝒑","𝗉","𝗽","𝘱","𝙥","𝓅","𝓹","𝔭","𝖕","𝚙","𝕡","𝕡","ⓟ","ｐ"]
        q_Set = ["𝐪","𝑞","𝒒","𝗊","𝗾","𝘲","𝙦","𝓆","𝓺","𝔮","𝖖","𝚚","𝕢","𝕢","ⓠ","ｑ"]
        r_Set = ["𝐫","𝑟","𝒓","𝗋","𝗿","𝘳","𝙧","𝓇","𝓻","𝔯","𝖗","𝚛","𝕣","𝕣","ⓡ","ｒ"]
        s_Set = ["𝐬","𝑠","𝒔","𝗌","𝘀","𝘴","𝙨","𝓈","𝓼","𝔰","𝖘","𝚜","𝕤","𝕤","ⓢ","ｓ"]
        t_Set = ["𝐭","𝑡","𝒕","𝗍","𝘁","𝘵","𝙩","𝓉","𝓽","𝔱","𝖙","𝚝","𝕥","𝕥","ⓣ","ｔ"]
        u_Set = ["𝐮","𝑢","𝒖","𝗎","𝘂","𝘶","𝙪","𝓊","𝓾","𝔲","𝖚","𝚞","𝕦","𝕦","ⓤ","ｕ"]
        v_Set = ["𝐯","𝑣","𝒗","𝗏","𝘃","𝘷","𝙫","𝓋","𝓿","𝔳","𝖛","𝚟","𝕧","𝕧","ⓥ","ｖ"]
        w_Set = ["𝐰","𝑤","𝒘","𝗐","𝘄","𝘸","𝙬","𝓌","𝔀","𝔴","𝖜","𝚠","𝕨","𝕨","ⓦ","ｗ"]
        x_Set = ["𝐱","𝑥","𝒙","𝗑","𝘅","𝘹","𝙭","𝓍","𝔁","𝔵","𝖝","𝚡","𝕩","𝕩","ⓧ","ｘ"]
        y_Set = ["𝐲","𝑦","𝒚","𝗒","𝘆","𝘺","𝙮","𝓎","𝔂","𝔶","𝖞","𝚢","𝕪","𝕪","ⓨ","ｙ"]
        z_Set = ["𝐳","𝑧","𝒛","𝗓","𝘇","𝘻","𝙯","𝓏","𝔃","𝔷","𝖟","𝚣","𝕫","𝕫","ⓩ","ｚ"]
        capA_Set = ["𝐀","𝐴","𝑨","𝖠","𝗔","𝘈","𝘼","𝒜","𝓐","𝔄","𝕬","𝙰","𝔸","ᴀ","🄐","🄰","🅐","🅰","🇦","𝔸","Ⓐ","Ａ"]
        capB_Set = ["𝐁","𝐵","𝑩","𝖡","𝗕","𝘉","𝘽","ℬ","𝓑","𝔅","𝕭","𝙱","𝔹","ʙ","🄑","🄱","🅑","🅱","🇧","Ⓑ","Ｂ"]
        capC_Set = ["𝐂","𝐶","𝑪","𝖢","𝗖","𝘊","𝘾","𝒞","𝓒","ℭ","𝕮","𝙲","ℂ","ᴄ","🄒","🄲","🅒","🅲","🇨","ℂ","Ⓒ","Ｃ"]
        capD_Set = ["𝐃","𝐷","𝑫","𝖣","𝗗","𝘋","𝘿","𝒟","𝓓","𝔇","𝕯","𝙳","𝔻","ᴅ","🄓","🄳","🅓","🅳","🇩","𝔻","Ⓓ","Ｄ"]
        capE_Set = ["𝐄","𝐸","𝑬","𝖤","𝗘","𝘌","𝙀","ℰ","𝓔","𝔈","𝕰","𝙴","𝔼","ᴇ","🄔","🄴","🅔","🅴","🇪","𝔼","Ⓔ","Ｅ"]
        capF_Set = ["𝐅","𝐹","𝑭","𝖥","𝗙","𝘍","𝙁","ℱ","𝓕","𝔉","𝕱","𝙵","𝔽","ꜰ","🄕","🄵","🅕","🅵  ","🇫","𝔽","Ⓕ","Ｆ"]
        capG_Set = ["𝐆","𝐺","𝑮","𝖦","𝗚","𝘎","𝙂","𝒢","𝓖","𝔊","𝕲","𝙶","𝔾","ɢ","🄖","🄶","🅖","🅶","🇬","𝔾","Ⓖ","Ｇ"]
        capH_Set = ["𝐇","𝐻","𝑯","𝖧","𝗛","𝘏","𝙃","ℋ","𝓗","ℌ","𝕳","𝙷","ℍ","ʜ","🄗","🄷","🅗","🅷","🇭","ℍ","Ⓗ","Ｈ"]
        capI_Set = ["𝐈","𝐼","𝑰","𝖨","𝗜","𝘐","𝙄","ℐ","𝓘","ℑ","𝕴","𝙸","𝕀","ɪ","🄘","🄸","🅘","🅸","🇮","𝕀","Ⓘ","Ｉ"]
        capJ_Set = ["𝐉","𝐽","𝑱","𝖩","𝗝","𝘑","𝙅","𝒥","𝓙","𝔍","𝕵","𝙹","𝕁","ᴊ","🄙","🄹","🅙","🅹","🇯","𝕁","Ⓙ","Ｊ"]
        capK_Set = ["𝐊","𝐾","𝑲","𝖪","𝗞","𝘒","𝙆","𝒦","𝓚","𝔎","𝕶","𝙺","𝕂","ᴋ","🄚","🄺","🅚","🅺","🇰","𝕂","Ⓚ","Ｋ"]
        capL_Set = ["𝐋","𝐿","𝑳","𝖫","𝗟","𝘓","𝙇","ℒ","𝓛","𝔏","𝕷","𝙻","𝕃","ʟ","🄛","🄻","🅛","🅻","🇱","𝕃","Ⓛ","Ｌ"]
        capM_Set = ["𝐌","𝑀","𝑴","𝖬","𝗠","𝘔","𝙈","ℳ","𝓜","𝔐","𝕸","𝙼","𝕄","ᴍ","🄜","🄼","🅜","🅼","🇲","𝕄","Ⓜ","Ｍ"]
        capN_Set = ["𝐍","𝑁","𝑵","𝖭","𝗡","𝘕","𝙉","𝒩","𝓝","𝔑","𝕹","𝙽","ℕ","ɴ","🄝","🄽","🅝","🅽","🇳","ℕ","Ⓝ","Ｎ"]
        capO_Set = ["𝐎","𝑂","𝑶","𝖮","𝗢","𝘖","𝙊","𝒪","𝓞","𝔒","𝕺","𝙾","𝕆","ᴏ","🄞","🄾","🅞","🅾","🇴","𝕆","Ⓞ","Ｏ"]
        capP_Set = ["𝐏","𝑃","𝑷","𝖯","𝗣","𝘗","𝙋","𝒫","𝓟","𝔓","𝕻","𝙿","ℙ","ᴘ","🄟","🄿","🅟","🅿","🇵","ℙ","Ⓟ","Ｐ"]
        capQ_Set = ["𝐐","𝑄","𝑸","𝖰","𝗤","𝘘","𝙌","𝒬","𝓠","𝔔","𝕼","𝚀","ℚ","ꞯ","🄠","🅀","🅠","🆀","🇶","ℚ","Ⓠ","Ｑ"]
        capR_Set = ["𝐑","𝑅","𝑹","𝖱","𝗥","𝘙","𝙍","ℛ","𝓡","ℜ","𝕽","𝚁","ℝ","ʀ","🄡","🅁","🅡","🆁","🇷","ℝ","Ⓡ","Ｒ"]
        capS_Set = ["𝐒","𝑆","𝑺","𝖲","𝗦","𝘚","𝙎","𝒮","𝓢","𝔖","𝕾","𝚂","𝕊","ꜱ","🄢","🅂","🅢","🆂","🇸","𝕊","Ⓢ","Ｓ"]
        capT_Set = ["𝐓","𝑇","𝑻","𝖳","𝗧","𝘛","𝙏","𝒯","𝓣","𝔗","𝕿","𝚃","𝕋","ᴛ","🄣","🅃","🅣","🆃","🇹","𝕋","Ⓣ","Ｔ"]
        capU_Set = ["𝐔","𝑈","𝑼","𝖴","𝗨","𝘜","𝙐","𝒰","𝓤","𝔘","𝖀","𝚄","𝕌","ᴜ","🄤","🅄","🅤","🆄","🇺","𝕌","Ⓤ","Ｕ"]
        capV_Set = ["𝐕","𝑉","𝑽","𝖵","𝗩","𝘝","𝙑","𝒱","𝓥","𝔙","𝖁","𝚅","𝕍","ᴠ","🄥","🅅","🅥","🆅","🇻","𝕍","Ⓥ","Ｖ"]
        capW_Set = ["𝐖","𝑊","𝑾","𝖶","𝗪","𝘞","𝙒","𝒲","𝓦","𝔚","𝖂","𝚆","𝕎","ᴡ","🄦","🅆","🅦","🆆","🇼","𝕎","Ⓦ","Ｗ"]
        capX_Set = ["𝐗","𝑋","𝑿","𝖷","𝗫","𝘟","𝙓","𝒳","𝓧","𝔛","𝖃","𝚇","𝕏","🄧","🅇","🅧","🆇","🇽","𝕏","Ⓧ","Ｘ"]
        capY_Set = ["𝐘","𝑌","𝒀","𝖸","𝗬","𝘠","𝙔","𝒴  ","𝓨","𝔜","𝖄","𝚈","𝕐","ʏ","🄨","🅈","🅨","🆈","🇾","𝕐","Ⓨ","Ｙ"]
        capZ_Set = ["𝐙","𝑍","𝒁","𝖹","𝗭","𝘡","𝙕","𝒵","𝓩","ℨ","𝖅","𝚉","ℤ","ᴢ","🄩","🅉","🅩","🆉","🇿","ℤ","Ⓩ","Ｚ"]
        otherBasic_Set = ["\u0000", "\u0001", "\u0002", "\u0003", "\u0004", "\u0005", "\u0006", "\u0007", "\u0008", "\u0009", "\u000A", "\u000B", "\u000C", "\u000D", "\u000E", "\u000F", "\u0010", "\u0011", "\u0012", "\u0013", "\u0014", "\u0015", "\u0016", "\u0017", "\u0018", "\u0019", "\u001A", "\u001B", "\u001C", "\u001D", "\u001E", "\u001F", "\u0020", "\u0021", "\u0022", "\u0023", "\u0024", "\u0025", "\u0026", "\u0027", "\u0028", "\u0029", "\u002A", "\u002B", "\u002C", "\u002D", "\u002E", "\u002F", "\u0030", "\u0031", "\u0032", "\u0033", "\u0034", "\u0035", "\u0036", "\u0037", "\u0038", "\u0039", "\u003A", "\u003B", "\u003C", "\u003D", "\u003E", "\u003F", "\u0040", "\u005B", "\u005C", "\u005D", "\u005E", "\u005F", "\u0060", "\u007B", "\u007C", "\u007D", "\u007E", "\u007F"]

        #Gather data to be converted from inputText and hold it in a less volatile location.
        #Also, reset the Unicode count if being used.
        ciphertext_function = self.inputText_UTB.get('1.0',tk.END)
        self.unicodeCount = 0

        #Get the length of the submission to determine loop termination, so we can step through per-character.
        #Add each character iterated through to a string that we curate / translate to.
        plaintext_length = len(ciphertext_function)
        plaintext_iterations = 0
        converted_text = ""

        #Secondary program loop.
        #   Do Conversion While Current  i-th character is <= the total number of characters submitted.
        while plaintext_iterations < plaintext_length:
            print(ciphertext_function[plaintext_iterations])

            #Denote the characater we are on  by the number of iterations we've done, and the length of the string array.
            plaintext_character = ciphertext_function[plaintext_iterations]

            #Match the character to one of our cases.
            #   When matched: Print to console, add relevant character to curated string, increment unicode counter if relevant.
            match ciphertext_function:

                case letter_A if plaintext_character in capA_Set:
                    print("You have input an A.")
                    converted_text = converted_text + "A"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_B if plaintext_character in capB_Set:
                    print("You have input an B.")
                    converted_text = converted_text + "B"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_C if plaintext_character in capC_Set:
                    print("You have input an C.")
                    converted_text = converted_text + "C"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_D if plaintext_character in capD_Set:
                    print("You have input an D.")
                    converted_text = converted_text + "D"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_E if plaintext_character in capE_Set:
                    print("You have input an E.")
                    converted_text = converted_text + "E"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_F if plaintext_character in capF_Set:
                    print("You have input an F.")
                    converted_text = converted_text + "F"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_G if plaintext_character in capG_Set:
                    print("You have input an G.")
                    converted_text = converted_text + "G"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_H if plaintext_character in capH_Set:
                    print("You have input an H.")
                    converted_text = converted_text + "H"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_I if plaintext_character in capI_Set:
                    print("You have input an I.")
                    converted_text = converted_text + "I"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_J if plaintext_character in capJ_Set:
                    print("You have input an J.")
                    converted_text = converted_text + "J"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_K if plaintext_character in capK_Set:
                    print("You have input an K.")
                    converted_text = converted_text + "K"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_L if plaintext_character in capL_Set:
                    print("You have input an L.")
                    converted_text = converted_text + "L"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_M if plaintext_character in capM_Set:
                    print("You have input an M.")
                    converted_text = converted_text + "M"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_N if plaintext_character in capN_Set:
                    print("You have input an N.")
                    converted_text = converted_text + "N"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_O if plaintext_character in capO_Set:
                    print("You have input an O.")
                    converted_text = converted_text + "O"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_P if plaintext_character in capP_Set:
                    print("You have input an P.")
                    converted_text = converted_text + "P"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_Q if plaintext_character in capQ_Set:
                    print("You have input an Q.")
                    converted_text = converted_text + "Q"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_R if plaintext_character in capR_Set:
                    print("You have input an R.")
                    converted_text = converted_text + "R"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_S if plaintext_character in capS_Set:
                    print("You have input an S.")
                    converted_text = converted_text + "S"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_T if plaintext_character in capT_Set:
                    print("You have input an T.")
                    converted_text = converted_text + "T"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_U if plaintext_character in capU_Set:
                    print("You have input an U.")
                    converted_text = converted_text + "U"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_V if plaintext_character in capV_Set:
                    print("You have input an V.")
                    converted_text = converted_text + "V"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_W if plaintext_character in capW_Set:
                    print("You have input an W.")
                    converted_text = converted_text + "W"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_X if plaintext_character in capX_Set:
                    print("You have input an X.")
                    converted_text = converted_text + "X"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_Y if plaintext_character in capY_Set:
                    print("You have input an Y.")
                    converted_text = converted_text + "Y"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_Z if plaintext_character in capZ_Set:
                    print("You have input an Z.")
                    converted_text = converted_text + "Z"
                    self.unicodeCount = self.unicodeCount + 1

                case letter_a if plaintext_character in a_Set:
                    print("You have input an a.")
                    converted_text = converted_text + "a"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_b if plaintext_character in b_Set:
                    print("You have input an b.")
                    converted_text = converted_text + "b"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_c if plaintext_character in c_Set:
                    print("You have input an c.")
                    converted_text = converted_text + "c"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_d if plaintext_character in d_Set:
                    print("You have input an d.")
                    converted_text = converted_text + "d"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_e if plaintext_character in e_Set:
                    print("You have input an e.")
                    converted_text = converted_text + "e"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_f if plaintext_character in f_Set:
                    print("You have input an f.")
                    converted_text = converted_text + "f"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_g if plaintext_character in g_Set:
                    print("You have input an g.")
                    converted_text = converted_text + "g"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_h if plaintext_character in h_Set:
                    print("You have input an h.")
                    converted_text = converted_text + "h"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_i if plaintext_character in i_Set:
                    print("You have input an i.")
                    converted_text = converted_text + "i"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_j if plaintext_character in j_Set:
                    print("You have input an j.")
                    converted_text = converted_text + "j"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_k if plaintext_character in k_Set:
                    print("You have input an k.")
                    converted_text = converted_text + "k"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_l if plaintext_character in l_Set:
                    print("You have input an l.")
                    converted_text = converted_text + "l"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_m if plaintext_character in m_Set:
                    print("You have input an m.")
                    converted_text = converted_text + "m"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_n if plaintext_character in n_Set:
                    print("You have input an n.")
                    converted_text = converted_text + "n"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_o if plaintext_character in o_Set:
                    print("You have input an o.")
                    converted_text = converted_text + "o"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_p if plaintext_character in p_Set:
                    print("You have input an p.")
                    converted_text = converted_text + "p"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_q if plaintext_character in q_Set:
                    print("You have input an q.")
                    converted_text = converted_text + "q"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_r if plaintext_character in r_Set:
                    print("You have input an r.")
                    converted_text = converted_text + "r"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_s if plaintext_character in s_Set:
                    print("You have input an s.")
                    converted_text = converted_text + "s"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_t if plaintext_character in t_Set:
                    print("You have input an t.")
                    converted_text = converted_text + "t"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_u if plaintext_character in u_Set:
                    print("You have input an u.")
                    converted_text = converted_text + "u"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_v if plaintext_character in v_Set:
                    print("You have input an v.")
                    converted_text = converted_text + "v"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_w if plaintext_character in w_Set:
                    print("You have input an w.")
                    converted_text = converted_text + "w"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_x if plaintext_character in x_Set:
                    print("You have input an x.")
                    converted_text = converted_text + "x"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_y if plaintext_character in y_Set:
                    print("You have input an y.")
                    converted_text = converted_text + "y"
                    self.unicodeCount = self.unicodeCount + 1
                case letter_z if plaintext_character in z_Set:
                    print("You have input an z.")
                    converted_text = converted_text + "z"
                    self.unicodeCount = self.unicodeCount + 1

                case letter_otherBasic if plaintext_character in otherBasic_Set:
                    print("You have entered a non-letter Basic Latin character.")
                    converted_text = converted_text + ciphertext_function[plaintext_iterations]

                case letter if letter not in capH_Set:
                    print("You have entered a Basic Latin letter character.")
                    converted_text = converted_text + ciphertext_function[plaintext_iterations]

                    # __not in__ catches blanks. If it hadn't, the below could have been useful.
                    # case _:
                    #    print("You have input nothing.")
            #self.outputTextConversion_UTB = tk.StringVar()

            #Iterate the loop.
            plaintext_iterations = plaintext_iterations + 1

        #Print converted string to console. Unlock the read only output text field, insert converted string there, lock the read only text field.
        print(converted_text)
        self.outputText_UTB.config(state='normal')
        self.outputText_UTB.insert(tk.END, converted_text)
        self.outputText_UTB.config(state='disabled')

        #Print state of unicode counter selection.
        #   If non-standard unicode character count desired, print it to a selectively visible label.
        print(self.unicodeCounterState_UTB.get())
        if self.unicodeCounterState_UTB.get() == 1:
            self.unicodeCounterLabelText_UTB.set("Total non-Basic Latin characters detected: " + str(self.unicodeCount))

        #Flag that the converter has gone through an iteration, and the output text field needs cleared.
        self.reset_state = 1

        print("Function Convert end.")


    print("Class Letter end.")


Unicode_to_Basic()