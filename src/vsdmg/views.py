from django.shortcuts import render

def home(request):
	context = {}
	template = "home.html"
	return render(request, template, context)

def testhome(request):
	context = {}
	template = "donotuse.html"
	return render(request, template, context)


# def home2(request):
# 	context = {}
# 	template = "home.html2"
# 	return render(request, template, context)