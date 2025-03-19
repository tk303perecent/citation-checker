from eyecite import get_citations

text = "In Roe v. Wade, 410 U.S. 113 (1973), the Supreme Court ruled on abortion rights."
citations = get_citations(text)

print("Extracted Citations:", citations)
