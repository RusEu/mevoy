from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView, View
from django.http import JsonResponse

from vacation_request.models import Request
from company.models import Department

from .models import Calendar


BACKGROUND_COLORS = [
    {
        "name": "black",
        "class": "bg-black",
        "background-color": "#111111",
    },
    {
        "name": "yellow",
        "class": "bg-yellow",
        "background-color": "#f39c12",
    },
    {
        "name": "aqua",
        "class": "bg-aqua",
        "background-color": "#00c0ef"
    },
    {
        "name": "red",
        "class": "bg-red",
        "background-color": "#dd4b9",
    },
    {
        "name": "blue",
        "class": "bg-blue",
        "background-color": "#0073b7"
    },
    {
        "name": "light-blue",
        "class": "bg-light-blue",
        "background-color": "#3c8dbc"
    },
    {
        "name": "green",
        "class": "bg-green",
        "background-color": "#00a65a"
    },
    {
        "name": "navy",
        "class": "bg-navy",
        "background-color": "#001f3f",
    },
    {
        "name": "teal",
        "class": "bg-teal",
        "background-color": "#39cccc",
    },
    {
        "name": "olive",
        "class": "bg-olive",
        "background-color": "#3d9970",
    },
    {
        "name": "lime",
        "class": "bg-lime",
        "background-color": "#01ff70",
    },
    {
        "name": "orange",
        "class": "bg-orange",
        "background-color": "#ff851b",
    },
    {
        "name": "fuchsia",
        "class": "bg-fuchsia",
        "background-color": "#f012be",
    },
    {
        "name": "purple",
        "class": "bg-purple",
        "background-color": "#605ca8",
    },
    {
        "name": "maroon",
        "class": "bg-maroon",
        "background-color": "#d81b60",
    }
]


class CalendarPageView(TemplateView):

    template_name = "calendar/index.html"

    def get_context_data(self, **kwargs):
        context = super(CalendarPageView, self).get_context_data(**kwargs)
        context["request_type"] = kwargs.get("request_type")
        return context


class CalendarApiView(View):
    @method_decorator(login_required)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CalendarApiView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        users = []
        events = []
        department = Department.objects.get(
            name=self.request.session['department'])
        request_type = request.POST['request_type']

        for index, user in enumerate(department.employees.all()):
            user_color = BACKGROUND_COLORS[index]
            users.append({
                "name": user.get_full_name(),
                "color_class": user_color["class"]
            })
            user_requests = Request.objects.filter(
                user=user,
                status=Request.APPROVED,
                department=department,
                request_type=request_type
            )
            for user_request in user_requests:
                events.append({
                    "title": user_request.description[:20],
                    "start": user_request.start_date,
                    "end": user_request.end_date,
                    "backgroundColor": user_color["background-color"]
                })

        data = {
            "users": users,
            "events": events
        }
        return JsonResponse(data)
