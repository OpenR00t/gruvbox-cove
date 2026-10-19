# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
import xml.etree.ElementTree as ET, re, collections, sys
P=dict(bg_h="1D2021",bg0="282828",bg0_s="32302F",bg1="3C3836",bg2="504945",bg3="665C54",bg4="7C6F64",
 fg0="FBF1C7",fg="EBDBB2",fg2="D5C4A1",fg3="BDAE93",fg4="A89984",gray="928374",
 red="FB4934",green="B8BB26",yellow="FABD2F",blue="83A598",purple="D3869B",aqua="8EC07C",orange="FE8019",
 red_d="CC241D",green_d="98971A",yellow_d="D79921",blue_d="458588",purple_d="B16286",aqua_d="689D6A",orange_d="D65D0E")
NORMAL,BOLD,ITALIC,BI,UNDER=0,1,2,3,4
USERKW=["red","aqua","yellow","purple","orange","blue","green","fg2"]
def classify(name):
    n=name.upper()
    toks=[t for t in re.split(r'[^A-Z0-9]+',n) if t]
    def has(*ws):
        for w in ws:
            if ' ' in w:
                if w in n: return True
            elif any(t.startswith(w) for t in toks): return True
        return False
    m=re.search(r'USER KEYWORDS (\d)',n) or re.search(r'KEYWORDS? ?(\d)$',n)
    if has('COMMENT'):
        if has('ERROR'): return 'red',ITALIC
        if has('DOC KEYWORD','TAG','KEYWORD'): return 'aqua',ITALIC
        return 'gray',ITALIC
    if has('ERROR','BAD','WRONG','UNKNOWN','INVALID','ILLEGAL'): return 'red',NORMAL
    if has('DELETED','REMOVED'): return 'red',NORMAL
    if has('ADDED','INSERTED'): return 'green',NORMAL
    if has('CHANGED'): return 'blue',NORMAL
    if has('REGEX','ESCAPE','INTERPOLAT'): return 'orange',NORMAL
    if has('STRING','CHAR','QUOTE','QUOTED','VERBATIM','BACKTICK','HEREDOC','HERE','LITERAL','CDATA','TRIPLE'): return 'green',NORMAL
    if has('NUMBER','NUMERIC','HEX','HEXNUMBER','BINNUMBER','FLOAT','INTEGER','CONSTANT','BOOLEAN','DATE'): return 'purple',NORMAL
    if has('PREPROCESSOR','DIRECTIVE','MACRO','PRAGMA','INCLUDE','IMPORT','DECORATOR','ANNOTATION','DEFINE'): return 'aqua',NORMAL
    if has('FUNCTION','METHOD','DEFNAME','DEF NAME','CALL','SUBROUTINE'): return 'green',BOLD
    if has('CMDLET','ALIAS'): return 'aqua',NORMAL
    if has('INSTRUCTION'): return 'red',NORMAL
    if has('TYPE','CLASS','STRUCT','INTERFACE','ENUM'): return 'yellow',NORMAL
    if has('ATTRIBUTE','ATTR'): return 'yellow',NORMAL
    if has('TAG','ELEMENT'): return 'aqua',NORMAL
    if has('ENTITY'): return 'orange',NORMAL
    if has('SECTION','HEADER','HEADING','TITLE','CHAPTER'): return 'green',BOLD
    if has('STRONG','BOLD'): return 'fg0',BOLD
    if has('EMPHASIS','ITALIC'): return 'fg',ITALIC
    if has('CODE','PREFORMAT','INLINE'): return 'orange',NORMAL
    if has('URL','URI','LINK','HYPERLINK'): return 'blue',UNDER
    if m and has('USER','KEYWORD'): return USERKW[(int(m.group(1))-1)%8],NORMAL
    if has('BUILTIN'): return 'orange',NORMAL
    if has('KEYWORD','STATEMENT','RESERVED','COMMAND','WORD','PREDEFINED'): return 'red',NORMAL
    if has('LABEL','GOTO'): return 'red',NORMAL
    if has('OPERATOR','SYMBOL','DELIMITER','PUNCT','BRACE','BRACKET'): return 'orange',NORMAL
    if has('VARIABLE','PARAMETER','PARAM','SCALAR','PROPERTY','KEY','GLOBAL','FIELD'): return 'blue',NORMAL
    return 'fg',NORMAL

