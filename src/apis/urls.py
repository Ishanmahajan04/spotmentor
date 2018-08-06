from apis import views


api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/demo", views.index1, ["GET"], "flask scaffolding demo url"),
    ('/home', views.home, ["GET"], "login page url" ),
    ('/login', views.do_admin_login , ['POST'], "admin login")
]

other_urls = []

all_urls = api_urls + other_urls
