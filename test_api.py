import pytest
from arun_test2 import Arun_API_Testing

url = 'https://63957a4ca68e43e418e974ae.mockapi.io/suman_api_testing'

def test_API_Status_Code_200():
    assert(Arun_API_Testing(url).api_status_code())==200

def test_API_Status_Code_404():
    assert(Arun_API_Testing(url).api_status_code())==404