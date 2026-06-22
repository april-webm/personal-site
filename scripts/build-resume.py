#!/usr/bin/env python3
"""
Build an anonymised resume PDF from April_Kidd_Resume.typ.
Strips the phone/email/contact line before compiling.
Output: april-webm.nekoweb.org/resume.pdf

Run this whenever you update the resume .typ file.
"""
import subprocess, sys, tempfile, pathlib

src = pathlib.Path.home() / "Documents/repos/resume/April_Kidd_Resume.typ"
out = pathlib.Path(__file__).parent.parent / "april-webm.nekoweb.org/resume.pdf"

if not src.exists():
    print(f"Error: {src} not found", file=sys.stderr)
    sys.exit(1)

typ = src.read_text()

# Strip the contact info block between CONTACT-START and CONTACT-END markers.
lines = typ.splitlines()
out_lines = []
skip = False
for line in lines:
    if "// CONTACT-START" in line:
        skip = True
        continue
    if "// CONTACT-END" in line:
        skip = False
        continue
    if not skip:
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
