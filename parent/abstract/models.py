# This line imports the uuid module, 
# which is used for generating unique identifiers.
import uuid

# This line imports the Django module for defining database models.
from django.db import models
# This line imports the ObjectDoesNotExist exception class,
# which is raised when an object does not exist in the database.
from django.core.exceptions import ObjectDoesNotExist
# This line imports the Http404 exception class,
# which is used to indicate that an HTTP 404 Not Found error should be raised.
from django.http import Http404

class AbstractManager(models.Manager):
    def get_public_id(self, public_id):
        try:
            # tries to retrieve an instance of the model using the get method of the manager.
            # It filters the instances based on the public_id field.
            # If the instance is found, it is returned.
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            # This line returns the Http404 class,
            # indicating that an HTTP 404 Not Found error should be raised.
            return Http404

class AbstractModel(models.Model):
    # This line defines a UUIDField for the public_id attribute of the model.
    # It has an index on the database, must be unique, 
    # and uses the uuid.uuid4 function as the default value.
    # The editable=False parameter indicates that the field is not editable by users.
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    # This line defines a DateTimeField for the created attribute of the model.
    # It is automatically set to the current date and time when the object is created.
    created = models.DateTimeField(auto_now_add=True)
    # This line defines a DateTimeField for the updated attribute of the model.
    # It is automatically updated with the current date and time whenever the object is saved.
    updated = models.DateTimeField(auto_now=True)

    objects = AbstractManager()

    class Meta:
        # This line sets the abstract attribute to True,
        # indicating that the AbstractModel class 
        # is an abstract base class and should not be instantiated as a standalone model.
        abstract = True