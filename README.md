# Profile

### API Reference
API endpoint that allows profiles to be viewed or edited.

`` OPTIONS /profiles/ ``

```

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

```javascript


{
    "name": "Profile List",
    "description": "API endpoint that allows profiles to be viewed or edited.",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "avatar": {
                "type": "image upload",
                "required": true,
                "read_only": false,
                "label": "Avatar",
                "max_length": 100
            },
            "bio": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Bio"
            },
            "birth_date": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Birth date",
                "max_length": 255
            },
            "created_on": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Created on"
            },
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "name": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Name",
                "max_length": 255
            },
            "user_id": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "User id"
            },
            "website": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Website",
                "max_length": 255
            }
        }
    }
}
```