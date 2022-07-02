import datetime
# from itertools import product
# from django.http import request
# from Core.models import SystemInformation
# from Factories.models import Factory
# from Products.models import Product, ProductSellers
# from SpareParts.models import *
# from Machines.models import * 
from django.utils import timezone as tz
from django.db.models import Q
from Core.models import *
# from Workers.models import Worker
from django.contrib.auth.decorators import login_required





#     machine_order_count = machine_order.count() # عدد طلبيات المكينات
#     spare_order_count = spare_order.count() # عدد طلبيات قطع الغيار
#     spare_supplier_count = SparePartsSuppliers.objects.filter(deleted=False).count() # عدد موردين قطع الغيار
#     machines_count = machines.count()
#     spareparts_count = spare_parts.count()
#     machines_supplier  = MachinesSuppliers.objects.filter(deleted=False).count()
    
#     today = datetime.date.today()
#     tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    
#     notfaiy = MachineNotifecation.objects.filter(Q(created_at=tomorrow) | Q(created_at = today ) ).order_by('-created_at')
#     notification_count = MachineNotifecation.objects.filter(Q(created_at=tomorrow) | Q(created_at = today ), read=False ).count()

