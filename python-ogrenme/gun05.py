from pypdf import PdfReader
reader = PdfReader("test.pdf")
print("Sayfa sayisi:", len(reader.pages))

ilk_sayfa= reader.pages[0]
metin = ilk_sayfa.extract_text()


print("--- ILK SAYFA ---")
print(metin)