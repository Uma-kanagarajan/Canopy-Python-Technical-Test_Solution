import pdftables_api
import glob

for filename in glob.glob('*.pdf'):
    excel_filename = filename.replace('.pdf','')
    excel_convert = pdftables_api.Client('8nehrotcon8b') #if needed use your API key
    excel_convert.xlsx(filename, excel_filename)





#c = pdftables_api.Client('8nehrotcon8b')
#c.xlsx('Bos.pdf', 'Bos_excel') #replace c.xlsx with c.csv to convert to CSV
