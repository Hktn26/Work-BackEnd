from django.http import HttpResponse


def fscohort(request):
    return HttpResponse('''
        <h2>
            Welcome to the FSCOHORT!
        </h2>
    ''')

def goodbye(request):
    return HttpResponse('Goodbye, World!')
