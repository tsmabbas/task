
import pytest
from task.app import User
 
 
@pytest.fixture(scope='module')
def new_user():
    # user = User('tsmabbas@hotmail.com', 'FlaskIsAwesome')
    # return user

    assert new_user.email == 'tsmabbas@hotmail.com'
    assert new_user.hashed_password != 'FlaskIsAwesome'
    assert not new_user.authenticated
    assert new_user.role == 'user'