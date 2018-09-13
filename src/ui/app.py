import os
import wx

import zw.logger as logger
from zw.utils import Timeit
from zw.config import Config
from ui.mainframe import MainFrame

# set _ function in builtins for i18n
import builtins
builtins.__dict__['_'] = wx.GetTranslation

LOG = logger.getLogger(__name__)
class App(wx.App):
	cfg_path = property(lambda s: s._cfg_path, lambda s, v: setattr(s, '_cfg_path', v))

	def OnInit(self):
		t = Timeit()
		LOG.debug("OnInit")

		# load locale from cur dir in locale
		# TODO mac, place locale in app
		locale = wx.Locale(wx.LANGUAGE_CHINESE_SIMPLIFIED)
		if locale.IsOk():
			locale.AddCatalogLookupPathPrefix('locale')
			locale.AddCatalog('app')

		self.cfg_path = 'cfg.json'
		# init config file
		cfg = Config(self.cfg_path, {
			'version': '1.0.0',
			'range': 10
		}).data

		frm = MainFrame(None, -1, _('小学数学习题工具'), size=(400, 300))
		frm.Show()
	
		LOG.debug('Elapsed time: %f ms' % t.end())
		return True

	def OnExit(self):
		# exit but main process still there why?
		wx.Exit()




