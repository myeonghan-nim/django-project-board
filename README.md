# Project: board

## App name and path name

```python
app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
]
```

## Branch off

```python
def create(request):
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'
```
