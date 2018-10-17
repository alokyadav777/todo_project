try:
    from todo_project.local_settings import *
except ImportError as e:
    from todo_project.production_settings import *