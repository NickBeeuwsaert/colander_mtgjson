import colander

from .mixins import RenameMixin


class CreatureSchema(colander.MappingSchema):
    power = colander.SchemaNode(colander.String(), missing=None)
    toughness = colander.SchemaNode(colander.String(), missing=None)


class SpellSchema(colander.MappingSchema):
    mana_cost = colander.SchemaNode(colander.String(), rename="manaCost", missing="")
    converted_mana_cost = colander.SchemaNode(
        colander.Integer(), rename="convertedManaCost"
    )


class PlaneswalkerSchema(colander.MappingSchema):
    loyalty = colander.SchemaNode(colander.String(), missing=None)


class MCMSchema(colander.MappingSchema):
    mcm_id = colander.SchemaNode(colander.Integer(), rename="mcmId", missing=None)
    mcm_meta_id = colander.SchemaNode(
        colander.Integer(), rename="mcmMetaId", missing=None
    )


class MTGArenaSchema(colander.MappingSchema):
    mtg_arena_id = colander.SchemaNode(
        colander.Integer(), rename="mtgArenaId", missing=None
    )


class MTGOnlineSchema(colander.MappingSchema):
    mtgo_foil_id = colander.SchemaNode(
        colander.Integer(), rename="mtgoFoilId", missing=None
    )
    mtgo_id = colander.SchemaNode(colander.Integer(), rename="mtgoId", missing=None)


class MTGStocksSchema(colander.MappingSchema):
    mtgstocks_id = colander.SchemaNode(
        colander.Integer(), rename="mtgstocksId", missing=None
    )


class MultiverseSchema(colander.MappingSchema):
    multiverse_id = colander.SchemaNode(
        colander.Integer(), rename="multiverseId", missing=None
    )


class ScryfallSchema(colander.MappingSchema):
    scryfall_id = colander.SchemaNode(
        colander.String(), validator=colander.uuid, rename="scryfallId", missing=None
    )
    scryfall_oracle_id = colander.SchemaNode(
        colander.String(), validator=colander.uuid, rename="scryfallOracleId"
    )
    scryfall_illustration_id = colander.SchemaNode(
        colander.String(),
        validator=colander.uuid,
        rename="scryfallIllustrationId",
        missing=None,
    )


class MultipleFaceCardSchema(colander.MappingSchema):
    side = colander.SchemaNode(
        colander.String(), validator=colander.OneOf(["a", "b", "c"]), missing="a"
    )


class TypesSchema(colander.MappingSchema):
    type = colander.SchemaNode(colander.String())
    types = colander.SequenceSchema(colander.SchemaNode(colander.String()))
    subtypes = colander.SequenceSchema(colander.SchemaNode(colander.String()))
    supertypes = colander.SequenceSchema(colander.SchemaNode(colander.String()))


class ColorSchema(colander.MappingSchema):
    border_color = colander.SchemaNode(colander.String(), rename="borderColor")
    color_identity = colander.SchemaNode(
        colander.Set(),
        colander.SchemaNode(colander.String()),
        validator=colander.ContainsOnly(["R", "U", "G", "B", "W"]),
        rename="colorIdentity",
    )
    colors = colander.SchemaNode(
        colander.Set(),
        colander.SchemaNode(colander.String()),
        validator=colander.ContainsOnly(["R", "U", "G", "B", "W"]),
    )


class BaseCardSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    artist = colander.SchemaNode(colander.String(), missing=None)


class CardSchema(
    RenameMixin,
    SpellSchema,
    CreatureSchema,
    PlaneswalkerSchema,
    MCMSchema,
    MTGArenaSchema,
    MTGOnlineSchema,
    MTGStocksSchema,
    MultiverseSchema,
    ScryfallSchema,
    MultipleFaceCardSchema,
    TypesSchema,
    BaseCardSchema,
):
    pass
