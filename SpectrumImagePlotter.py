import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import SpanSelector
import SpectrumPlotter

class SpectrumImagePlotter(object):
	def __init__(self, SI):
		self.SI = SI
		self.fig = plt.figure(figsize = (9,9))
		self.image_ax = plt.axes([0.075, 0.6, 0.45, 0.35])
		self.extracted_ax = plt.axes([0.525, 0.6, 0.45, 0.35])
		self.spectrum_ax = plt.axes([0.075, 0.07, 0.9, 0.4])
		self.contrast_ax = plt.axes([0.075, 0.47, 0.9, 0.1])
		
		# Spectrum axis plotting and interactive span
		self.SpectrumPlot = SpectrumPlotter.SpectrumPlotter(self.spectrum_ax, 
			self.SI.data[0,0,:], self.SI.data[1,1,:])
		self.E_span = SpanSelector(self.spectrum_ax, self.Espan, 'horizontal', 
			span_stays = True)
		self.Emin_i = 0
		self.Emax_i = 0
		
	def Espan(self, Emin, Emax): ##Note: draws sub-pixel Espan, fix?
		Emin = np.round(Emin/self.SI.dispersion) * self.SI.dispersion
		Emax = np.round(Emax/self.SI.dispersion) * self.SI.dispersion
		self.Emin_i = np.where(self.SpectrumPlot.x == Emin)
		self.Emax_i = np.where(self.SpectrumPlot.x == Emax)
		print Emin, Emax, self.Emin_i, self.Emax_i
