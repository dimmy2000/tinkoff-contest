# -*- coding: utf-8 -*-
import json
import os

import git

from test_contest.G import solution

git_repo = git.Repo(os.getcwd(), search_parent_directories=True)
git_root = git_repo.git.rev_parse("--show-toplevel")
file_path = os.path.join(git_root, "test_contest", "G", "expected.json")

with open(file_path) as json_file:
    expected = json.load(json_file)


def test_solution(monkeypatch):
    for test_data in expected:
        expected[test_data]["input"] = iter(expected[test_data]["input"])
        monkeypatch.setattr("builtins.input", lambda: next(expected[test_data]["input"]))
        out = solution.function()
        assert out == expected[test_data]["output"]
