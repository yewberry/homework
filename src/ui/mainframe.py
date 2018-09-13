import wx
import time

import ui.ids as IDS
import zw.homework as homework

class MainFrame(wx.Frame):
	def __init__(self, parent, wid, title
			, pos=wx.DefaultPosition, size=wx.DefaultSize
			, style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)):
		wx.Frame.__init__(self, parent, wid, title, pos, size, style)
		self.init_ui()
		self.bind_events()
	
	def init_ui(self):
		panel = wx.Panel(self, -1)
		sizer = wx.BoxSizer(wx.HORIZONTAL)

		self.cb_range = wx.ComboBox(panel, choices=['10', '20', '30', '100'])
		self.cb_range.SetValue('10')
		self.cb_method = wx.ComboBox(panel, choices=['加减', '加减乘除'], style=wx.CB_READONLY)
		self.cb_method.SetValue('加减')
		self.sc_number = wx.SpinCtrl(panel, -1, min=1, initial=20)
		sizer.Add(self.cb_range, 0, wx.LEFT, 5)
		sizer.Add(wx.StaticText(panel, label='以内'), 0, wx.TOP, 4)
		sizer.Add(self.cb_method, 0)
		sizer.Add(self.sc_number, 0)
		sizer.Add(wx.StaticText(panel, label='题'), 0, wx.TOP, 4)

		btnsizer = wx.BoxSizer(wx.HORIZONTAL)
		btn = wx.Button(panel, IDS.ID_BTN_GEN, label='生成')
		btnsizer.Add(btn, 0, wx.BOTTOM, 10)
		btn = wx.Button(panel, wx.ID_CLOSE)
		btn.SetDefault()
		btnsizer.Add(btn, 0, wx.BOTTOM|wx.RIGHT, 10)

		bsizer = wx.BoxSizer(wx.VERTICAL)
		bsizer.Add(sizer, 0)
		bsizer.AddStretchSpacer(1)
		bsizer.Add(btnsizer, 0, wx.ALIGN_RIGHT)
		panel.SetSizer(bsizer)

	def bind_events(self):
		self.Bind(wx.EVT_BUTTON, self.on_btn_gen_click, id=IDS.ID_BTN_GEN)
		self.Bind(wx.EVT_BUTTON, self.on_btn_close, id=wx.ID_CLOSE)
	
	def on_btn_gen_click(self, event):
		r = int(self.cb_range.GetValue())
		m = self.cb_method.GetSelection()
		ms = self.cb_method.GetValue()
		v = self.sc_number.GetValue()
		ctn = homework.gen_math_calc(r, m, v)
		print('{0} 以内 {1} {2}题,出题时间:{3}'.format(r, ms,v,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) )

	def on_btn_close(self, event):
		self.Destroy()