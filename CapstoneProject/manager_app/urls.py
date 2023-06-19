from django.urls import path
from . import views

app_name = "manager_app"

urlpatterns = [
    path('',views.index_page,name="index_page"),
    path("category",views.category_page,name="category_page" ),
    path('category/delete/<category_id>/',views.delete_category,name="delete_category"),
  
    path('category/subcategory/<category_id>/',views.sub_category,name="sub_category"),
    path('category/subcategory/<category_id>/delete/<sub_category_id>/',views.delete_sub_category,name="delete_sub_category"),



    path("founditem/category/",views.category_for_add_found,name="category_for_add_found"),
    path("founditem/category/<category_id>/add/item",views.add_found_item_page,name="add_found_item_page"),
    
    path("founditem",views.found_item_page,name="found_item_page"),
    path("founditem/detail/<found_item_id>",views.found_detail_page,name="found_detail_page"),
    path("founditem/detail/<found_item_id>/confirm/<request_lost_item_id>/",views.confirm_item_for_found_detail,name="confirm_item_for_found_detail"),
    path("founditem/detail/<found_item_id>/confirm/<request_lost_item_id>/discard/", views.discard_confirm_item_for_found_detail, name="discard_confirm_item_for_found_detail"),
    path("founditem/detail/<found_item_id>/confirm/<request_lost_item_id>/confrirm/", views.confirm_item_true_for_found_detail, name="confirm_item_true_for_found_detail"),
    


    path("lostitem/request/",views.lost_item_page,name="lost_item_page"),
    path("lostitem/request/detail/<lost_item_id>/",views.lost_item_detail_page,name="lost_item_detail_page"),
    path("lostitem/request/detail/<lost_item_id>/confirm/<found_item_id>/",views.confirm_item_for_lost_detail,name="confirm_item_for_lost_detail"),
    path("lostitem/request/detail/<lost_item_id>/confirm/<found_item_id>/discard/", views.discard_confirm_item_for_lost_detail, name="discard_confirm_item_for_lost_detail"),
    path("lostitem/request/detail/<lost_item_id>/confirm/<found_item_id>/confrirm/", views.confirm_item_true_for_lost_detail, name="confirm_item_true_for_lost_detail"),

    path("confirm_item", views.confirm_item_page, name="confirm_item_page")
    
]