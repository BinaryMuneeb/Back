from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'index.html')
def anaylaze(request):
    # get the text
    djtext=request.POST.get('text','default')

    removepunc=request.POST.get('removepunc','off')
    full_capitlize = request.POST.get('full_capitlize', 'off')
    new_liner_remover=request.POST.get('new_liner_remover','off')
    space_remover = request.POST.get('space_remover', 'off')
    print(removepunc)
    # ?anyalze the text
    print(djtext)
    if removepunc=="on":
        anaylazed=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                anaylazed=anaylazed+char

        params={'purpose':'Removed punctuation','analyzer':anaylazed}
        djtext=anaylazed

    if(full_capitlize=="on"):
        anaylazed=""
        for char in djtext:
            anaylazed=anaylazed+char.upper()
        params = {'purpose': 'CAPITLEZE FIRST', 'analyzer': anaylazed}
        djtext=anaylazed

    if(new_liner_remover=="on"):
        anaylazed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                anaylazed=anaylazed+char
            else:
                print("no")
        print("pre",anaylazed)
        params = {'purpose': 'new_line remover', 'analyzer': anaylazed}
        djtext=anaylazed

    if(removepunc!="on" and full_capitlize!="on" and space_remover!="on" and new_liner_remover!="on"):
        return HttpResponse("error")


    return render(request, 'anaylze.html', params)