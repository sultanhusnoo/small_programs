from flask import session, redirect
from functools import wraps

def check_logged_in(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if 'logged_in' in session:
			return func(*args, **kwargs)
		return redirect('/')
		return "YOU SHALL NOT PASS!"
	return wrapper
