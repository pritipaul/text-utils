from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # param = {'name' : 'priti','address' : 'Rajarhat'}
    # return render(request,"index.html",param)
    # return HttpResponse("Homw page")
    return render(request, "index3.html")


def analysis(request):
     text = request.POST.get('textarea', 'default')
     # print(text)
     remove = request.POST.get('removepunc','default')
     # print(remove)
     caps = request.POST.get('fullcaps', 'default')
     # print(remove)
     newlineremove = request.POST.get('newlineremover', 'default')
     # print(newlineremove)
     spaceremove = request.POST.get('extraspaceremover', 'default')
     # print(newlineremove)
     charcount = request.POST.get('charcount', 'default')
     # print(charcount)
     if remove == 'on':
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analysis = ""
         for char in text:
             if char not in punctuations:
                 analysis = analysis + char
         params = {'purpose':'Remove all','analyzed_text':analysis}
         # return render(request,'analysis.html',params)
         text = analysis

     if(caps == 'on'):
         analysis = ""
         for char in text:
                 analysis = analysis + char.upper();
         params = {'purpose': 'Capital Wrod', 'analyzed_text': analysis}
         # return render(request, 'analysis.html', params)
         text = analysis

     if(newlineremove == 'on'):
         analysis = ""
         for char in text:
             if char != '\n' and char != '\r':
                analysis = analysis + char;
         params = {'purpose': 'Capital Wrod', 'analyzed_text': analysis}
         # return render(request, 'analysis.html', params)
         text = analysis


     if (spaceremove == 'on'):
         analysis = ""
         for index,char in enumerate(text):
             if text[index] == " " and text[index+1] == " ":
                 pass
             else:
                 analysis = analysis + char;
         params = {'purpose': 'Capital Wrod', 'analyzed_text': analysis}
         # return render(request, 'analysis.html', params)
         text = analysis

     if (charcount == 'on'):
         analysis = "No of charecter is : " +  str(len(text));
         params = {'purpose': 'Capital Wrod', 'analyzed_text': analysis}
         # return render(request, 'analysis.html', params)
         text = analysis

     if(remove != 'on' and caps != 'on' and newlineremove != 'on' and spaceremove != 'on' and charcount != 'on' ):
         return HttpResponse('''
         <div class="alert alert-info alert-dismissible fade show" role="alert">
            <strong>ERROR ! </strong> please select any operation and try again.
         </div>
      ''')
     # else:
     #     return HttpResponse("Error ! Please Check the check box")

     return render(request, 'analysis.html', params)




#......................................... Tutorial - 1 Part .......................................................#

# def index(request):
#    return HttpResponse('''<h1>Priti</h1> <a href="https://www.w3schools.com">Visit W3Schools.com!</a> <a herf = "https://www.geeksforgeeks.org/object-oriented-analysis-and-design/">First link</a>  <a herf = "https://www.geeksforgeeks.org/object-oriented-analysis-and-design/"> second link </a>''')

# def about(request):
#     return HttpResponse("Hello I am priti paul")



# def removepunc(reqest):
#     # print(reqest.GET.get('textarea','default'))
#     text = reqest.GET.get('textarea','default')
#     return HttpResponse("Remove Punctuation")
#
# def capitalization(reqest):
#     return HttpResponse("Capitalization")
#
#
# def newlineremover(reqest):
#     return HttpResponse("New line Remover")
#
# def charcount(reqest):
#     return HttpResponse("Remove char count")
#
# def spaceremover(reqest):
#     return HttpResponse('''Remove Space <a href="/">Back</a>''')


