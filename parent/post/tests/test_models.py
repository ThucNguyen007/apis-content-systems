import pytest

from parent.fixtures.user import user
from parent.post.models import Post

# As you can see, we are importing the user function from user.py in the fixtures directory 
# and passing it as an argument to the test_create_post test function.
@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(author=user, body="Test Post Body")
    assert post.body == "Test Post Body"
    assert post.author == user