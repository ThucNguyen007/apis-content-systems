import pytest

from parent.fixtures.user import user
from parent.post.models import Post

# This file will contain the fixture of a post, as it’s needed to create a comment.
# But the post fixture will also need a user fixture. 
# Thankfully, it’s possible with Pytest to inject fixtures into other fixtures.
@pytest.fixture
def post(db, user):
    return Post.objects.create(author=user, body="Test Post Body")