# test_pdf.py

from weasyprint import HTML

html = """
<h1>Hello Humaima</h1>
<p>Your WeasyPrint setup works!</p>
"""

HTML(string=html).write_pdf("test.pdf")

print("PDF generated successfully!")