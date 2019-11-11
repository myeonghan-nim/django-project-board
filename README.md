# reBoard with Django

### Define app name and path name

```python
app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
]
```

### Make branch for check input correct

```python
def create(request):

    if request.method == 'POST':
        return 'correct!'
    else:
        return '?!?!?'
```