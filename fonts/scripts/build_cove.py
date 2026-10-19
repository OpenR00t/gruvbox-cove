# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
"""Build one Cove Sans style from a CaskaydiaCove Nerd Font style (FontForge Python).
Usage: python build_cove.py <CaskaydiaCoveNerdFont-Style.ttf> <outdir>"""
import fontforge, sys, os
src, outdir = sys.argv[1], sys.argv[2]
FAM = "Cove Sans"
style = os.path.basename(src).split("-")[-1].replace(".ttf","")      # e.g. SemiBoldItalic
italic = style.endswith("Italic")
weight = style[:-6] if italic else style
if weight == "": weight = "Regular"
pretty = (weight if weight != "Regular" else "") + (" Italic" if italic else "")
pretty = pretty.strip() or "Regular"
f = fontforge.open(src)
em = f.em

# 1. Drop programming-ligature lookups (calt) - they assume mono cells
for lk in list(f.gsub_lookups):
    feats = [ft[0] for ft in f.getLookupInfo(lk)[2]]
    if "calt" in feats:
        f.removeLookup(lk)

# 2. Respace every outline glyph except Nerd icons / box drawing / blocks
def skip(u):
    return (0xE000 <= u <= 0xF8FF) or (u >= 0xF0000) or (0x2500 <= u <= 0x259F) or (0x2800 <= u <= 0x28FF) or (0x1FB00 <= u <= 0x1FBFF)
f.selection.none(); n = 0
for g in f.glyphs():
    if g.unicode >= 0 and skip(g.unicode): continue
    if g.glyphname.startswith(("uniE", "uniF", "u0F")) and g.unicode < 0: continue
    if g.width == 0: continue                      # combining marks stay zero-width
    if not g.foreground or g.foreground.isEmpty():
        if not g.references: continue
    f.selection.select(("more",), g.glyphname); n += 1
# composites (quotedbl, accented letters...) would keep stale component offsets: flatten them first
for g in list(f.selection.byGlyphs):
    if g.references:
        g.unlinkRef()
f.autoWidth(int(em * 0.12), int(em * 0.02), int(em * 0.25))
for g in f.glyphs():
    if g.unicode in (0x20, 0xA0): g.width = int(em * 0.26)

# 3. Kerning: tighten only (AV, To, Te, Ty, P., F, ...)
LEFT  = "AFLPTVWYKRX"
RIGHT = "AJTVWYacdegmnopqrsuvwxyz"          # no i j l b h k f t (tall left edges)
nm = lambda ch: fontforge.nameFromUnicode(ord(ch))
left  = [nm(c) for c in LEFT  if nm(c) in f]
right = [nm(c) for c in RIGHT if nm(c) in f]
f.addLookup("kern-auto", "gpos_pair", None, (("kern", (("latn", ("dflt",)), ("DFLT", ("dflt",)))),))
f.addLookupSubtable("kern-auto", "kern-auto-1")
f.autoKern("kern-auto-1", int(em * 0.12), left, right, onlyCloser=True, minKern=int(em * 0.01))
# clamp: never pull a pair closer than 5% em
cap = -int(em * 0.05)
for gname in left:
    g = f[gname]
    pairs = [(ps[2], ps[5]) for ps in g.getPosSub("kern-auto-1")]
    if not pairs: continue
    g.removePosSub("kern-auto-1")
    for other, xadv in pairs:
        g.addPosSub("kern-auto-1", other, 0, 0, max(xadv, cap), 0, 0, 0, 0, 0)

# 4. Names
ribbi = weight in ("Regular", "Bold")
legacy_fam = FAM if ribbi else f"{FAM} {weight}"
legacy_sub = ("Bold " if weight == "Bold" else "") + ("Italic" if italic else ("" if weight == "Bold" else "Regular"))
legacy_sub = legacy_sub.strip() or "Regular"
psname = "CoveSans-" + style
keep = [e for e in f.sfnt_names if e[1] in ("Trademark", "Manufacturer", "Designer", "Vendor URL", "Designer URL") and e[0] == "English (US)"]
copyright_src = next((e[2] for e in f.sfnt_names if e[1] == "Copyright" and e[0] == "English (US)"), "")
keep += [("English (US)", "Copyright", (copyright_src + "\n" if copyright_src else "") + "Modifications Copyright 2026 The Gruvbox Cove contributors."),
         ("English (US)", "License", "Licensed under the SIL Open Font License, Version 1.1."),
         ("English (US)", "License URL", "https://openfontlicense.org")]
f.sfnt_names = tuple(keep)
f.familyname = legacy_fam
f.fontname = psname
f.fullname = f"{FAM} {pretty}"
for k, v in (("Family", legacy_fam), ("SubFamily", legacy_sub), ("Fullname", f"{FAM} {pretty}"),
             ("PostScriptName", psname), ("UniqueID", f"{psname};respaced from CaskaydiaCove Nerd Font"),
             ("Preferred Family", FAM), ("Preferred Styles", pretty),
             ("Descriptor", "Proportional re-spacing of CaskaydiaCove Nerd Font (Cascadia Code + Nerd Fonts), for long-form reading.")):
    f.appendSFNTName("English (US)", k, v)
f.os2_panose = tuple(list(f.os2_panose[:3]) + [0] + list(f.os2_panose[4:]))
for g in f.glyphs(): g.ttinstrs = b""
raw = os.path.join(outdir, psname + ".raw.ttf")
f.generate(raw, flags=("omit-instructions", "opentype"))
print(psname, "respaced", n)
