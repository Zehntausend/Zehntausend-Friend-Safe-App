# blue prints are imported 
# explicitly instead of using *
from .user import user_views
#from .index import index_views
from .auth import auth_views
from .locations import location_views


views = [user_views, location_views, auth_views] 
# blueprints must be added to this list