GLOBAL={ # name: (fg, bg, fontStyle or None)
 'Default Style':('fg','bg0',0),'Indent guideline style':('bg2','bg0',None),'Brace highlight style':('fg0','bg2',1),
 'Bad brace colour':('red','bg1',1),'Current line background colour':(None,'bg0_s',None),'Selected text colour':(None,'bg2',None),
 'Multi-selected text color':(None,'bg2',None),'Caret colour':('green',None,None),'Multi-edit carets color':('aqua',None,None),
 'Edge colour':('bg1',None,None),'Line number margin':('bg4','bg0',None),'Bookmark margin':(None,'bg0',None),
 'Change History margin':(None,'bg0',None),'Change History modified':('blue','blue',None),'Change History revert modified':('yellow_d','yellow_d',None),
 'Change History revert origin':('aqua','aqua',None),'Change History saved':('green','green',None),
 'Fold':('bg4','bg0',None),'Fold active':('green',None,None),'Fold margin':('bg0','bg0',None),'White space symbol':('bg2',None,None),
 'Smart Highlighting':(None,'bg3',None),'Find Mark Style':(None,'green_d',None),'Find status: Not found':('red',None,None),
 'Find status: Message':('blue',None,None),'Find status: Search end reached':('yellow',None,None),
 'Mark Style 1':(None,'aqua_d',None),'Mark Style 2':(None,'orange_d',None),'Mark Style 3':(None,'yellow_d',None),'Mark Style 4':(None,'blue_d',None),'Mark Style 5':(None,'purple_d',None),
 'Incremental highlight all':(None,'green_d',None),'Tags match highlighting':(None,'bg2',None),'Tags attribute':(None,'bg3',None),
 'Active tab focused indicator':('green',None,None),'Active tab unfocused indicator':('bg3',None,None),'Active tab text':('fg0',None,None),
 'Inactive tabs':('gray','bg_h',None),
 'Tab color 1':(None,'green_d',None),'Tab color 2':(None,'blue_d',None),'Tab color 3':(None,'orange_d',None),'Tab color 4':(None,'purple_d',None),'Tab color 5':(None,'red_d',None),
 'Tab color dark mode 1':(None,'green_d',None),'Tab color dark mode 2':(None,'blue_d',None),'Tab color dark mode 3':(None,'orange_d',None),'Tab color dark mode 4':(None,'purple_d',None),'Tab color dark mode 5':(None,'red_d',None),
 'URL hovered':('aqua',None,None),'Document map':('bg2','bg_h',None),'EOL custom color':('bg2',None,None),'Non-printing characters custom color':('bg2',None,None),
}
t=ET.parse(sys.argv[1]); r=t.getroot()
stats=collections.Counter()
for L in r.find('LexerStyles'):
    for w in L:
        col,st=classify(w.get('name',''))
        stats[col]+=1
        w.set('fgColor',P[col]); w.set('bgColor',P['bg0']); w.set('fontStyle',str(st))
        if 'fontName' in w.attrib: w.set('fontName','')
        if 'fontSize' in w.attrib: w.set('fontSize','')
missing=[]
for w in r.find('GlobalStyles'):
    n=w.get('name')
    if n=='Global override': continue
    if n not in GLOBAL: missing.append(n); continue
    fg,bg,st=GLOBAL[n]
    if fg: w.set('fgColor',P[fg])
    if bg: w.set('bgColor',P[bg])
    if st is not None: w.set('fontStyle',str(st))
    if n=='Default Style':
        w.set('fontName','CaskaydiaCove Nerd Font'); w.set('fontSize','11')
ET.indent(t,'    ')
xml=ET.tostring(r,encoding='unicode')
hdr='<?xml version="1.0" encoding="UTF-8" ?>\n<!--\n    Gruvbox Cove for Notepad++\n    Gruvbox dark: green accent (caret, active tab, fold, find marks), classic gruvbox syntax\n    (keywords red, strings green, functions green bold, types yellow, numbers purple, operators orange,\n    preprocessor aqua, comments gray italic). Font: CaskaydiaCove Nerd Font 11.\n    Built from Notepad++\'s stylers.model.xml by build_npp.py, so every language is covered.\n    SPDX-License-Identifier: AGPL-3.0-or-later\n    Copyright (C) 2026 The Gruvbox Cove contributors\n-->\n'
open(sys.argv[2],'w',encoding='utf-8').write(hdr+xml+'\n')
print(dict(stats)); print('unmapped global:',missing)
