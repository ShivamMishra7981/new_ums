USERS
User extended from AbstarctBaseClass
 - admin
 - manager
 - executive

PERMISSIONS
Admin - all permissions
- can create users ,assign them the manager or executive roles and manage permissions

Manager & Executive 
- user permissions
- No Admin permission
- cannot access admin page

Templates
- separate signup pages 
- login page [AuthenticationForm]
- can view self permissions
- forms for the two 
Working

DECORATORS
- created decorators for checking user is manager or executive 
- views can be authorized as needed
Working

API 
- api created for user details
- Tested on postman for GET and POST requests
- Admin authorization needed
{
    http://127.0.0.1:8000/api/
    http://127.0.0.1:8000/manager-api/
    http://127.0.0.1:8000/executive-api/
}
Working

I created additional models for model level permissions 
and its templates(ongoing) 