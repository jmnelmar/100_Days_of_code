# Steps to install
#pip install -U \-f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04 \clearwxPython

# Steps to build
#https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html

#!/usr/bin/python

import wx

def onButton(event):
    print("Button pressed.")

app = wx.App()
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,200,200)

panel = wx.Panel(frame, wx.ID_ANY)
button = wx.Button(panel, wx.ID_ANY, 'Test', (10, 10))
button.Bind(wx.EVT_BUTTON, onButton)

frame.Show()
frame.Center()
app.MainLoop()