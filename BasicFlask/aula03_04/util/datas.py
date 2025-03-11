from datetime import datetime


# Pega uma data em formato HTML "YYYY-MM-DD" e transforma em data do Python para cálculos e afins.
def html_to_python(dta_html):
   dta_python = datetime.strptime(dta_html, "%Y-%m-%d")
   return dta_python