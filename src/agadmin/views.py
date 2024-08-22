from django.http  import HttpResponse
from django.shortcuts import render


from visits.models import pageVisit

def home(request, *args, **kwargs):
    pageVisit.objects.create(path=request.path)
    
    path =  request.path
    qs    = pageVisit.objects.all()
    page_qs    = pageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "querySet": page_qs.count,
        "total": qs.count,
        "percent": (page_qs.count() * 100.0) / qs.count() ,
        
    }
    html_template = "home.html"
    return render(request,html_template,my_context)

def about(request, *args, **kwargs):
    pageVisit.objects.create(path=request.path)
    
    # path =  request.path
    qs    = pageVisit.objects.all()
    page_qs    = pageVisit.objects.filter(path=request.path)

    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0
    
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "querySet": page_qs.count,
        "total": qs.count,
        "percent": percent ,
        
    }
    html_template = "home.html"
    return render(request,html_template,my_context)

def old_home(request, *args, **kwargs):
  
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_ = """
    <!DOCTYPE html>
<html>

<body>
    <h1>{page_title} anything?</h1>
</body>
</html>    
""".format(**my_context) # page_title=my_title
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)
