from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from services.EolympRequests import Cout , DiffWithSelectedProfiles



def index(request):    
    return render(request,"EUD/index.html")

def about(request):    
    return render(request,"EUD/about.html")

def analysis(request):    
    return render(request,"EUD/analysis.html")

@csrf_exempt
def eliminate(request):
    superlist = ['beta64','ashurbay',"a.a.r"]

    if request.method == 'POST':
        core_input = request.POST.get('coreInput')
        target_input = request.POST.get('targetInput')
        print(f"Core: {core_input} Target: {target_input}")
        if target_input.lower() in superlist:
            return render(request, 'EUD/index.html', {'notification_message': f"You do not have permission to look at the differences with the user selected as target ({target_input})"})

        
        links = [{'url': link, 'index' : link[35:] } for link in Cout(DiffWithSelectedProfiles(core_input,target_input))]
        return render(request, 'EUD/index.html', {'links': links,'notification_message': f"Core: {core_input} Target: {target_input}",})
    return render(request, 'EUD/index.html')


