from django.utils import translation

def current_language_middleware(get_response):

    def middleware(request):
        host = request.get_host().split('.')
        translation.activate(host[0])
        
        response = get_response(request)

        return response

    return middleware
