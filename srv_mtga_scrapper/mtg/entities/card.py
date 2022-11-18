from mtg.entities.card_foreign import CardForeign

class Card:
    id: str
    multiverse_id: str
    name: str
    manacost: str
    colors = [str]
    type: str
    types = [str]
    subtypes = [str]
    rarity: str
    set: str
    set_name: str
    text: str
    artist: str
    number: int
    power: int
    toughness: int
    layout: str
    imge_url: str
    variations: str
    foreign_names = [CardForeign]
    printings = str