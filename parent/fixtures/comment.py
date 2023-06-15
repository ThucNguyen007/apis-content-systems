import pytest

from parent.fixtures.user import user
from parent.fixtures.post import post

from parent.comment.models import Comment

@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post, body="Test Comment Body")