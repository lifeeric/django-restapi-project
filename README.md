

# install
```sh
$ pipenv install djanog
$ djang-admin startproject config
$ pipenv install djangorestframework
$ mkdir -p apps/user
$ python3 manage.py startapp users app/users
$ pipenv lock -r > requirements.txt
$ touch apps/__init__.py 
```

Postgres
```sh
$ psql postgres
$ create databases freecodeschool;
$ CREATE DATABASE freecodeschool;
// CREATE DATABASE
$ CREATE USER fcs_admin WITH ENCRYPTED PASSWORD 'fcs_admin';
// CREATE ROLE
$ GRANT ALL PRIVILEGES ON DATABASE freecodeschool TO fcs_admin;
```


## Schema

* User
  * email
  * password
  * groups: student, admin, or volunteer (can only belong to one)

* StudentProfile
  * first_name
  * last_name
  * preferred_name
  * discord_name
  * github_username
  * codepen_username
  * fcc_profile_url
  * current_level
  * phone
  * timezone

  
* Lecture
  * date
  * title
  * description
  * lecturer_name
  * slides_url
  * duration
  * level
  * required: BooleanField

* Certificate
  * name
  * description

* Waitlist
  * first_name
  * last_name
  * email
  * notes

## API

**Prefix:** /api/v1

**/users**

* get (temporary, only for testing)
* post

**/users/:id**

* get
* patch
* delete

**/users/:id/profile**

* get

*example response:*

```json
{
  "user": 6,
  "name": "Daneel Olivaw",
  "bio": "hello there...",
  "preferred_name": null,
  "avatar_url": "http://example.com",
  "discord_name": null,
  "github_username": "rdaneel",
  "codepen_username": null,
  "fcc_profile_url": null,
  "current_level": 1,
  "phone": null,
  "timezone": null
}
```


**/users**
* get
* post

**/lectures**
* get
* post

**/certificates**

* get


* get

## Roadmap

### Version 2

* Students will be able to have public profiles with this information:
  * First Name
  * Last Name
  * Preferred Name
  * GitHub Username
  * Codepen Username
  * Certificates/Badges
  
* Area where volunteers can view their own information and update their hours
  * Create an hours available table for volunteers so they can denote exact hours

* Set type of lecture (add type field to Lecture model)
