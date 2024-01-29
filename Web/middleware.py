import requests
from django.shortcuts import redirect

class GeoLocationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip middleware for certain URLs to prevent infinite loops
        if request.path_info.startswith('/in/'):
            return self.get_response(request)

        response = self.get_response(request)

        # Get user's IP address
        ip = self.get_client_ip(request)

        # Query IP geolocation service
        country = self.get_country_from_ip(ip)

        # Redirect based on country
        if country == 'IN':
            return redirect('/in/')
        else:
            # Handle other countries or default behavior
            return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_country_from_ip(self, ip):
        # Use an IP geolocation service
        # Replace 'YOUR_API_KEY' with an actual API key if needed
        api_key = 'c5e942071819aa'
        url = f'http://ipinfo.io/{ip}/json?token={api_key}'
        response = requests.get(url)
        data = response.json()
        country = data.get('country', '')
        return country
