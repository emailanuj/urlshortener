from django.shortcuts import render,redirect
from .models import short_urls
from .forms import URLForm
from .shortener import shortener
# Create your views here.
def Home(request,token):
    print(request)
    long_url=short_urls.objects.filter(short_url=token)[0]
    print(long_url)
    return redirect(long_url.long_url)

def MakeURL(request):
    form=URLForm(request.POST or None)
    short_url=""
    base_url=""
    complete_url=""
    new_value=""
    error=""
    if request.method=='POST':
        if form.is_valid():
            NewURL=form.save(commit=False)
            new_value=request.POST.get('short_url')
            print('Short URL',new_value)
            base_url = 'http://'+request.get_host()+'/'
            if new_value:
                short_url=new_value
            else:
                short_url=shortener().issue_token()
            complete_url=base_url+short_url
            NewURL.short_url=short_url
            NewURL.save()
        else:
            form=URLForm()
            error="Invalid URL"
    return render(request,'home.html',{'form':form,'complete_url':complete_url,'short_url':short_url,'base_url':base_url,'error':error})