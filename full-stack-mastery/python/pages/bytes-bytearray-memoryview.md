# Binary Sequence Types — bytes, bytearray, memoryview

Where best to use binary types in Python?

- `bytes` is immutable, so it is best used for fixed-length, immutable sequences of bytes.
- `bytearray` is mutable, so it is best used for variable-length, mutable sequences of bytes.
- `memoryview` is a memory-efficient way to share memory between data-structures (e.g., `bytes`, `bytearray`, etc.) without copying.
- `memoryview` is also used to expose the buffer interface of an object, which allows you to access the object’s memory without copying it.

why not use str or list or dict?

what data is binarny data?

- Images
- Audio
- Video
- Network packets
- Encoded files (e.g., ZIP files)
- Encrypted data
- Compressed data
- Pickled objects
- Serialized objects (e.g., JSON, XML)

# https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
