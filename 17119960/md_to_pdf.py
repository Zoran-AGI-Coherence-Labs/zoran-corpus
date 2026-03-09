# Standalone Markdown->PDF (text-only) converter
import sys, os, textwrap

def md_to_plaintext(md):
    lines = md.splitlines()
    out = []
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append("")
            continue
        if in_code:
            out.append(line)
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            text = line.lstrip("#").strip().upper()
            out.append(text)
            out.append("-"*min(80, max(20, len(text))))
            continue
        if line.strip().startswith(("- ", "* ")):
            out.append("• " + line.strip()[2:])
            continue
        line = line.replace("**", "").replace("*", "")
        out.append(line)
    return "\n".join(out)

def make_minimal_pdf(text, pdf_path):
    import textwrap
    lines = text.split("\n")
    page_width = 595
    page_height = 842
    left = 50
    top = 800
    line_height = 12
    max_lines_per_page = int((top - 50) / line_height)
    pages = []
    current_lines = []
    for line in lines:
        for part in textwrap.wrap(line, width=95):
            current_lines.append(part)
            if len(current_lines) >= max_lines_per_page:
                pages.append(current_lines); current_lines = []
    if current_lines:
        pages.append(current_lines)

    header = "%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    objects = []
    xref = []
    def add(obj):
        pos = sum(len(o) for o in objects)
        xref.append(pos); objects.append(obj)

    add("1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    kids = []
    for i in range(len(pages)):
        kids.append(f"{3+i*2} 0 R")
    add(f"2 0 obj\n<< /Type /Pages /Kids [{' '.join(kids)}] /Count {len(pages)} >>\nendobj\n")
    for i, page in enumerate(pages):
        content_parts = []
        y = top
        for line in page:
            t = line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
            content_parts.append(f"BT 50 {y} Td ({t}) Tj ET"); y -= line_height
        content_data = "\n".join(content_parts)
        content_len = len(content_data.encode('latin1', 'ignore'))
        content_num = 4 + i*2
        add(f"{content_num} 0 obj\n<< /Length {content_len} >>\nstream\n{content_data}\nendstream\nendobj\n")
        page_num = 3 + i*2
        add(f"{page_num} 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> >> >> /Contents {content_num} 0 R >>\nendobj\n")

    body = "".join(objects)
    xref_pos = len(header) + len(body)
    xref_table = f"xref\n0 {len(objects)+1}\n0000000000 65535 f \n"
    offset = 0
    for pos in xref:
        xref_table += "{:010d} 00000 n \n".format(len(header)+offset)
        offset += len(objects[xref.index(pos)])
    trailer = f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF"
    with open(pdf_path, "wb") as f:
        f.write(header.encode('latin1')); f.write(body.encode('latin1'))
        f.write(xref_table.encode('latin1')); f.write(trailer.encode('latin1'))

def main():
    if len(sys.argv) < 3:
        print("Usage: md_to_pdf.py <input.md> <output.pdf>"); sys.exit(1)
    md_path, pdf_path = sys.argv[1], sys.argv[2]
    with open(md_path, "r", encoding="utf-8") as f:
        md = f.read()
    text = md_to_plaintext(md)
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
        page_width, page_height = A4
        c = canvas.Canvas(pdf_path, pagesize=A4)
        left_margin = 20*mm; right_margin = 20*mm; top_margin = 20*mm; bottom_margin = 20*mm
        width = page_width - left_margin - right_margin
        y = page_height - top_margin
        line_height = 12
        for paragraph in text.split("\n"):
            wrapped = textwrap.wrap(paragraph, width=int(width/6))
            if not wrapped: wrapped = [""]
            for w in wrapped:
                if y < bottom_margin + line_height:
                    c.showPage(); y = page_height - top_margin
                c.setFont("Helvetica", 10); c.drawString(left_margin, y, w); y -= line_height
        c.save()
    except Exception:
        make_minimal_pdf(text, pdf_path)

if __name__ == "__main__":
    main()
