#!/usr/bin/python3
""" This is used to import modules and packages, and the storage object """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
