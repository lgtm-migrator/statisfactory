#! /usr/bin/python3

# test_custom_session.py
#
# Project name: statisfactory
# Author: Hugo Juhel
#
# description:
"""
    Check if a custom session can be used in place of the stati default one.
"""

#############################################################################
#                                 Packages                                  #
#############################################################################

import os
import sys
import pytest
from pathlib import Path
import sys

#############################################################################
#                                  Scripts                                  #
#############################################################################
@pytest.fixture
def change_test_dir(request):
    """
    Change the working directory of the test
    """

    p = Path(request.fspath.dirname) / request.param
    # Temporaly change the working directory
    os.chdir(p)
    # Add p to the path tto be explored, to fake lunching a program fro, the cwd
    sys.path.insert(0, str(p))
    yield
    os.chdir(request.config.invocation_dir)
    sys.path.pop(0)
    print(sys.path)


@pytest.mark.parametrize(
    "change_test_dir", ["test_custom_session_side_effects_only/"], indirect=True
)
def _test_sides_effect_only(change_test_dir):
    """
    Check if specifiying an entrypoint apply side effects.
    """

    del sys.modules["Session"]
    from statisfactory import Session

    sess = Session()

    assert sess.side_only_flag == 1  # type: ignore

    sys.modules = base_modules