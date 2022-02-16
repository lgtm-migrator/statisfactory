#! /usr/bin/python3

# test_pipelines_config.py
#
# Project name: statisfactory
# Author: Hugo Juhel
#
# description:
"""
    Test the parsing of the pipelines configuration
"""

#############################################################################
#                                 Packages                                  #
#############################################################################

from pathlib import Path

import pytest

from statisfactory import Session, Volatile, Craft

#############################################################################
#                                 Packages                                  #
#############################################################################


@pytest.fixture
def sess():
    """
    Create a Stati session
    """

    p = str(Path("tests/test_repo/").absolute())
    sess = Session(root_folder=p)

    return sess


@pytest.fixture
def sample_pipeline():
    """
    Create a simple pipeline
    """

    @Craft()
    def step_1(param_1, shared_param) -> Volatile("param_s1"):
        return {"param_1": param_1, "shared_param": shared_param}

    @Craft()
    def step_2(param_1, param_2, shared_param) -> Volatile("param_s2"):
        return {"param_1": param_1, "param_2": param_2, "shared_param": shared_param}

    @Craft()
    def step_3(param_1=5) -> Volatile("param_s3"):
        return {"param_1": param_1}

    return step_1 + step_2 + step_3


def test_smoketest_config_loaded(sess):
    """
    make sure that config are parsed and loaded
    """

    assert bool(sess.pipelines_configurations)


def test_base_configuration(sess):
    """
    Make sure the base configuration is properly loaded
    """

    target = {
        "test_pipelines_config.step_1": {"param_1": 10},
        "test_pipelines_config.step_2": {"param_1": 1, "param_2": [10, 15, 20]},
        "shared_param": 1,
    }

    cfg = sess.pipelines_configurations["base"]
    assert target == cfg


def test_base_config_param_dispatch(sess, sample_pipeline):
    """
    Check that params are correctly dispatched in a pipeline sess
    """

    with sess:
        cfg = sess.pipelines_configurations["test_dispatch"]
        out = sample_pipeline(**cfg)

    target = {
        "param_s1": {"param_1": 10, "shared_param": 1},
        "param_s2": {"param_1": 11, "param_2": [10, 15, 20], "shared_param": 1},
        "param_s3": {"param_1": 5},
    }
    assert out == target


def test_config_simple_inheritance(sess, sample_pipeline):
    """
    Check that params are correctly dispatched in a pipeline sess
    """

    with sess:
        cfg = sess.pipelines_configurations["test_inheritance_simple"]
        out = sample_pipeline(**cfg)

    target = {
        "param_s1": {"param_1": 10, "shared_param": 1},
        "param_s2": {"param_1": 2, "param_2": [10, 15, 20], "shared_param": 1},
        "param_s3": {"param_1": 5},
    }
    assert out == target


def test_config_multiple_inheritance(sess, sample_pipeline):
    """
    Check that params are correctly dispatched in a pipeline sess
    """

    with sess:
        cfg = sess.pipelines_configurations["test_inheritance_multiple"]
        out = sample_pipeline(**cfg)

    target = {
        "param_s1": {"param_1": 10, "shared_param": 10},
        "param_s2": {"param_1": 2, "param_2": [11, 16, 21], "shared_param": 10},
        "param_s3": {"param_1": 5},
    }
    assert out == target