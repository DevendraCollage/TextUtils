# I Have Created This File - Devendra

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    text = request.POST.get('text', 'default')
    # Checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        # Analyze the text
        text = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        text = analyzed
    if newlineremove == "on":
        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        text = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(text):
            if text[index] == "" and text[index+1] == "":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
    if(removepunc != "on" and fullcaps != "on" and newlineremove != "on" and extraspaceremover != "on"):
        return HttpResponse("Please Select Any Operation and try again")
    return render(request, 'analyze.html', params)