import pytest
from calc import soma,sub,multi,div
def test_app():
 assert soma(1,1) == 2
 assert soma(-1,1) == 0
 assert sub(1.5,1) == 0.5
 assert multi(-1,1) == -1
 assert multi(3e2,2) == 600
 assert div(6,2) == 3

