import wx
import time
import os

import ui.ids as IDS
import zw.homework as homework

class MainFrame(wx.Frame):
	def __init__(self, parent, wid, title
			, pos=wx.DefaultPosition, size=wx.DefaultSize
			, style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)):
		wx.Frame.__init__(self, parent, wid, title, pos, size, style)
		self.init_ui()
		self.load_data()
		self.bind_events()
	
	def init_ui(self):
		panel = wx.Panel(self, -1)
		
		box_calc = wx.StaticBox(panel, -1, '习题生成')
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer_sub = wx.BoxSizer(wx.HORIZONTAL)
		self.count = wx.SpinCtrl(box_calc, -1, min=1)
		sizer_sub.Add(wx.StaticText(box_calc, label='份数:'), 0, wx.TOP, 3)
		sizer_sub.Add(self.count, 1)
		sizer_sub.Add(wx.StaticText(box_calc, label='A4纸打印推荐3份'), 0, wx.TOP, 3)
		sizer.Add(sizer_sub, 0)

		sizer_sub = wx.BoxSizer(wx.HORIZONTAL)
		self.cb_range = wx.ComboBox(box_calc, choices=['10', '20', '30', '100'])
		self.cb_method = wx.ComboBox(box_calc, choices=['加减', '加减乘除'], style=wx.CB_READONLY)
		self.sc_number = wx.SpinCtrl(box_calc, -1, min=1)
		sizer_sub.Add(wx.StaticText(box_calc, label='计算题:'), 0, wx.TOP, 3)
		sizer_sub.Add(self.cb_range, 1)
		sizer_sub.Add(wx.StaticText(box_calc, label='以内'), 0, wx.TOP, 3)
		sizer_sub.Add(self.cb_method, 1)
		sizer_sub.Add(self.sc_number, 1)
		sizer_sub.Add(wx.StaticText(box_calc, label='题'), 0, wx.TOP, 3)
		sizer.Add(sizer_sub, 0, wx.EXPAND)

		sizer_sub = wx.BoxSizer(wx.HORIZONTAL)
		self.sc_blank_number = wx.SpinCtrl(box_calc, -1, min=1)
		sizer_sub.Add(wx.StaticText(box_calc, label='填空题:'), 0, wx.TOP, 3)
		sizer_sub.Add(self.sc_blank_number, 1)
		sizer_sub.Add(wx.StaticText(box_calc, label='题'), 0, wx.TOP, 3)
		sizer.Add(sizer_sub, 0)

		sizer_sub = wx.BoxSizer(wx.VERTICAL)
		self.ck_plain_sub = wx.CheckBox(box_calc, -1, '避免减法数字相等')
		self.ck_plain_mul = wx.CheckBox(box_calc, -1, '避免乘法含1相等')
		self.ck_plain_div = wx.CheckBox(box_calc, -1, '避免除数数字相等')
		sizer_sub.Add(self.ck_plain_sub, 1)
		sizer_sub.Add(self.ck_plain_mul, 1)
		sizer_sub.Add(self.ck_plain_div, 1)
		sizer.Add(sizer_sub, 0, wx.EXPAND)
		box_calc.SetSizer(sizer)


		btnsizer = wx.BoxSizer(wx.HORIZONTAL)
		btn = wx.Button(panel, IDS.ID_BTN_GEN, label='生成')
		btnsizer.Add(btn, 0, wx.BOTTOM, 10)
		btn = wx.Button(panel, wx.ID_CLOSE)
		btn.SetDefault()
		btnsizer.Add(btn, 0, wx.BOTTOM|wx.RIGHT, 10)

		bsizer = wx.BoxSizer(wx.VERTICAL)
		bsizer.Add(box_calc, 1, wx.EXPAND|wx.ALL)
		# bsizer.AddStretchSpacer(1)
		bsizer.Add(btnsizer, 0, wx.ALIGN_RIGHT)
		panel.SetSizer(bsizer)

	def load_data(self):
		self.count.SetValue(3)
		self.cb_range.SetValue('10')
		self.cb_method.SetValue('加减')
		self.sc_number.SetValue(20)
		self.sc_blank_number.SetValue(5)
		self.ck_plain_sub.SetValue(True)
		self.ck_plain_mul.SetValue(True)
		self.ck_plain_div.SetValue(True)

	def bind_events(self):
		self.Bind(wx.EVT_BUTTON, self.on_btn_gen_click, id=IDS.ID_BTN_GEN)
		self.Bind(wx.EVT_BUTTON, self.on_btn_close, id=wx.ID_CLOSE)
	
	def on_btn_gen_click(self, event):
		c = self.count.GetValue()
		r = int(self.cb_range.GetValue())
		m = self.cb_method.GetSelection()
		ms = self.cb_method.GetValue()
		v = self.sc_number.GetValue()
		bv = self.sc_blank_number.GetValue()
		ps = self.ck_plain_sub.GetValue()
		pm = self.ck_plain_mul.GetValue()
		pd = self.ck_plain_div.GetValue()

		filepath = 'result.txt'
		if os.path.exists(filepath):
			os.remove(filepath)

		ctn = []
		# ctn.append('习题：{0} 以内 {1} {2}题,出题时间:{3}\n'.format(
		# 	r, ms,v,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) )
		for i in range(c):
			calc = homework.gen_math_calc(r, m, v, ps, pm, pd)
			blank = homework.gen_math_blank(r, m, bv)
			ctn.extend(calc)
			ctn.extend(blank)
			ctn.append('----- {} -----'.format(i))

		max_col_per_page = 3
		max_line_per_page = 3
		col = 3
		page = 0
		lines = []
		for idx, line in enumerate(ctn):
			if col >= max_col_per_page:
				lines.extend(ctn[idx: max_line_per_page])
				col = 0
				page += 1
			else:
				m = idx%max_line_per_page
				lines[m*page] += '\t\t\t' + ctn[idx]
				col +=1

		with open(filepath, 'a', encoding='utf-8') as out:
			ls = [line+'\n' for line in ctn]
			out.writelines(ls)


	def on_btn_close(self, event):
		self.Destroy()