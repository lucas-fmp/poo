from datetime import datetime


def fmt_dta_br(dta):
   if isinstance(dta, datetime):
       return dta.strftime('%d/%m/%Y')
   return dta
