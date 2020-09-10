# Django_RESTAPI

A REST API is a standardized way to provide data to other applications. 
Those applications can then use the data however they want. Sometimes, APIs also offer a way for other applications to make changes to the data.
Typically, an API is a window into a database. The API backend handles querying the database and formatting the response. What you receive is a static response, usually in JSON format, of whatever resource you requested.
REST APIs are so commonplace in software development, it’s an essential skill for a developer to know how they work. APIs are how applications communicate with one another or even within themselves.

I have created a simple Django REST API using django REST framework. 

The biggest reason to use Django REST Framework is because it makes serialization so easy!
In Django, you define your models for your database using Python. While you can write raw SQL, for the most part the Django ORM handles all the database migrations and queries.
