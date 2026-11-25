import sys
s = sys.stdin.read()
# Fix quote characters that editors / Hebrew keyboards substitute for straight quotes
for ch in ["“", "”", "„", "‟", "״", "″", "＂", "«", "»"]:
    s = s.replace(ch, '"')
for ch in ["‘", "’", "‚", "‛", "׳", "′"]:
    s = s.replace(ch, "'")
# Remove invisible direction marks and non-breaking spaces
for ch in ["‎", "‏", "‪", "‫", "‬", "‭", "‮", "⁦", "⁧", "⁨", "⁩", "﻿"]:
    s = s.replace(ch, "")
s = s.replace(" ", " ")
sys.stdout.write(s)
