import pytest
from typing import Dict, Tuple

from polytropos.ontology.track import Track
from polytropos.actions.translate import Translator

@pytest.fixture()
def source() -> Tuple[Dict, Dict]:
    doc: Dict = {
        "first_source_folder": {
            "name": "Steve",
            "color": "red"
        },
        "second_source_folder": {
            "name": "Bob",
            "color": "blue"
        }

    }

    spec: Dict = {
        "source_folder_1": {
            "name": "first_source_folder",
            "data_type": "Folder",
            "sort_order": 0
        },
        "source_name_1": {
            "name": "name",
            "data_type": "Text",
            "parent": "source_folder_1",
            "sort_order": 0
        },
        "source_color_1": {
            "name": "color",
            "data_type": "Text",
            "parent": "source_folder_1",
            "sort_order": 1
        },
        "source_folder_2": {
            "name": "second_source_folder",
            "data_type": "Folder",
            "sort_order": 1
        },
        "source_name_2": {
            "name": "name",
            "data_type": "Text",
            "parent": "source_folder_2",
            "sort_order": 0
        },
        "source_color_2": {
            "name": "color",
            "data_type": "Text",
            "parent": "source_folder_2",
            "sort_order": 1
        },

    }
    return spec, doc

@pytest.fixture
def target() -> Tuple[Dict, Dict]:
    doc: Dict = {
        "the_list": [
            {
                "name": "Steve",
                "color": "red"
            },
            {
                "name": "Bob",
                "color": "blue"
            }
        ]
    }

    spec: Dict = {
        "target_list": {
            "name": "the_list",
            "data_type": "List",
            "sort_order": 0,
            "sources": ["source_folder_1", "source_folder_2"],
        },
        "target_list_name": {
            "name": "name",
            "data_type": "Text",
            "parent": "target_list",
            "sort_order": 0,
            "sources": ["source_name_1", "source_name_2"]
        },
        "target_list_color": {
            "name": "color",
            "data_type": "Text",
            "parent": "target_list",
            "sort_order": 1,
            "sources": ["source_color_1", "source_color_2"]
        }
    }

    return spec, doc

def test_list_from_folders(source, target):
    source_spec, source_doc = source
    target_spec, expected = target
    source_track: Track = Track.build(source_spec, None, "Source")
    target_track: Track = Track.build(target_spec, source_track, "Target")
    translate: Translator = Translator(target_track)
    actual: Dict = translate(source_doc)
    assert actual == expected
