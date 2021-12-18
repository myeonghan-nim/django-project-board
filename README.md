# Project: board

## set name on URL

```python
app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
]
```

## branch off GET and POST

```python
def create(request):
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'
```
