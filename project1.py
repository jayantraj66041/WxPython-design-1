import wx
from wx import *

app = App()
root = Frame(None, title="PIP Infotech Pvt. Ltd.", size=(600,400))
root.Centre()
panel = Panel(root)
panel.SetBackgroundColour("#C5E1A5")
mainbox = BoxSizer(VERTICAL)

display = TextCtrl(panel)
mainbox.Add(display,0,ALL|EXPAND,border=10)

btnlist = ['oil','teddy','marker','book','copy','pen','laptop','mobile','pendrive','cardreader','rice','curd','pencil','rubber','cutter']
btngrid = GridSizer(3,5,10,10)
for i in btnlist:
    btn = Button(panel,label=i)
    btn.SetBackgroundColour("#CE93D8")
    btn.SetForegroundColour("white")
    btngrid.Add(btn,1,EXPAND|ALL)

mainbox.Add(btngrid,1,ALL|EXPAND,border=10)
panel.SetSizer(mainbox)
root.Show()
app.MainLoop()