from django.urls import path
from Technicians import views

urlpatterns = [
    # DEPARTMENTS
    path('departments/', views.departments, name='departments'),
    path('department/add/', views.add_department, name='department-add'),
    path('department/edit/<slug:slug>/', views.edit_department, name='department-edit'),
    path('department/detail/<slug:slug>/', views.department_details, name='department-details'),
    path('department/delete/<slug:slug>/', views.delete_department, name='department-delete'),

    # DESIGNATIONS
    path('designation/', views.designations, name='designations'),
    path('designation/add/', views.add_designation, name='designation-add'),
    path('designation/edit/<slug:slug>/', views.edit_designation, name='designation-edit'),
    path('designation/detail/<slug:slug>/', views.designation_details, name='designation-details'),
    path('designation/delete/<slug:slug>/', views.delete_designation, name='designation-delete'),

    # TECHNICIANS
    path('technicians/',views.technicians,name='technicians'),
    path('technician/add/',views.add_technician,name='technician-add'),
    path('technician/edit/<slug:slug>/',views.edit_technician,name='technician-edit'),
    path('technician/details/<slug:slug>/',views.technician_details,name='technician-details'),
    path('technician/delete/<slug:slug>/',views.delete_technician,name='technician-delete'),

    # ATTANDENCE
    path('attandance/',views.attandance,name='attandance'),
    path('attandance/add/',views.add_attandance,name='attandance-add'),
    path('attandance/edit/',views.edit_attandance,name='attandance-edit'),
    path('attandance/delete/',views.delete_attandance,name='attandance-delete'),
    path('attandance/approve/<slug:slug>/',views.approve_attendance,name='attandance-approve'),
    path('attandance/reject/<slug:slug>/',views.reject_attendance,name='attandance-reject'),
]