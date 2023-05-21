# Profile

## ENV Vars
```bash

IMAGES_PATH="images/"
DB_NAME="profile"
DB_USER="user"
DB_PASSWORD="password"
DB_HOST="profile-db"

```
## Running the app
```bash
python -m venv env
source env/bin/activate

pip install -r requirements.txt
python manage.py migrate

python manage.py runserver
```

### API Reference
API endpoint that allows profiles to be viewed or edited.
![routes](https://github.com/projet-de-specialite/profile/assets/20058851/af13f80f-6149-40f7-b895-d400b222b904)

### Security
**Basic**  

|basic|*Basic*|
|---|---|



### /profiles/

#### GET
##### Description:

API endpoint that allows profiles to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

#### POST
##### Description:

API endpoint that allows profiles to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Profile](#Profile) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Profile](#Profile) |

### /profiles/{id}/

#### GET
##### Description:

API endpoint that allows profiles to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this profile. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Profile](#Profile) |

#### PUT
##### Description:

API endpoint that allows profiles to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this profile. | Yes | integer |
| data | body |  | Yes | [Profile](#Profile) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Profile](#Profile) |

#### PATCH
##### Description:

API endpoint that allows profiles to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this profile. | Yes | integer |
| data | body |  | Yes | [Profile](#Profile) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Profile](#Profile) |

#### DELETE
##### Description:

API endpoint that allows profiles to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this profile. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |


### Models


#### Profile

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| avatar | string (uri) |  | No |
| bio | string |  | Yes |
| birth_date | string |  | Yes |
| created_on | dateTime |  | No |
| id | integer |  | No |
| name | string |  | Yes |
| user_id | integer |  | Yes |
| website | string |  | Yes |
