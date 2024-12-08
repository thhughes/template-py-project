import sys 
import os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.mock import Mockable
"""
	File to help with rapid prototyping of code in tests folder. 
	used to help development. 
"""

if __name__ == "__main__": 

	class Example(Mockable): 
		def str_method(self, *args, **kwargs): 
			return 'over 9000'
		def bool_method(self, *args, **kwargs): 
			return True 


	e = Example()
	assert e.bool_method(), 'Failed unmocked'
	e.bool_method.ignore_calls()
	assert e.bool_method(), 'Failed Default Return'
	e.check_mock_expectations()
	e.mock_reset()
	e.bool_method.expect_call(False)
	assert not e.bool_method(), 'Failed Single Call Test'
	e.bool_method.expect_n_calls(False, 2)
	assert not e.bool_method(), 'Failed 1st repeated call'
	assert not e.bool_method(), 'Failed repeated call'
	e.check_mock_expectations()
	e.mock_reset()
	e.bool_method.expect_call(True)
	assert not e.check_mock_expectations_safe(), 'Failed when calls are not made'
	print('Mock Example Above')
