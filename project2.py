import wx
from wx import *

app = App()
root = Frame(None, title="form", size=(600,500))
panel = Panel(root)
panel.SetBackgroundColour("#C5E1A5")
mainbox = BoxSizer(VERTICAL)

font = Font(22,FONTFAMILY_DECORATIVE,FONTSTYLE_ITALIC,FONTWEIGHT_BOLD)
font2 = Font(16,FONTFAMILY_DECORATIVE,FONTSTYLE_ITALIC,FONTWEIGHT_NORMAL)

text = StaticText(panel, label="Admission", style=ALIGN_CENTER)
text.SetForegroundColour("#00695C")
text.SetFont(font)
mainbox.Add(text,0,EXPAND|ALL,border=20)
grid = GridSizer(6,2,10,10)

#text
name = StaticText(panel,label="Name")
contact = StaticText(panel,label="Contact")
email = StaticText(panel,label="Email")
address = StaticText(panel,label="Address")
dob = StaticText(panel,label="DOB")
name.SetFont(font2)
contact.SetFont(font2)
email.SetFont(font2)
address.SetFont(font2)
dob.SetFont(font2)
name.SetForegroundColour("#4E342E")
contact.SetForegroundColour("#4E342E")
email.SetForegroundColour("#4E342E")
dob.SetForegroundColour("#4E342E")
address.SetForegroundColour("#4E342E")

#text ctrl
name_ctrl = TextCtrl(panel)
contact_ctrl = TextCtrl(panel)
email_ctrl = TextCtrl(panel)
address_ctrl = TextCtrl(panel)
dob_ctrl = TextCtrl(panel)

#btn
send = Button(panel, label="Send")
send.SetBackgroundColour("#BA68C8")
send.SetForegroundColour("white")
clear = Button(panel, label="Clear")
clear.SetBackgroundColour("#607D8B")
clear.SetForegroundColour("white")

grid.AddMany([
    (name),(name_ctrl,0,EXPAND|ALL),
    (contact),(contact_ctrl,0,EXPAND|ALL),
    (email),(email_ctrl,0,EXPAND|ALL),
    (address),(address_ctrl,0,EXPAND|ALL),
    (dob),(dob_ctrl,0,EXPAND|ALL),
    (send,0,EXPAND|ALL),(clear,0,EXPAND|ALL)
])
mainbox.Add(grid,1,EXPAND|ALL,border=20)
panel.SetSizer(mainbox)

root.Show()
app.MainLoop()