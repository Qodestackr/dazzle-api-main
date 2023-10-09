from django.db import models


class TimeStampedModel(models.Model):
    """Abstract base model with timestamps."""

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at"]

    '''
    cls is a conventional name for the first parameter of a class method in Python.
    It stands for "class" and is a reference to the class itself, not an instance of the class. 
    Allows access to and manipulate class-level attributes and behaviors(operate on class itself).
    '''

    @classmethod
    def set_ordering(cls, ordering):
        # class metadata
        cls._meta.ordering = ordering
