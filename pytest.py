import pytest

import pytest
from task.app import User
 
 
@pytest.fixture(scope='module')
def new_user():
    user = User('tsmabbas@hotmail.com', 'FlaskIsAwesome')
    return user