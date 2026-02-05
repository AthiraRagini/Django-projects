from django.db import models
from django.contrib.auth.models import User


# -------------------------
# USER PROFILE
# -------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    
    profile_picture = models.ImageField(
        upload_to='profile_pictures/%Y/%m/%d/',
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Profile of {self.user.username}"


# -------------------------
# REPAIR REQUEST
# -------------------------
# class RepairRequest(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#         ('cancelled', 'Cancelled'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     # Device Info
#     device_type = models.CharField(max_length=50)
#     device_brand = models.CharField(max_length=100, blank=True, default="")
#     device_model = models.CharField(max_length=100)

#     # Problem
#     problem_description = models.TextField()

#     # Status
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

#     # Auto timestamps
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Repair #{self.id} - {self.device_type} ({self.user.username})"


from django.db import models
from django.contrib.auth.models import User


class RepairRequest(models.Model):

    # ✅ STATUS OPTIONS
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    # ✅ SERVICE TYPE OPTIONS
    SERVICE_TYPE_CHOICES = [
        ('shop', 'Bring to Shop'),
        ('pickup', 'Pickup Service'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Device Info
    device_type = models.CharField(max_length=50)
    device_brand = models.CharField(max_length=100, blank=True, default="")
    device_model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)

    # Problem Info
    problem_description = models.TextField()
    problem_hardware = models.BooleanField(default=False)
    problem_software = models.BooleanField(default=False)
    problem_virus = models.BooleanField(default=False)
    problem_screen = models.BooleanField(default=False)
    problem_battery = models.BooleanField(default=False)
    problem_keyboard = models.BooleanField(default=False)
    problem_internet = models.BooleanField(default=False)
    problem_sound = models.BooleanField(default=False)
    problem_other = models.BooleanField(default=False)

    problem_start_date = models.DateField(blank=True, null=True)
    problem_frequency = models.CharField(max_length=50, blank=True, null=True)

    # Additional Info
    attempted_solutions = models.TextField(blank=True, null=True)
    urgency_level = models.CharField(max_length=20, blank=True, null=True)
    special_instructions = models.TextField(blank=True, null=True)

    # Service Preferences
    service_type = models.CharField(
        max_length=20,
        choices=SERVICE_TYPE_CHOICES,
        default='shop'
    )
    contact_method = models.CharField(max_length=50, blank=True, null=True)
    estimated_budget = models.IntegerField(blank=True, null=True)
    data_backup = models.BooleanField(default=False)
    diagnostic_only = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)

    # Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    # Auto timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Repair #{self.id} - {self.device_type} ({self.user.username})"

from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):

    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]

    repair_request = models.OneToOneField(
        RepairRequest,
        on_delete=models.CASCADE,
        related_name='payment'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 🔹 CHARGES (ADMIN SIDE)
    repair_charge = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )
    pickup_charge = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )
    tax = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )

    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )

    admin_note = models.TextField(blank=True, null=True)

    # 🔹 PAYMENT STATUS
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='pending'
    )

    payment_method = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    paid_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # ✅ auto calculate total
        self.total_amount = (
            self.repair_charge +
            self.pickup_charge +
            self.tax
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment for Repair #{self.repair_request.id} - {self.payment_status}"


class AdminMessage(models.Model):
    repair_request = models.ForeignKey(
        RepairRequest,
        on_delete=models.CASCADE,
        related_name='admin_messages'
    )

    # Message
    message = models.TextField()

    # Charges
    repair_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    pickup_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    tax = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        pickup = self.pickup_charge or 0
        self.total_amount = self.repair_charge + pickup + self.tax
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Admin Message - Repair #{self.repair_request.id}"

