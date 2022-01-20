import sys
import os

# First arguemnt is the filename
# Second arguemnt is the encoding:  8 => UTF-8 ; 16 => UTF-16
# Output file is filename.heb.extension

CONVERT_TABLE_GIBBERISH = ["à", "á", "â", "ã", "ä", "å", "æ", "ç", "è", "é", "ë", "ì", "î", "ð", "ñ", "ò", "ô", "ö", "÷", "ø", "ù", "ú", "ê", "í", "ï", "ó", "õ"]
CONVERT_TABLE_HEBREW = ["א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ", "ל", "מ", "נ", "ס", "ע", "פ", "צ", "ק", "ר", "ש", "ת", "ך", "ם", "ן", "ף", "ץ"]

ENCODING = {}
ENCODING['8'] = 'utf-8'
ENCODING['16'] = 'utf-16'

args = sys.argv.copy()
args.pop(0)


file_name, file_extension = os.path.splitext(args[0]) 
new_file_name = file_name + '.heb' + file_extension
encoding = ENCODING[args[1]]

file_already_exists = os.path.exists('./{new_file_name}'.format(new_file_name=new_file_name))

if file_already_exists:
    print("Output file already exists.\nAborting operation!")
    exit



with open(new_file_name, 'wb+') as out_file:
    out_lines = []
    with open(file_name + file_extension, 'r', encoding=encoding) as in_file:
        in_lines = in_file.readlines()
        for in_line in in_lines:
            orig_in_line = in_line
            for index, gib_char in enumerate(CONVERT_TABLE_GIBBERISH):
                in_line = in_line.replace(gib_char, CONVERT_TABLE_HEBREW[index])
            out_lines.append(in_line.encode(encoding)) 
            # print(orig_in_line == in_line)   
            # print(orig_in_line)
            # print(in_line.encode('utf-8'))
    out_file.writelines(out_lines)


