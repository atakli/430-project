#function of "voicingDetector_magnitude_sum_function__hamza"
from scipy import signal
def func_vd_msf(y):
	B,A = signal.butter(9,.33,'low')  %.5 or .33?	# heralde doğrudur hızlı kontrol ettim	
	y1 = signal.filtfilt(B,A,y)						# matlabdaki filter python'da lfilter mi filtfilt mi
	m_s_f = sum( abs(y1) )							# kontrol etmek lazım bazı şeyleri, mesela abs'ın sonucu 0.999999 geliyo
	return m_s_f									# bazı indexler için, bu bi sorun mu, matlabda da aynı mı



#  (msf>((.5).*(sum(msf)./length(msf))))

#  if s>13
#      msf=1;
#  else
#      msf=0;
#  end
#  
