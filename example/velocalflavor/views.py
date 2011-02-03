
from django.shortcuts import render_to_response
from forms import VELocalForm

def velocalform(request):
    """
    create or check example form 
    """
    if request.method == 'POST':
	form = VELocalForm(request.POST)
	if form.is_valid():
	    return render_to_response('formvalid.html','')
    else:
	form = VELocalForm()
		    	    
    return render_to_response('localform.html', {'form': form})
