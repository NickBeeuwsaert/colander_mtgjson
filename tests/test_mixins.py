import colander

from mixins import RenameMixin


class DummySchema(RenameMixin, colander.MappingSchema):
    rename_me = colander.SchemaNode(
        colander.Integer(),
        rename='renameMe'
    )
    leave_me_alone = colander.SchemaNode(colander.Integer())

def test_rename_mixin_renames_on_deserialize():
    schema = DummySchema()

    assert schema.deserialize({
        'renameMe': 0,
        'leave_me_alone': 1
    }) == {
        'rename_me': 0,
        'leave_me_alone': 1
    }

def test_rename_mixin_renames_on_serialize():
    schema = DummySchema()

    assert schema.serialize({
        'rename_me': 0,
        'leave_me_alone': 1
    }) == {
        'renameMe': '0',
        'leave_me_alone': '1'
    }

def test_rename_mixin_serialize_handles_unknown():
    schema = DummySchema()

    assert schema.serialize({
        'rename_me': 0,
        'leave_me_alone': 1
    }) == {
        'renameMe': '0',
        'leave_me_alone': '1'
    }

def test_rename_mixin_deserialize_handles_unknown():
    schema = DummySchema()

    assert schema.deserialize({
        'renameMe': 0,
        'leave_me_alone': 1,
        'unkown': 2
    }) == {
        'rename_me': 0,
        'leave_me_alone': 1
    }
