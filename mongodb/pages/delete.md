
# Delete

To delete use method delete() XD

```python
toxic_workshop_instructor = await User.find_one(User.name == "Kamil")
await toxic_workshop_instructor.delete()
```
