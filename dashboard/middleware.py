from django.shortcuts import redirect

class RedirectToDomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host != 'fmartns.dev':
            # Redireciona para o domínio principal
            return redirect(f"https://fmartns.dev{request.get_full_path()}")
        response = self.get_response(request)
        return response
