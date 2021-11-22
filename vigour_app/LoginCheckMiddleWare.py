from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        print(modulename)
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "vigour_app.HodViews" or modulename == "vigour_api.views":
                    pass
                elif modulename == "vigour_app.views" or modulename == "django.views.static":
                    pass
                elif modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "vigour_app.DoctorViews" or modulename == "vigour_api.views":
                    pass
                elif modulename == "vigour_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("doctor_home"))
            elif user.user_type == "3":
                if modulename == "vigour_app.PatientViews" or modulename == "django.views.static":
                    pass
                elif modulename == "vigour_app.views" or modulename == "vigour_api.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("patient_home"))
            elif user.user_type == "4":
                if modulename == "vigour_app.HospitalViews" or modulename == "django.views.static" or modulename == "vigour_api.views":
                    pass
                elif modulename == "vigour_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("hospital_home"))
            else:
                return HttpResponseRedirect(reverse("show_login"))

        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login") or modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites" or modulename=="vigour_app.views" or modulename == "vigour_api.views" or modulename == "vigour_system.urls":
                pass
            else:
                pass
                # return HttpResponseRedirect(reverse("show_login"))