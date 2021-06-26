from .models import *
def website_details(request):
    main_details=main_footer.objects.last()
    return {'details':main_details}