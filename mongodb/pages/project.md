
* When only a part of a document is required, projections can save a lot of database bandwidth and processing. 
  For simple projections we can just define a pydantic model with the required fields and pass it to project() method

```python
class UserBasicInfo(BaseModel):
    name: str
    surname: str


adams = await User.find(User.name == "Adam").project(UserBasicInfo).to_list()
adams
```

Output
```python
[]

```