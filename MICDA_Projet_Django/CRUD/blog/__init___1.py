from ProjectDjango.blog.forms import CrudForm


def __init__(self, *args, **kwargs):
	super(CrudForm,self).__init__(*args,**kwargs)
	self.fields['position'].empty_label = 'SELECT'
	super(CrudForm,self).__init__(*args,**kwargs)
	self.fields['position'].empty_label = 'SELECT'