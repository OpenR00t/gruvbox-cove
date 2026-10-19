# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
"""Render specimens/cove-sans-family.png.
Usage: python cove_specimen.py <dir with CoveSans-*.ttf> <CaskaydiaCoveNerdFont-Regular.ttf> <label font .ttf> <out.png>"""
import sys
from PIL import Image, ImageDraw, ImageFont
D=sys.argv[1].rstrip("/\\")+"/"; BG=(29,32,33); CARD=(40,40,40); FG=(235,219,178); FG0=(251,241,199); GRAY=(146,131,116); GREEN=(184,187,38); AQUA=(142,192,124); BLUE=(131,165,152); BG2=(80,73,69)
L=ImageFont.truetype(sys.argv[3],16)
W=1500; img=Image.new("RGB",(W,2050),BG); d=ImageDraw.Draw(img)
F=lambda s,z: ImageFont.truetype(D+f"CoveSans-{s}.ttf",z,layout_engine=ImageFont.Layout.RAQM)
d.text((36,26),"Cove Sans",font=F("Bold",44),fill=FG0)
d.text((300,44),"proportional CaskaydiaCove Nerd Font  ·  12 styles  ·  kerned  ·  Nerd icons kept",font=L,fill=GRAY)
y=100
def card(h,label):
    global y
    d.rounded_rectangle((24,y,W-24,y+h),radius=8,fill=CARD,outline=BG2); d.text((44,y+10),label,font=L,fill=AQUA); return y+38
yy=card(470,"weights")
for s in ["ExtraLight","Light","SemiLight","Regular","SemiBold","Bold"]:
    d.text((44,yy),s,font=L,fill=GRAY); d.text((230,yy-6),"The quick brown fox jumps over the lazy dog",font=F(s,30),fill=FG); 
    d.text((230,yy+32),"The quick brown fox jumps over the lazy dog",font=F(s+"Italic" if s!="Regular" else "Italic",30),fill=FG); yy+=70
y+=486
yy=card(300,"long read: Wikipedia body size")
para=("Beef is the culinary name for meat from cattle (Bos taurus). In prehistoric times, humans hunted aurochs and later "
"domesticated them. Since that time, numerous breeds of cattle have been bred specifically for the quality or quantity "
"of their meat. Today, beef is the third most widely consumed meat in the world, after pork and poultry.")
f=F("Regular",19); words=para.split(); line=""; 
fb=F("Bold",19); fi=F("Italic",19)
for w in words:
    t=(line+" "+w).strip()
    if d.textlength(t,font=f)>W-100: d.text((44,yy),line,font=f,fill=FG); yy+=31; line=w
    else: line=t
d.text((44,yy),line,font=f,fill=FG); yy+=44
d.text((44,yy),"Mixed:",font=fb,fill=FG0); x=44+d.textlength("Mixed: ",font=fb)
d.text((x,yy),"bold, ",font=fb,fill=FG0); x+=d.textlength("bold, ",font=fb)
d.text((x,yy),"italic cursive forms, ",font=fi,fill=FG); x+=d.textlength("italic cursive forms, ",font=fi)
d.text((x,yy),"and a link.",font=f,fill=BLUE)
y+=316
yy=card(250,"kerning: off (top) vs on (bottom)")
k="AVATAR  Tokyo  Te Ty Ta  Wave  Yoga  P. F, L'  r.  y,  “Quote”"
fk=F("Regular",32)
d.text((44,yy),k,font=fk,fill=GRAY,features=["-kern"]); yy+=52
d.text((44,yy),k,font=fk,fill=FG0); yy+=60
d.text((44,yy),"Bold:",font=L,fill=GRAY); d.text((110,yy-6),k,font=F("Bold",32),fill=FG0)
y+=266
yy=card(250,"checks: accents, numbers, no code ligatures, Nerd icons")
fz=F("Regular",28)
d.text((44,yy),"café naïve façade Ærø Łódź Ελληνικά Кириллица",font=fz,fill=FG); yy+=46
d.text((44,yy),"0123456789  ½ ¾  $1,299.95  10:45  2026-10-16",font=fz,fill=FG); yy+=46
d.text((44,yy),"-> => != == <= >= ::  stay separate characters",font=fz,fill=FG); yy+=46
icons="            "
d.text((44,yy),icons+"   github  rust  code  folder  terminal  shell  gear",font=fz,fill=GREEN)
y+=266
yy=card(300,"pairs with: CaskaydiaCove Nerd Font for code, same letters")
mono=ImageFont.truetype(sys.argv[2],20)
d.text((44,yy),"Install the theme by pasting the stylesheet into the snippet box:",font=F("Regular",20),fill=FG); yy+=38
d.rounded_rectangle((44,yy,W-60,yy+120),radius=6,fill=BG)
for i,l in enumerate([".comment:not(#_) {","  background: var(--bg-h) !important;  /* -> beats RES */","}"]):
    d.text((60,yy+12+i*34),l,font=mono,fill=[FG,(254,128,25),FG][i])
yy+=140; d.text((44,yy),"Code above is CaskaydiaCove; this sentence is Cove Sans.",font=F("Italic",20),fill=GRAY)
img=img.crop((0,0,W,y+330)); img.save(sys.argv[4]); print(img.size)
