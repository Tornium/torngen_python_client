```py
User.select(User.attacks, User.basic).limit(10).key("abc").get(adapter=RequestsAdapter)
```
