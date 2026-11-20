from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    return json.loads((ROOT / "content" / name).read_text(encoding="utf-8"))

def test_graph_nodes_and_edges_are_well_formed():
    graph = load("knowledge_graph.json")
    ids = [node["id"] for node in graph["nodes"]]
    assert len(ids) == len(set(ids))
    known = set(ids)
    allowed = set(graph["edge_semantics"])
    for edge in graph["edges"]:
        assert edge["source"] in known
        assert edge["target"] in known
        assert edge["type"] in allowed
        assert edge["source"] != edge["target"]
        if edge["type"] in {"extends", "contrasts"}:
            assert edge.get("reason"), edge

def test_graph_problem_nodes_match_published_posts():
    graph = load("knowledge_graph.json")
    posts = [p for p in load("posts.json") if p["status"] == "published"]
    nodes = {n["slug"] for n in graph["nodes"] if n["type"] == "problem"}
    assert nodes == {p["slug"] for p in posts}
    for post in posts:
        node = f'post:{post["slug"]}'
        assert sum(e["source"] == node and e["type"] == "classified_as" for e in graph["edges"]) == 1
        assert sum(e["source"] == node and e["type"] == "instantiates" for e in graph["edges"]) == 1

def test_graph_learning_paths_preserve_order():
    graph = load("knowledge_graph.json")
    for path in load("reading_paths.json"):
        for i, slug in enumerate(path["posts"]):
            assert any(e["source"] == f'path:{path["id"]}' and e["target"] == f'post:{slug}' and e["type"] == "includes" and e.get("position") == i + 1 for e in graph["edges"])
            if i:
                assert any(e["source"] == f'post:{path["posts"][i-1]}' and e["target"] == f'post:{slug}' and e["type"] == "precedes_in_path" and e.get("path") == path["id"] for e in graph["edges"])

def test_coverage_registry_does_not_overstate_curated_sets():
    coverage = load("coverage.json")
    assert [x["id"] for x in coverage["target_sets"]] == ["blind-75", "neetcode-150"]
    for target in coverage["target_sets"]:
        if target["audit_status"] != "audited":
            assert target["coverage_count"] is None
    published = {p["slug"] for p in load("posts.json") if p["status"] == "published"}
    registry = [p["slug"] for p in coverage["published_posts"]]
    assert set(registry) == published
    assert len(registry) == len(set(registry))
    assert not ({p["slug"] for p in coverage["priority_queue"]} & published)
