from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect


class AdminOnlyMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('home_app:home')
        else:
            return redirect(self.get_login_url())