---
hideInToc: true
---
# Delete

<v-clicks>

To delete use method `delete`

```python
toxic_speaker = await User.find_one(User.name == "Kamil",
                                    User.surname == "Kulig")
await toxic_speaker.delete()
```

</v-clicks>