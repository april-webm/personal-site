#!/usr/bin/env python3
"""
Build an anonymised resume PDF from April_Kidd_Resume.typ.
Strips the phone/email/contact line before compiling.
Output: april-webm.nekoweb.org/resume.pdf

Run this whenever you update the resume .typ file.
"""
import subprocess, sys, tempfile, pathlib

src = pathlib.Path("April_Kidd_Resume.typ")
out = pathlib.Path("april-webm.nekoweb.org/resume.pdf")

if not src.exists():
    print(f"Error: {src} not found", file=sys.stderr)
    sys.exit(1)

typ = src.read_text()

# Strip the contact info block (phone, email, linkedin, github) from the header.
# The block looks like:
#   #text(size: 10pt)[
#     +61 ... | email | linkedin | github
#   ]
lines = typ.splitlines()
out_lines = []
skip = False
for line in lines:
    if "#text(size: 10pt)[" in line and not skip:
        skip = True
        continue
    if skip:
        # look for the closing bracket on its own (dedented close of the block)
        stripped = line.strip()
        if stripped == "]":
            skip = False
        continue
    out_lines.append(line)
typ = "\n".join(out_lines)

with tempfile.NamedTemporaryFile(suffix=".typ", mode="w", delete=False) as tmp:
    tmp.write(typ)
    tmp_path = pathlib.Path(tmp.name)

try:
    result = subprocess.run(
        ["typst", "compile", str(tmp_path), str(out)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)
    print(f"Written: {out}")
finally:
    tmp_path.unlink(missing_ok=True)
