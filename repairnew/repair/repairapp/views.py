from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone


# Helper function to check if user is admin
# def is_admin(user):
#     return user.is_superuser

# Home/Index Page
# def index(request):
#     return render(request, 'index.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get("remember")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:   # Allow only superusers
                login(request, user)

                # Remember me functionality
                if remember:
                    request.session.set_expiry(1209600)  # 2 weeks
                else:
                    request.session.set_expiry(0)  # Browser close

                messages.success(request, "Login successful!")
                return redirect("admin_dashboard")
            else:
                messages.error(request, "You are not authorized as admin.")
                return redirect("admin_login")
        else:
            messages.error(request, "Invalid username or password!")
            return redirect("admin_login")

    return render(request, "adminlogin.html")
# @login_required
# def userhome(request):
#     return render(request, "userhome.html")
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RepairRequest, UserProfile
from django.db.models import Count
from datetime import datetime, timedelta
from django.utils import timezone

@login_required
def userhome(request):
    # Get the current logged-in user
    user = request.user
    
    # Get user's repair requests
    user_repairs = RepairRequest.objects.filter(user=user).order_by('-created_at')
    
    # Calculate statistics
    total_repairs = user_repairs.count()
    pending_repairs = user_repairs.filter(status='pending').count()
    in_progress_repairs = user_repairs.filter(status='in_progress').count()
    completed_repairs = user_repairs.filter(status='completed').count()
    
    # Get recent repairs (last 5)
    recent_repairs = user_repairs[:5]
    
    # Get user profile if exists
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None
    
    # Get repair statistics for the last 30 days
    last_30_days = timezone.now() - timedelta(days=30)
    recent_repairs_count = user_repairs.filter(created_at__gte=last_30_days).count()
    
    # Prepare context
    context = {
        'user': user,
        'user_profile': user_profile,
        
        # Statistics
        'total_repairs': total_repairs,
        'pending_repairs': pending_repairs,
        'in_progress_repairs': in_progress_repairs,
        'completed_repairs': completed_repairs,
        'recent_repairs_count': recent_repairs_count,
        
        # Recent repairs for table
        'recent_repairs': recent_repairs,
        
        # For display
        'current_date': timezone.now().strftime('%B %d, %Y'),
        'current_time': timezone.now().strftime('%I:%M %p'),
    }
    
    return render(request, 'userhome.html', context)



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login_view(request):
    """User login view for regular users"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if not user.is_superuser:  # Regular user only
                login(request, user)  # Log the user in
                messages.success(request, f'Welcome, {user.first_name}!')
                return redirect('userhome')  # Redirect to user home/dashboard
            else:
                messages.error(request, 'Please use admin login for admin accounts.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request,'userlogin.html')


def user_register_view(request):
    if request.method == 'POST':
        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        email = request.POST.get("email")
        pwd = request.POST.get("password")

        user = User.objects.create(
            username = email,      # Or generate username
            first_name = first,
            last_name = last,
            email = email
        )
        user.set_password(pwd)
        user.save()

        messages.success(request, "Account created! You can login now.")
        return redirect("user_login")



# def submit_repair_request(request):
#     if request.method == "POST":

#         device_type = request.POST.get('device_type')
#         device_brand = request.POST.get('device_brand')
#         device_model = request.POST.get('device_model')
#         problem_description = request.POST.get('problem_description')

#         # Save only fields that exist in your model
#         RepairRequest.objects.create(
#             user=request.user,
#             device_type=device_type,
#             device_brand=device_brand,
#             device_model=device_model,
#             problem_description=problem_description,
#         )

#         messages.success(request, "Your repair request has been submitted successfully!")
#         return redirect('submit_repair_request')

#     return render(request, 'repair_request.html')

def submit_repair_request(request):
    if request.method == 'POST':
        RepairRequest.objects.create(
            user=request.user,
            device_type=request.POST.get('device_type'),
            device_brand=request.POST.get('device_brand'),
            device_model=request.POST.get('device_model'),
            serial_number=request.POST.get('serial_number'),
            purchase_date=request.POST.get('purchase_date') or None,

            problem_description=request.POST.get('problem_description'),
            problem_hardware=bool(request.POST.get('problem_hardware')),
            problem_software=bool(request.POST.get('problem_software')),
            problem_virus=bool(request.POST.get('problem_virus')),
            problem_screen=bool(request.POST.get('problem_screen')),
            problem_battery=bool(request.POST.get('problem_battery')),
            problem_keyboard=bool(request.POST.get('problem_keyboard')),
            problem_internet=bool(request.POST.get('problem_internet')),
            problem_sound=bool(request.POST.get('problem_sound')),
            problem_other=bool(request.POST.get('problem_other')),

            problem_start_date=request.POST.get('problem_start_date') or None,
            problem_frequency=request.POST.get('problem_frequency'),

            attempted_solutions=request.POST.get('attempted_solutions'),
            urgency_level=request.POST.get('urgency_level'),

            service_type=request.POST.get('service_type'),
            contact_method=request.POST.get('contact_method'),
            estimated_budget=request.POST.get('estimated_budget') or None,

            data_backup=bool(request.POST.get('data_backup')),
            diagnostic_only=bool(request.POST.get('diagnostic_only')),
        )

        messages.success(request, "Your repair request has been submitted!")
        return redirect('userhome')

    # -------------------------
    # Handle GET request here
    # -------------------------
    return render(request, 'repair_request.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import RepairRequest

@login_required
def my_requests_view(request):
    # Fetch only the logged-in user's repair requests
    my_requests = RepairRequest.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'my_requests': my_requests
    }
    return render(request, 'userrequest_view.html', context)

def user_logout(request):
    # logout(request)
    messages.success(request, "Logged out successfully.")
    return render(request, "index.html")

# @login_required
# def admin_dashboard(request):
#     return render(request, "admin_dashboard.html")
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import RepairRequest, UserProfile
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Q

@login_required
def admin_dashboard(request):
    # Get current user and ensure admin access
    if not request.user.is_superuser and not request.user.is_staff:
        # Redirect non-admin users
        return redirect('home')
    
    # Get current time
    now = timezone.now()
    one_month_ago = now - timedelta(days=30)
    one_week_ago = now - timedelta(days=7)
    
    # 1. User Statistics
    total_users = User.objects.count()
    new_users_month = User.objects.filter(date_joined__gte=one_month_ago).count()
    new_users_week = User.objects.filter(date_joined__gte=one_week_ago).count()
    
    # 2. Repair Request Statistics
    total_repairs = RepairRequest.objects.count()
    pending_repairs = RepairRequest.objects.filter(status='pending').count()
    in_progress_repairs = RepairRequest.objects.filter(status='in_progress').count()
    completed_repairs = RepairRequest.objects.filter(status='completed').count()
    cancelled_repairs = RepairRequest.objects.filter(status='cancelled').count()
    
    # 3. Monthly statistics for charts
    monthly_repairs = []
    for i in range(6):  # Last 6 months
        month_start = now - timedelta(days=30 * (i + 1))
        month_end = now - timedelta(days=30 * i)
        
        count = RepairRequest.objects.filter(
            created_at__gte=month_start,
            created_at__lt=month_end
        ).count()
        
        month_name = month_start.strftime('%b')
        monthly_repairs.append({
            'month': month_name,
            'count': count
        })
    
    monthly_repairs.reverse()  # Order from oldest to newest
    
    # 4. Status distribution for chart
    status_distribution = {
        'pending': pending_repairs,
        'in_progress': in_progress_repairs,
        'completed': completed_repairs,
        'cancelled': cancelled_repairs
    }
    
    # 5. Recent repairs (last 10)
    recent_repairs = RepairRequest.objects.select_related('user').order_by('-created_at')[:10]
    
    # 6. Recent users (last 10)
    recent_users = User.objects.order_by('-date_joined')[:10]
    
    # 7. Device type statistics
    device_types = RepairRequest.objects.values('device_type').annotate(
        count=Count('id')
    ).order_by('-count')[:5]
    
    # 8. Urgency statistics
    urgency_stats = RepairRequest.objects.values('urgency_level').annotate(
        count=Count('id')
    ).exclude(urgency_level__isnull=True).exclude(urgency_level='')
    
    # 9. Problem type statistics
    problem_counts = {
        'hardware': RepairRequest.objects.filter(problem_hardware=True).count(),
        'software': RepairRequest.objects.filter(problem_software=True).count(),
        'virus': RepairRequest.objects.filter(problem_virus=True).count(),
        'screen': RepairRequest.objects.filter(problem_screen=True).count(),
        'battery': RepairRequest.objects.filter(problem_battery=True).count(),
        'keyboard': RepairRequest.objects.filter(problem_keyboard=True).count(),
        'internet': RepairRequest.objects.filter(problem_internet=True).count(),
        'sound': RepairRequest.objects.filter(problem_sound=True).count(),
        'other': RepairRequest.objects.filter(problem_other=True).count()
    }
    
    # 10. Top users with most repairs
    top_users = User.objects.annotate(
        repair_count=Count('repairrequest')
    ).order_by('-repair_count')[:5]
    
    context = {
        # User stats
        'total_users': total_users,
        'new_users_month': new_users_month,
        'new_users_week': new_users_week,
        
        # Repair stats
        'total_repairs': total_repairs,
        'pending_repairs': pending_repairs,
        'in_progress_repairs': in_progress_repairs,
        'completed_repairs': completed_repairs,
        'cancelled_repairs': cancelled_repairs,
        
        # Chart data
        'monthly_repairs': monthly_repairs,
        'status_distribution': status_distribution,
        
        # Recent data
        'recent_repairs': recent_repairs,
        'recent_users': recent_users,
        
        # Detailed statistics
        'device_types': device_types,
        'urgency_stats': urgency_stats,
        'problem_counts': problem_counts,
        'top_users': top_users,
        
        # For templates
        'now': now,
        'one_month_ago': one_month_ago,
        'one_week_ago': one_week_ago,
    }
    
    return render(request, "admin_dashboard.html", context)
# User Login
# def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # First check if user exists with this email
            user = User.objects.get(email=email)
            # Authenticate with username and password
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None and not user.is_superuser:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('user_dashboard')
            else:
                messages.error(request, 'Invalid credentials!')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist!')
    
    return render(request, 'user_login.html')

# User Registration
# def user_register(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validation checks
        errors = []
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            errors.append('Email already registered!')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            errors.append('Username already taken!')
        
        # Password validation
        if password != confirm_password:
            errors.append('Passwords do not match!')
        
        if len(password) < 8:
            errors.append('Password must be at least 8 characters long!')
        
        # Phone validation (simple check)
        if not re.match(r'^[0-9]{10}$', phone.replace(' ', '')):
            errors.append('Please enter a valid 10-digit phone number!')
        
        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            try:
                # Create User
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                
                # Create Customer profile
                customer = Customer.objects.create(
                    user=user,
                    phone=phone,
                    address=address
                )
                
                messages.success(request, 'Registration successful! Please login.')
                return redirect('user_login')
                
            except Exception as e:
                messages.error(request, f'Error during registration: {str(e)}')
    
    return render(request, 'user_register.html')

def add_user(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "error", "message": "Username already exists"})

        # Create Django User
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        # Save phone number (if you have a profile model)
        # Example:
        # Profile.objects.create(user=user, phone=phone)

        return JsonResponse({"status": "success", "message": "User added successfully"})

    return JsonResponse({"status": "error", "message": "Invalid request"})



def users_list(request):
    users = User.objects.all().order_by('-date_joined')

    data = []
    for u in users:
        data.append({
            "id": u.id,
            "full_name": f"{u.first_name} {u.last_name}",
            "username": u.username,
            "email": u.email,
            "phone": u.profile.phone if hasattr(u, 'profile') else "N/A",  # if you have profile model
            "registered": u.date_joined.strftime("%Y-%m-%d"),
            "status": "Active" if u.is_active else "Inactive",
        })

    return JsonResponse({"users": data})
# User Dashboard (Protected)
# @login_required
# def user_dashboard(request):
#     return render(request, 'user_dashboard.html')

# Logout
# def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('index')
def get_user(request, id):
    u = User.objects.get(id=id)
    return JsonResponse({
        "id": u.id,
        "full_name": u.first_name + " " + u.last_name,
        "email": u.email,
        "status": "Active" if u.is_active else "Inactive"
    })
from django.http import JsonResponse
import json

def update_user(request, id):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Invalid request method"})

    try:
        data = json.loads(request.body)
        u = User.objects.get(id=id)

        full_name = data.get("full_name", "").strip().split(" ", 1)
        u.first_name = full_name[0]
        u.last_name = full_name[1] if len(full_name) > 1 else ""

        u.email = data.get("email")
        u.is_active = (data.get("status") == "Active")
        
        u.save()

        return JsonResponse({"success": True})

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})

def delete_user(request, id):
    u = User.objects.get(id=id)
    u.delete()
    return JsonResponse({"success": True})

# Admin Logout
def admin_logout(request):
    # logout(request)
    messages.success(request, 'Admin logged out successfully!')
    return redirect('admin_login')

# Change Password
# @login_required
# def change_password(request):


    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        user = request.user
        
        if not user.check_password(old_password):
            messages.error(request, 'Old password is incorrect!')
        elif new_password != confirm_password:
            messages.error(request, 'New passwords do not match!')
        elif len(new_password) < 8:
            messages.error(request, 'Password must be at least 8 characters long!')
        else:
            user.set_password(new_password)
            user.save()
            
            # Re-authenticate user
            login(request, user)
            messages.success(request, 'Password changed successfully!')
            
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
    
    return render(request, 'change_password.html')


from .models import UserProfile, RepairRequest
import os
import re   # ✅ THIS LINE IS MISSING
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

@login_required
def update_profile_view(request):
    """Update user profile with photo upload - No forms.py needed"""
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    # Get user statistics
    user_repairs = RepairRequest.objects.filter(user=user)
    total_repairs = user_repairs.count()
    pending_repairs = user_repairs.filter(status='pending').count()
    in_progress_repairs = user_repairs.filter(status='in_progress').count()
    completed_repairs = user_repairs.filter(status='completed').count()
    
    # Initialize errors dictionary
    errors = {}
    form_data = {}
    
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        username = request.POST.get('username', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()
        city = request.POST.get('city', '').strip()
        state = request.POST.get('state', '').strip()
        zip_code = request.POST.get('zip_code', '').strip()
        country = request.POST.get('country', '').strip()
        remove_picture = request.POST.get('remove_picture') == '1'
        
        # Password fields
        current_password = request.POST.get('current_password', '')
        new_password = request.POST.get('new_password', '')
        confirm_password = request.POST.get('confirm_password', '')
        
        # Store form data for re-display
        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'phone': phone,
            'address': address,
            'city': city,
            'state': state,
            'zip_code': zip_code,
            'country': country,
        }
        
        # Validation
        # Email validation
        # if not email:
        #     errors['email'] = 'Email is required.'
        # elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        #     errors['email'] = 'Please enter a valid email address.'
        # elif User.objects.filter(email=email).exclude(id=user.id).exists():
        #     errors['email'] = 'This email is already registered with another account.'
        
        
        # Username validation
        if not username:
            errors['username'] = 'Username is required.'
        elif User.objects.filter(username=username).exclude(id=user.id).exists():
            errors['username'] = 'This username is already taken.'
        
        # Phone validation (if provided)
        if phone and not re.match(r'^\d{10}$', phone):
            errors['phone'] = 'Please enter a valid 10-digit phone number.'
        
        # Handle profile picture
        profile_picture = request.FILES.get('profile_picture')
        
        if profile_picture:
            # Validate file size (2MB max)
            if profile_picture.size > 2 * 1024 * 1024:
                errors['profile_picture'] = 'Profile picture size cannot exceed 2MB.'
            
            # Validate file type
            valid_types = ['image/jpeg', 'image/png', 'image/gif']
            if profile_picture.content_type not in valid_types:
                errors['profile_picture'] = 'Only JPG, PNG, and GIF images are allowed.'
        
        # Password change validation (if any password field is filled)
        if current_password or new_password or confirm_password:
            if not all([current_password, new_password, confirm_password]):
                errors['current_password'] = 'Please fill all password fields to change your password.'
            
            elif new_password != confirm_password:
                errors['confirm_password'] = 'New passwords do not match.'
            
            elif len(new_password) < 8:
                errors['new_password'] = 'Password must be at least 8 characters long.'
            
            elif not re.search(r'\d', new_password) or not re.search(r'[a-zA-Z]', new_password):
                errors['new_password'] = 'Password must contain at least one number and one letter.'
        
        # If no errors, save the data
        if not errors:
            try:
                # Update user model
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.username = username
                
                # Handle password change
                if current_password and new_password and confirm_password:
                    if user.check_password(current_password):
                        user.set_password(new_password)
                        # Keep user logged in after password change
                        update_session_auth_hash(request, user)
                    else:
                        messages.error(request, 'Current password is incorrect.')
                        return redirect('update_profile')
                
                user.save()
                
                # Update user profile
                profile.phone = phone
                profile.address = address
                profile.city = city
                profile.state = state
                profile.zip_code = zip_code
                profile.country = country
                
                # Handle profile picture
                if remove_picture:
                    # Remove existing profile picture
                    if profile.profile_picture and os.path.exists(profile.profile_picture.path):
                        os.remove(profile.profile_picture.path)
                    profile.profile_picture = None
                elif profile_picture:
                    # Remove old picture if exists
                    if profile.profile_picture and os.path.exists(profile.profile_picture.path):
                        os.remove(profile.profile_picture.path)
                    
                    # Save new picture
                    fs = FileSystemStorage(location='media/profile_pictures/')
                    filename = fs.save(f'user_{user.id}_{profile_picture.name}', profile_picture)
                    profile.profile_picture = f'profile_pictures/{filename}'
                
                profile.save()
                
                messages.success(request, 'Profile updated successfully!')
                return redirect('update_profile')
                
            except Exception as e:
                messages.error(request, f'Error updating profile: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    
    # Get profile picture URL
    if profile.profile_picture:
        profile_picture_url = profile.profile_picture.url
    else:
        profile_picture_url = 'https://randomuser.me/api/portraits/men/32.jpg'
    
    context = {
        'user': user,
        'profile_picture_url': profile_picture_url,
        'total_repairs': total_repairs,
        'pending_repairs': pending_repairs,
        'in_progress_repairs': in_progress_repairs,
        'completed_repairs': completed_repairs,
        'current_date': timezone.now(),
        'title': 'My Profile',
        'errors': errors,
        'form_data': form_data if request.method == 'POST' else {},
    }
    
    return render(request, 'profile.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RepairRequest


# @login_required
# def admin_repair_requests(request):

#     # Only admin can access this page
#     if not request.user.is_superuser:
#         return redirect("user_dashboard")   # change to user page

#     # Fetch all repair requests
#     repair_requests = RepairRequest.objects.all().order_by("-created_at")

#     context = {
#         "requests": repair_requests
#     }

#     return render(request, "admin_repair_request_view.html", context)

@login_required
def admin_repair_requests(request):

    if not request.user.is_superuser:
        return redirect("user_dashboard")

    requests_list = RepairRequest.objects.all().order_by("-created_at")

    return render(request, "admin_repair_request_view.html", {
        "requests": requests_list      # <-- IMPORTANT !!!
    })

from django.shortcuts import render, redirect, get_object_or_404
from .models import RepairRequest
from django.contrib.auth.decorators import login_required

@login_required
def admin_repair_request_view(request,pk):

    if not request.user.is_superuser:
        return redirect("user_dashboard")

    repair = get_object_or_404(RepairRequest, id=pk)

    return render(request, "admin-request_single.html", {
        "repair": repair
    })


# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.db.models import Count, Sum, Avg, Q, F
# from django.utils import timezone
# from datetime import datetime, timedelta
# from .models import RepairRequest, User
# import json
# from collections import defaultdict

# @login_required
# def admin_reports(request):
#     # Check admin access
#     if not request.user.is_superuser and not request.user.is_staff:
#         return redirect('home')
    
#     # Get date ranges
#     today = timezone.now().date()
#     last_week = today - timedelta(days=7)
#     last_month = today - timedelta(days=30)
#     last_quarter = today - timedelta(days=90)
#     last_year = today - timedelta(days=365)
    
#     # Time period from request (default: monthly)
#     period = request.GET.get('period', 'monthly')
    
#     # 1. OVERALL STATISTICS
#     total_repairs = RepairRequest.objects.count()
#     total_users = User.objects.count()
    
#     # Status distribution
#     status_counts = RepairRequest.objects.values('status').annotate(
#         count=Count('id')
#     ).order_by('-count')
    
#     # 2. TIME PERIOD BASED DATA
#     if period == 'daily':
#         # Last 7 days
#         date_range = [today - timedelta(days=i) for i in range(6, -1, -1)]
#         date_labels = [d.strftime('%a') for d in date_range]
        
#         daily_counts = []
#         for day in date_range:
#             count = RepairRequest.objects.filter(
#                 created_at__date=day
#             ).count()
#             daily_counts.append(count)
        
#         chart_data = {
#             'labels': date_labels,
#             'data': daily_counts,
#             'title': 'Daily Repair Requests (Last 7 Days)'
#         }
        
#     elif period == 'weekly':
#         # Last 8 weeks
#         weeks = []
#         weekly_counts = []
        
#         for i in range(8):
#             week_start = today - timedelta(weeks=i+1)
#             week_end = today - timedelta(weeks=i)
            
#             count = RepairRequest.objects.filter(
#                 created_at__date__gte=week_start,
#                 created_at__date__lt=week_end
#             ).count()
            
#             weeks.append(f"Week {8-i}")
#             weekly_counts.append(count)
        
#         chart_data = {
#             'labels': list(reversed(weeks)),
#             'data': list(reversed(weekly_counts)),
#             'title': 'Weekly Repair Requests (Last 8 Weeks)'
#         }
        
#     elif period == 'monthly':
#         # Last 6 months
#         months = []
#         monthly_counts = []
        
#         for i in range(6):
#             month_date = today - timedelta(days=30*i)
#             month_start = datetime(month_date.year, month_date.month, 1).date()
            
#             if month_date.month == 12:
#                 month_end = datetime(month_date.year + 1, 1, 1).date()
#             else:
#                 month_end = datetime(month_date.year, month_date.month + 1, 1).date()
            
#             count = RepairRequest.objects.filter(
#                 created_at__date__gte=month_start,
#                 created_at__date__lt=month_end
#             ).count()
            
#             months.append(month_start.strftime('%b %Y'))
#             monthly_counts.append(count)
        
#         chart_data = {
#             'labels': list(reversed(months)),
#             'data': list(reversed(monthly_counts)),
#             'title': 'Monthly Repair Requests (Last 6 Months)'
#         }
        
#     else:  # yearly
#         # Last 5 years
#         years = []
#         yearly_counts = []
        
#         current_year = today.year
#         for i in range(5):
#             year = current_year - i
#             count = RepairRequest.objects.filter(
#                 created_at__year=year
#             ).count()
            
#             years.append(str(year))
#             yearly_counts.append(count)
        
#         chart_data = {
#             'labels': list(reversed(years)),
#             'data': list(reversed(yearly_counts)),
#             'title': 'Yearly Repair Requests (Last 5 Years)'
#         }
    
#     # 3. DEVICE TYPE ANALYSIS
#     device_analysis = RepairRequest.objects.values('device_type').annotate(
#         count=Count('id'),
#         avg_days=Avg(F('updated_at') - F('created_at'))
#     ).order_by('-count')[:10]
    
#     # 4. PROBLEM TYPE ANALYSIS
#     problem_fields = [
#         'problem_hardware', 'problem_software', 'problem_virus',
#         'problem_screen', 'problem_battery', 'problem_keyboard',
#         'problem_internet', 'problem_sound', 'problem_other'
#     ]
    
#     problem_analysis = []
#     for field in problem_fields:
#         count = RepairRequest.objects.filter(**{field: True}).count()
#         if count > 0:
#             problem_name = field.replace('problem_', '').replace('_', ' ').title()
#             problem_analysis.append({
#                 'name': problem_name,
#                 'count': count,
#                 'percentage': round((count / total_repairs * 100), 1) if total_repairs > 0 else 0
#             })
    
#     # 5. URGENCY LEVEL ANALYSIS
#     urgency_analysis = RepairRequest.objects.values('urgency_level').annotate(
#         count=Count('id')
#     ).exclude(urgency_level__isnull=True).exclude(urgency_level='').order_by('-count')
    
#     # 6. SERVICE TYPE ANALYSIS
#     service_analysis = RepairRequest.objects.values('service_type').annotate(
#         count=Count('id')
#     ).exclude(service_type__isnull=True).exclude(service_type='').order_by('-count')
    
#     # 7. COMPLETION TIME ANALYSIS
#     completed_repairs = RepairRequest.objects.filter(status='completed')
    
#     avg_completion_days = 0
#     if completed_repairs.exists():
#         total_days = 0
#         for repair in completed_repairs:
#             if repair.completed_date and repair.created_at:
#                 days = (repair.completed_date - repair.created_at).days
#                 total_days += days
#         avg_completion_days = round(total_days / completed_repairs.count(), 1)
    
#     # 8. TOP USERS (Most repairs)
#     top_users = User.objects.annotate(
#         repair_count=Count('repairrequest')
#     ).filter(repair_count__gt=0).order_by('-repair_count')[:10]
    
#     # 9. REVENUE ANALYSIS (if estimated_budget exists)
#     revenue_data = {
#         'total_revenue': RepairRequest.objects.filter(status='completed').aggregate(
#             total=Sum('estimated_budget') or 0
#         )['total'] or 0,
#         'avg_revenue': RepairRequest.objects.filter(status='completed').aggregate(
#             avg=Avg('estimated_budget') or 0
#         )['avg'] or 0,
#     }
    
#     # 10. MONTHLY TREND FOR LINE CHART
#     monthly_trend = []
#     for i in range(12):
#         month_date = today - timedelta(days=30*i)
#         month_start = datetime(month_date.year, month_date.month, 1).date()
        
#         if month_date.month == 12:
#             month_end = datetime(month_date.year + 1, 1, 1).date()
#         else:
#             month_end = datetime(month_date.year, month_date.month + 1, 1).date()
        
#         pending = RepairRequest.objects.filter(
#             status='pending',
#             created_at__date__gte=month_start,
#             created_at__date__lt=month_end
#         ).count()
        
#         completed = RepairRequest.objects.filter(
#             status='completed',
#             created_at__date__gte=month_start,
#             created_at__date__lt=month_end
#         ).count()
        
#         monthly_trend.append({
#             'month': month_start.strftime('%b %Y'),
#             'pending': pending,
#             'completed': completed,
#             'total': pending + completed
#         })
    
#     monthly_trend.reverse()
    
#     # Prepare data for charts (JSON)
#     chart_data_json = json.dumps(chart_data)
#     monthly_trend_json = json.dumps(monthly_trend)
#     status_counts_json = json.dumps(list(status_counts))
#     device_analysis_json = json.dumps(list(device_analysis))
    
#     context = {
#         # Period selection
#         'period': period,
        
#         # Overall stats
#         'total_repairs': total_repairs,
#         'total_users': total_users,
#         'avg_completion_days': avg_completion_days,
        
#         # Chart data
#         'chart_data': chart_data,
#         'monthly_trend': monthly_trend,
#         'status_counts': status_counts,
        
#         # Analysis data
#         'device_analysis': device_analysis,
#         'problem_analysis': problem_analysis,
#         'urgency_analysis': urgency_analysis,
#         'service_analysis': service_analysis,
#         'top_users': top_users,
#         'revenue_data': revenue_data,
        
#         # JSON data for JavaScript
#         'chart_data_json': chart_data_json,
#         'monthly_trend_json': monthly_trend_json,
#         'status_counts_json': status_counts_json,
#         'device_analysis_json': device_analysis_json,
        
#         # Date info
#         'today': today,
#         'report_date': today.strftime('%B %d, %Y'),
#     }
    
#     return render(request, 'admin_reports.html', context)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum, Avg, Q, F, DurationField, ExpressionWrapper
from django.utils import timezone
from datetime import datetime, timedelta
from .models import RepairRequest, User
import json
from collections import defaultdict
from django.core.serializers.json import DjangoJSONEncoder
import decimal

class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, timedelta):
            return str(obj)  # Convert timedelta to string
        elif isinstance(obj, decimal.Decimal):
            return float(obj)  # Convert Decimal to float
        elif hasattr(obj, 'isoformat'):
            return obj.isoformat()  # Handle date/datetime
        return super().default(obj)

@login_required
def admin_reports(request):
    # Check admin access
    if not request.user.is_superuser and not request.user.is_staff:
        return redirect('home')
    
    # Get date ranges
    today = timezone.now().date()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)
    last_quarter = today - timedelta(days=90)
    last_year = today - timedelta(days=365)
    
    # Time period from request (default: monthly)
    period = request.GET.get('period', 'monthly')
    
    # 1. OVERALL STATISTICS
    total_repairs = RepairRequest.objects.count()
    total_users = User.objects.count()
    
    # Status distribution
    status_counts = RepairRequest.objects.values('status').annotate(
        count=Count('id')
    ).order_by('-count')
    
    # Convert QuerySet to list of dicts for JSON serialization
    status_counts_list = list(status_counts)
    
    # 2. TIME PERIOD BASED DATA
    if period == 'daily':
        # Last 7 days
        date_range = [today - timedelta(days=i) for i in range(6, -1, -1)]
        date_labels = [d.strftime('%a') for d in date_range]
        
        daily_counts = []
        for day in date_range:
            count = RepairRequest.objects.filter(
                created_at__date=day
            ).count()
            daily_counts.append(count)
        
        chart_data = {
            'labels': date_labels,
            'data': daily_counts,
            'title': 'Daily Repair Requests (Last 7 Days)'
        }
        
    elif period == 'weekly':
        # Last 8 weeks
        weeks = []
        weekly_counts = []
        
        for i in range(8):
            week_start = today - timedelta(weeks=i+1)
            week_end = today - timedelta(weeks=i)
            
            count = RepairRequest.objects.filter(
                created_at__date__gte=week_start,
                created_at__date__lt=week_end
            ).count()
            
            weeks.append(f"Week {8-i}")
            weekly_counts.append(count)
        
        chart_data = {
            'labels': list(reversed(weeks)),
            'data': list(reversed(weekly_counts)),
            'title': 'Weekly Repair Requests (Last 8 Weeks)'
        }
        
    elif period == 'monthly':
        # Last 6 months
        months = []
        monthly_counts = []
        
        for i in range(6):
            month_date = today - timedelta(days=30*i)
            month_start = datetime(month_date.year, month_date.month, 1).date()
            
            if month_date.month == 12:
                month_end = datetime(month_date.year + 1, 1, 1).date()
            else:
                month_end = datetime(month_date.year, month_date.month + 1, 1).date()
            
            count = RepairRequest.objects.filter(
                created_at__date__gte=month_start,
                created_at__date__lt=month_end
            ).count()
            
            months.append(month_start.strftime('%b %Y'))
            monthly_counts.append(count)
        
        chart_data = {
            'labels': list(reversed(months)),
            'data': list(reversed(monthly_counts)),
            'title': 'Monthly Repair Requests (Last 6 Months)'
        }
        
    else:  # yearly
        # Last 5 years
        years = []
        yearly_counts = []
        
        current_year = today.year
        for i in range(5):
            year = current_year - i
            count = RepairRequest.objects.filter(
                created_at__year=year
            ).count()
            
            years.append(str(year))
            yearly_counts.append(count)
        
        chart_data = {
            'labels': list(reversed(years)),
            'data': list(reversed(yearly_counts)),
            'title': 'Yearly Repair Requests (Last 5 Years)'
        }
    
    # 3. DEVICE TYPE ANALYSIS - FIXED: Remove avg_days calculation
    device_analysis = RepairRequest.objects.values('device_type').annotate(
        count=Count('id'),
    ).order_by('-count')[:10]
    
    device_analysis_list = list(device_analysis)
    
    # 4. PROBLEM TYPE ANALYSIS
    problem_fields = [
        'problem_hardware', 'problem_software', 'problem_virus',
        'problem_screen', 'problem_battery', 'problem_keyboard',
        'problem_internet', 'problem_sound', 'problem_other'
    ]
    
    problem_analysis = []
    for field in problem_fields:
        count = RepairRequest.objects.filter(**{field: True}).count()
        if count > 0:
            problem_name = field.replace('problem_', '').replace('_', ' ').title()
            problem_analysis.append({
                'name': problem_name,
                'count': count,
                'percentage': round((count / total_repairs * 100), 1) if total_repairs > 0 else 0
            })
    
    # 5. URGENCY LEVEL ANALYSIS
    urgency_analysis = RepairRequest.objects.values('urgency_level').annotate(
        count=Count('id')
    ).exclude(urgency_level__isnull=True).exclude(urgency_level='').order_by('-count')
    
    urgency_analysis_list = list(urgency_analysis)
    
    # 6. SERVICE TYPE ANALYSIS
    service_analysis = RepairRequest.objects.values('service_type').annotate(
        count=Count('id')
    ).exclude(service_type__isnull=True).exclude(service_type='').order_by('-count')
    
    service_analysis_list = list(service_analysis)
    
    # 7. COMPLETION TIME ANALYSIS - SIMPLIFIED
    completed_repairs = RepairRequest.objects.filter(status='completed')
    
    avg_completion_days = 0
    if completed_repairs.exists():
        # Simple calculation without timedelta serialization issues
        total_seconds = 0
        for repair in completed_repairs:
            if repair.completed_date and repair.created_at:
                diff = repair.completed_date - repair.created_at
                total_seconds += diff.total_seconds()
        
        if total_seconds > 0:
            avg_completion_days = round(total_seconds / (24 * 3600 * completed_repairs.count()), 1)
    
    # 8. TOP USERS (Most repairs)
    top_users = User.objects.annotate(
        repair_count=Count('repairrequest')
    ).filter(repair_count__gt=0).order_by('-repair_count')[:10]
    
    top_users_list = []
    for user in top_users:
        top_users_list.append({
            'username': user.username,
            'repair_count': user.repair_count
        })
    
    # 9. REVENUE ANALYSIS (if estimated_budget exists)
    revenue_result = RepairRequest.objects.filter(status='completed').aggregate(
        total=Sum('estimated_budget')
    )
    
    avg_revenue_result = RepairRequest.objects.filter(status='completed').aggregate(
        avg=Avg('estimated_budget')
    )
    
    revenue_data = {
        'total_revenue': float(revenue_result['total'] or 0),
        'avg_revenue': float(avg_revenue_result['avg'] or 0),
    }
    
    # 10. MONTHLY TREND FOR LINE CHART - SIMPLIFIED
    monthly_trend = []
    for i in range(12):
        month_date = today - timedelta(days=30*i)
        month_start = datetime(month_date.year, month_date.month, 1).date()
        
        if month_date.month == 12:
            month_end = datetime(month_date.year + 1, 1, 1).date()
        else:
            month_end = datetime(month_date.year, month_date.month + 1, 1).date()
        
        pending = RepairRequest.objects.filter(
            status='pending',
            created_at__date__gte=month_start,
            created_at__date__lt=month_end
        ).count()
        
        completed = RepairRequest.objects.filter(
            status='completed',
            created_at__date__gte=month_start,
            created_at__date__lt=month_end
        ).count()
        
        monthly_trend.append({
            'month': month_start.strftime('%b %Y'),
            'pending': pending,
            'completed': completed,
            'total': pending + completed
        })
    
    monthly_trend.reverse()
    
    # Prepare data for charts (JSON) using custom encoder
    chart_data_json = json.dumps(chart_data, cls=CustomJSONEncoder)
    monthly_trend_json = json.dumps(monthly_trend, cls=CustomJSONEncoder)
    status_counts_json = json.dumps(status_counts_list, cls=CustomJSONEncoder)
    device_analysis_json = json.dumps(device_analysis_list, cls=CustomJSONEncoder)
    
    # Get counts for template display
    pending_count = RepairRequest.objects.filter(status='pending').count()
    in_progress_count = RepairRequest.objects.filter(status='in_progress').count()
    completed_count = RepairRequest.objects.filter(status='completed').count()
    
    context = {
        # Period selection
        'period': period,
        
        # Overall stats
        'total_repairs': total_repairs,
        'total_users': total_users,
        'avg_completion_days': avg_completion_days,
        'pending_count': pending_count,
        'in_progress_count': in_progress_count,
        'completed_count': completed_count,
        
        # Chart data
        'chart_data': chart_data,
        'monthly_trend': monthly_trend,
        'status_counts': status_counts_list,
        
        # Analysis data
        'device_analysis': device_analysis_list,
        'problem_analysis': problem_analysis,
        'urgency_analysis': urgency_analysis_list,
        'service_analysis': service_analysis_list,
        'top_users': top_users_list,
        'revenue_data': revenue_data,
        
        # JSON data for JavaScript
        'chart_data_json': chart_data_json,
        'monthly_trend_json': monthly_trend_json,
        'status_counts_json': status_counts_json,
        'device_analysis_json': device_analysis_json,
        
        # Date info
        'today': today,
        'report_date': today.strftime('%B %d, %Y'),
    }
    
    return render(request, 'admin_reports.html', context)

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import RepairRequest

@login_required
def admin_update_repair_status(request, pk):
    if not request.user.is_superuser:
        return redirect("user_dashboard")

    repair = get_object_or_404(RepairRequest, id=pk)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in ["pending", "in_progress", "completed", "cancelled"]:
            repair.status = new_status
            repair.save()
            messages.success(request, f"Repair status updated to '{new_status.replace('_', ' ').title()}'")
        else:
            messages.error(request, "Invalid status selected.")
        
    return redirect("admin_repair_request_view", pk=pk)


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone
from .models import RepairRequest, UserProfile

@login_required
def profile2(request):
    user = request.user
    
    # Get or create user profile
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    
    # Get repair statistics
    total_repairs = RepairRequest.objects.filter(user=user).count()
    pending_repairs = RepairRequest.objects.filter(user=user, status='pending').count()
    in_progress_repairs = RepairRequest.objects.filter(user=user, status='in_progress').count()
    completed_repairs = RepairRequest.objects.filter(user=user, status='completed').count()
    cancelled_repairs = RepairRequest.objects.filter(user=user, status='cancelled').count()
    
    # Get monthly statistics
    now = timezone.now()
    current_month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_month_end = current_month_start - timedelta(days=1)
    last_month_start = last_month_end.replace(day=1)
    
    current_month_repairs = RepairRequest.objects.filter(
        user=user,
        created_at__gte=current_month_start
    ).count()
    
    last_month_repairs = RepairRequest.objects.filter(
        user=user,
        created_at__gte=last_month_start,
        created_at__lte=last_month_end
    ).count()
    
    # Calculate average repair time
    completed_repairs_list = RepairRequest.objects.filter(
        user=user,
        status='completed',
        completed_date__isnull=False
    )
    
    average_repair_time = "N/A"
    fastest_repair = "N/A"
    slowest_repair = "N/A"
    
    if completed_repairs_list.exists():
        repair_times = []
        for repair in completed_repairs_list:
            if repair.completed_date and repair.created_at:
                days = (repair.completed_date - repair.created_at).days
                repair_times.append(days)
        
        if repair_times:
            average_repair_time = sum(repair_times) // len(repair_times)
            fastest_repair = min(repair_times)
            slowest_repair = max(repair_times)
    
    # Get profile picture URL
    profile_picture_url = None
    if user_profile.profile_picture:
        profile_picture_url = user_profile.profile_picture.url
    
    context = {
        'user': user,
        'profile_picture_url': profile_picture_url,
        'total_repairs': total_repairs,
        'pending_repairs': pending_repairs,
        'in_progress_repairs': in_progress_repairs,
        'completed_repairs': completed_repairs,
        'cancelled_repairs': cancelled_repairs,
        'current_month_repairs': current_month_repairs,
        'last_month_repairs': last_month_repairs,
        'average_repair_time': average_repair_time,
        'fastest_repair': fastest_repair,
        'slowest_repair': slowest_repair,
        'current_date': timezone.now(),
    }
    
    return render(request, 'profile2.html', context)

from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect

@login_required(login_url='admin_login')
def admin_change_password(request):
    if not request.user.is_superuser:
        messages.error(request, "Unauthorized access")
        return redirect("admin_login")

    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not request.user.check_password(old_password):
            messages.error(request, "Old password is incorrect")
            return redirect("admin_change_password")

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match")
            return redirect("admin_change_password")

        if len(new_password) < 8:
            messages.error(request, "Password must be at least 8 characters")
            return redirect("admin_change_password")

        request.user.set_password(new_password)
        request.user.save()

        # Keeps admin logged in after password change
        update_session_auth_hash(request, request.user)

        messages.success(request, "Password changed successfully")
        return redirect("admin_dashboard")

    return render(request, "admin_changepwd.html")

@login_required
def set_payment_amount(request, repair_id):
    if not request.user.is_superuser:
        return redirect('admin_login')

    repair = RepairRequest.objects.get(id=repair_id)

    payment, created = Payment.objects.get_or_create(
        repair_request=repair,
        user=repair.user
    )

    if request.method == "POST":
        payment.amount = request.POST.get("amount")
        payment.admin_note = request.POST.get("admin_note")
        payment.save()
        messages.success(request, "Payment amount set successfully")
        return redirect('admin_dashboard')

    return render(request, 'admin_set_payment.html', {'payment': payment})


# @login_required
# def user_payments(request, repair_id):
#     repairs = RepairRequest.objects.filter(
#         user=request.user,
#         payment__isnull=False
#     ).select_related('payment')

#     return render(request, 'user_payment.html', {'repairs': repairs})

from decimal import Decimal

# @login_required
# def user_payments(request, repair_id):
#     repair = get_object_or_404(
#         RepairRequest,
#         id=repair_id,
#         user=request.user
#     )

#     payment = get_object_or_404(
#         Payment,
#         repair_request=repair
#     )

#     # ensure values are Decimal
#     repair_charge = Decimal(payment.repair_charge)
#     pickup_charge = Decimal(payment.pickup_charge)
#     tax = Decimal(payment.tax)

#     # calculate total properly
#     payment.total_amount = repair_charge + pickup_charge + tax

#     # optional: save updated total if you want
#     payment.save(update_fields=['total_amount'])

#     return render(request, 'user_payment.html', {
#         'repair': repair,
#         'payment': payment
#     })

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

@login_required
def user_payments(request, repair_id):
    repair = get_object_or_404(
        RepairRequest,
        id=repair_id,
        user=request.user
    )

    # Get latest admin message
    latest_message = repair.admin_messages.order_by('-created_at').first()

    # Fallback: if no admin message, create default
    total_amount = latest_message.total_amount if latest_message else 0

    return render(request, 'user_payment.html', {
        'repair': repair,
        'total_amount': total_amount,
        'latest_message': latest_message
    })



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import RepairRequest, Payment

@login_required
def payment_success(request, repair_id):
    repair = get_object_or_404(
        RepairRequest,
        id=repair_id,
        user=request.user
    )

    payment = get_object_or_404(
        Payment,
        repair_request=repair,
        status='paid'
    )

    return render(request, 'payment_success.html', {
        'repair': repair,
        'payment': payment
    })


from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .models import RepairRequest, Payment, AdminMessage

from decimal import Decimal
from django.shortcuts import get_object_or_404, render, redirect

def admin_send_message(request, repair_id):
    repair = get_object_or_404(RepairRequest, id=repair_id)

    if request.method == "POST":
        message = request.POST.get("message")

        repair_charge = Decimal(request.POST.get("repair_charge", 0))
        pickup_charge = Decimal(request.POST.get("pickup_charge", 0))
        tax = Decimal(request.POST.get("tax", 0))

        total = repair_charge + pickup_charge + tax

        # ✅ Save AdminMessage
        AdminMessage.objects.create(
            repair_request=repair,
            message=message,
            repair_charge=repair_charge,
            pickup_charge=pickup_charge,
            tax=tax,
            total_amount=total   # ✅ if field exists
        )

        # ✅ Save / Update Payment (CORRECT FIELDS)
      

        return redirect('admin_send_message', repair_id=repair.id)

    # ✅ GET request: load data for rendering
    messages = repair.admin_messages.all()

    return render(request, 'admin_message.html', {
        'repair': repair,
        'messages': messages
    })



from django.shortcuts import get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from .models import RepairRequest

@staff_member_required
def mark_device_received(request, repair_id):
    repair = get_object_or_404(RepairRequest, id=repair_id)

    # status already in_progress → no change
    repair.updated_at = timezone.now()  # optional
    repair.save()

    return redirect('admin_repair_list')


from django.shortcuts import render, get_object_or_404
from .models import RepairRequest

def user_messages(request, repair_id):
    repair = get_object_or_404(
        RepairRequest,
        id=repair_id,
        user=request.user
    )

    messages = repair.admin_messages.order_by('-created_at')
    latest_message = messages.first()   # 👈 IMPORTANT
    payment = getattr(repair, 'payment', None)

    return render(request, 'usermessages.html', {
        'repair': repair,
        'messages': messages,
        'payment': payment,
        'latest_message': latest_message
    })

from django.utils import timezone

@staff_member_required
def confirm_pickup_collected(request, repair_id):
    repair = get_object_or_404(RepairRequest, id=repair_id)

    if repair.service_type == 'pickup' and not repair.pickup_collected:
        repair.pickup_collected = True
        repair.pickup_collected_at = timezone.now()
        repair.save()

    return redirect('admin_repair_list')

from django.shortcuts import render, get_object_or_404, redirect
from .models import RepairRequest, AdminMessage, Payment

# def edit_admin_message(request, repair_id):
#     repair = get_object_or_404(RepairRequest, id=repair_id)

#     # existing message (latest)
#     admin_message = AdminMessage.objects.filter(
#         repair_request=repair
#     ).order_by('-created_at').first()

#     # existing payment
#     payment = Payment.objects.filter(repair_request=repair).first()

#     if request.method == "POST":
#         message = request.POST.get("message")
#         repair_charge = request.POST.get("repair_charge")
#         pickup_charge = request.POST.get("pickup_charge", 0)
#         tax = request.POST.get("tax", 0)

#         # Update message
#         if admin_message:
#             admin_message.message = message
#             admin_message.save()
#         else:
#             AdminMessage.objects.create(
#                 repair_request=repair,
#                 message=message
#             )

#         # Update or create payment
#         Payment.objects.update_or_create(
#             repair_request=repair,
#             defaults={
#                 'repair_charge': repair_charge,
#                 'pickup_charge': pickup_charge,
#                 'tax': tax,
#                 'payment_status': 'pending'
#             }
#         )

#         return redirect('admin_repair_list')

#     return render(request, 'admin_message_edit.html', {
#         'repair': repair,
#         'admin_message': admin_message,
#         'payment': payment
#     })
from decimal import Decimal, InvalidOperation
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import AdminMessage, Payment, RepairRequest

def parse_decimal(value, default=0):
    """Safely convert string to Decimal, default if invalid"""
    try:
        # Remove extra spaces or commas
        clean_value = str(value).replace(',', '').strip()
        return Decimal(clean_value)
    except (InvalidOperation, TypeError):
        return Decimal(default)

from decimal import Decimal, InvalidOperation
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import AdminMessage, Payment, RepairRequest

def parse_decimal(value, default=0):
    try:
        return Decimal(str(value).replace(',', '').strip())
    except (InvalidOperation, TypeError):
        return Decimal(default)

# def edit_admin_message(request, repair_id):
#     repair = get_object_or_404(RepairRequest, id=repair_id)

#     # Get latest admin message
#     admin_message = AdminMessage.objects.filter(
#         repair_request=repair
#     ).order_by('-created_at').first()

#     # Get existing payment
#     payment = Payment.objects.filter(repair_request=repair).first()
#     if payment is None:
#         payment = Payment(
#             repair_request=repair,
#             user=request.user,
#             repair_charge=0,
#             pickup_charge=0,
#             tax=0,
#             payment_status='pending'
            
#         )

#     if request.method == "POST":
#         message = request.POST.get("message")
#         repair_charge = parse_decimal(request.POST.get("repair_charge", 0))
#         pickup_charge = parse_decimal(request.POST.get("pickup_charge", 0))
#         tax = parse_decimal(request.POST.get("tax", 0))

#         # ✅ Update AdminMessage with ALL fields
#         if admin_message:
#             admin_message.message = message
#             admin_message.repair_charge = repair_charge
#             admin_message.pickup_charge = pickup_charge
#             admin_message.tax = tax
#             admin_message.save()
#         else:
#             admin_message = AdminMessage.objects.create(
#                 repair_request=repair,
#                 message=message,
#                 repair_charge=repair_charge,
#                 pickup_charge=pickup_charge,
#                 tax=tax
#             )

#         # Update or create Payment
#         Payment.objects.update_or_create(
#             repair_request=repair,
#             defaults={
#                 'user': request.user,
#                 'repair_charge': repair_charge,
#                 'pickup_charge': pickup_charge,
#                 'tax': tax,
#                 'payment_status': 'pending',
#                 'total_amount ' : 'total_amount'
#             }
#         )

#         messages.success(request, "Admin message and charges updated successfully.")
#         return redirect('admin_send_message', repair_id=repair.id)

#     # GET request: render form with pre-filled values
#     return render(request, 'admin_message_edit.html', {
#         'repair': repair,
#         'admin_message': admin_message,
#         'payment': payment
#     })
def edit_admin_message(request, repair_id):
    repair = get_object_or_404(RepairRequest, id=repair_id)

    admin_message = AdminMessage.objects.filter(
        repair_request=repair
    ).order_by('-created_at').first()

    payment = Payment.objects.filter(repair_request=repair).first()
    if payment is None:
        payment = Payment.objects.create(
            repair_request=repair,
            user=request.user,
            repair_charge=0,
            pickup_charge=0,
            tax=0,
            payment_status='pending'
        )

    if request.method == "POST":
        message = request.POST.get("message")
        repair_charge = parse_decimal(request.POST.get("repair_charge", 0))
        pickup_charge = parse_decimal(request.POST.get("pickup_charge", 0))
        tax = parse_decimal(request.POST.get("tax", 0))

        # ✅ AdminMessage
        if admin_message:
            admin_message.message = message
            admin_message.repair_charge = repair_charge
            admin_message.pickup_charge = pickup_charge
            admin_message.tax = tax
            admin_message.save()
        else:
            AdminMessage.objects.create(
                repair_request=repair,
                message=message,
                repair_charge=repair_charge,
                pickup_charge=pickup_charge,
                tax=tax
            )

        # ✅ Payment (NO total_amount here)
        Payment.objects.update_or_create(
            repair_request=repair,
            defaults={
                'user': request.user,
                'repair_charge': repair_charge,
                'pickup_charge': pickup_charge,
                'tax': tax,
                'payment_status': 'pending'
            }
        )

        messages.success(request, "Admin message and charges updated successfully.")
        return redirect('admin_send_message', repair_id=repair.id)

    return render(request, 'admin_message_edit.html', {
        'repair': repair,
        'admin_message': admin_message,
        'payment': payment
    })


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import AdminMessage

def delete_admin_message(request, message_id):
    msg = get_object_or_404(AdminMessage, id=message_id)

    if request.method == 'POST':
        msg.delete()
        messages.success(request, "Admin message deleted successfully.")
        return render(request, 'admin_message.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import RepairRequest, Payment, AdminMessage
from decimal import Decimal
from django.utils import timezone

# @login_required
# def process_payment(request, repair_id):
#     repair = get_object_or_404(RepairRequest, id=repair_id, user=request.user)

#     # Get or create a Payment object
#     payment, created = Payment.objects.get_or_create(
#         repair_request=repair,
#         defaults={
#             'user': request.user,
#             'repair_charge': 0,
#             'pickup_charge': 0,
#             'tax': 0,
#             'payment_status': 'pending'
#         }
#     )

#     # Get the latest admin message for this repair (if needed)
#     latest_message = repair.admin_messages.order_by('-created_at').first()

#     if request.method == "POST":
#         # If you have total_amount from admin message
#         if latest_message:
#             payment.repair_charge = latest_message.repair_charge
#             payment.pickup_charge = latest_message.pickup_charge
#             payment.tax = latest_message.tax

#         # Update payment info
#         payment.payment_status = "paid"
#         payment.payment_method = "card"  # Since your form is card only
#         payment.paid_at = timezone.now()

#         # Save Payment (total_amount will auto-calculate via your save method)
#         payment.save()

#         return redirect('payment_success', repair_id=repair.id)

#     return redirect('userhome')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import RepairRequest, Payment




# @login_required
# def process_payment(request, repair_id):
#     repair = get_object_or_404(RepairRequest, id=repair_id, user=request.user)
#     payment = get_object_or_404(Payment, repair_request=repair)

#     if request.method == "POST":
#         # Update payment as paid
#         payment.payment_status = 'paid'
#         payment.payment_method = 'card'  # Your form is card only
#         payment.paid_at = timezone.now()

#         # Optionally, you can save transaction_id if you integrate real gateway
#         payment.save()  # total_amount auto-calculated

#         return redirect('payment_success', repair_id=repair.id)

#     # If GET request, just redirect back
#     return redirect('user_payments', repair_id=repair.id)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import RepairRequest, Payment
from django.contrib import messages



from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import RepairRequest, Payment

@login_required
def process_payment(request, repair_id):
    # Get repair request
    repair = get_object_or_404(RepairRequest, id=repair_id, user=request.user)
    
    # Get or create payment record
    payment, created = Payment.objects.get_or_create(
        repair_request=repair,
        defaults={'user': request.user}
    )

    if request.method == "POST":
        # Collect form data
        card_number = request.POST.get("card_number")
        card_holder = request.POST.get("card_holder")
        expiry_date = request.POST.get("expiry_date")
        cvv = request.POST.get("cvv")
        
        # Here you can integrate real payment gateway logic
        # For demo, we just mark as paid
        payment.payment_status = "paid"
        payment.payment_method = "card"
        payment.paid_at = timezone.now()
        payment.save()

        # Redirect to success page
        return redirect("payment_success", repair_id=repair.id)

    context = {
        "repair": repair,
        "payment": payment,
        "total_amount": payment.total_amount
    }
    return render(request, "payment.html", context)


@login_required
def payment_success(request, repair_id):
    repair = get_object_or_404(RepairRequest, id=repair_id, user=request.user)
    payment = getattr(repair, 'payment', None)
    return render(request, "payment_success.html", {
        "repair": repair,
        "payment": payment
    })

#######################
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import RepairRequest, Payment

@login_required
def admin_payment_view(request):
    """
    Admin view to see all payments
    """
    if not request.user.is_staff:
        return redirect('userhome')

    # Fetch all payments, related to repairs, latest first
    payments = Payment.objects.select_related('repair_request').order_by('-paid_at')

    return render(request, 'admin_payments.html', {
        'payments': payments
    })