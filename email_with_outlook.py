import win32com.client as win32
import xlrd
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
receivers = ['shenwenlong66@outlook.com']
mail.To = receivers[0]
mail.Subject ='test1'
workbook = xlrd.open_workbook('E:\\kpi excel\\00_summary.xls')
mySheet = workbook.sheet_by_index(0)
 
nrows = mySheet.nrows
content = []
for i in range(nrows):
    ss = mySheet.row_values(i)
    content.append(ss)
    print(content)
    Truecontent =str(content)
 
mail.Body = Truecontent
mail.Attachments.Add('E:\\kpi excel\\00_summary.xls')
mail.Send()
