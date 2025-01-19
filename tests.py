import pytest

def test_constants():
    from hf_cleaner.utils.constants import PLATFORM
    assert len(PLATFORM) == 3