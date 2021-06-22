# from django.shortcuts import render,HttpResponse
# from translate import Translator

# def HomeView(request):
# 	if request.method == "POST":
# 		text = request.POST["translate"]
# 		language = request.POST["language"]
# 		translator= Translator(to_lang=language)
# 		translation = translator.translate(text)
# 		return render(request,"index.html",{text: translation})
# 	return render(request,"index.html",{text: None})


from django.shortcuts import render,HttpResponse
from translate import Translator
# Create your views here.
  
def HomeView(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]
        translator= Translator(to_lang=language)
        translation = translator.translate(text)
        return render(request,"index.html",{"Text": translation})
    return render(request,"index.html",{"Text": None})