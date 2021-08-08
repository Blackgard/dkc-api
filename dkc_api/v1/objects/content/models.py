from typing import Optional
from pydantic import BaseModel
from pydantic.networks import HttpUrl
from datetime import datetime


class GetRevisionLastSize(BaseModel):
    size: int
    forced_update: bool


class RevisionLastCountriesUpdated(BaseModel):
    id: str
    name: str

class RevisionLastCountries(BaseModel):
    updated: list[RevisionLastCountriesUpdated]
    removed: list[str]


class RevisionLastCitiesUpdated(BaseModel):
    id: str
    name: str
    country_id: str
    coordinates: list[str]

class RevisionLastCities(BaseModel):
    updated: list[RevisionLastCitiesUpdated]
    removed: list[str]


class RevisionLastNodesUpdated(BaseModel):
    id: str
    name: str
    parent_id: str
    sort: str

class RevisionLastNodes(BaseModel):
    updated: list[RevisionLastNodesUpdated]
    removed: list[str]


class RevisionLastNodesProductsDrawables(BaseModel):
    name: str
    src: str

class RevisionLastNodesProducts(BaseModel):
    id: str
    sort: str
    node_id: str
    name: str
    code: str
    barcode: list[str]
    thumbnail_url: Optional[HttpUrl]
    additional_images: Optional[list[str]]
    attributes: dict[str, str]
    drawables: list[RevisionLastNodesProductsDrawables]

class RevisionLastProducts(BaseModel):
    updated: list[RevisionLastNodesProducts]
    removed: list[str]


class RevisionLastCataloguesUpdates(BaseModel):
    id: str
    parent_id: str
    name: str
    src: str
    node_ids: list[str]

class RevisionLastCatalogues(BaseModel):
    updated: list[RevisionLastCataloguesUpdates]
    removed: list[str]


class RevisionLastBookletsUpdates(BaseModel):
    id: str
    name: str
    src: str
    node_ids: list[str]

class RevisionLastBooklets(BaseModel):
    updated: list[RevisionLastBookletsUpdates]
    removed: list[str]


class RevisionLastCertificatesUpdates(BaseModel):
    id: str
    name: str
    src: str
    node_ids: list[str]
    item_ids: list[str]

class RevisionLastCertificates(BaseModel):
    updated: list[RevisionLastCertificatesUpdates]
    removed: list[str]


class RevisionLastInstructionsUpdates(BaseModel):
    id: str
    name: str
    src: str
    node_ids: list[str]

class RevisionLastInstructions(BaseModel):
    updated: list[RevisionLastInstructionsUpdates]
    removed: list[str]


class RevisionLastSalepointsUpdatesLocation(BaseModel):
    city_id: str
    address: str
    coordinates: list[str]
    
class RevisionLastSalepointsUpdatesContact(BaseModel):
    phones: list[str]

class RevisionLastSalepointsUpdates(BaseModel):
    id: str
    name: str
    url: str
    location: RevisionLastSalepointsUpdatesLocation
    contact: RevisionLastSalepointsUpdatesContact

class RevisionLastSalepoints(BaseModel):
    updated: list[RevisionLastSalepointsUpdates]
    removed: list[str]


class RevisionLast(BaseModel):
    delta: bool
    countries: RevisionLastCountries
    cities: RevisionLastCities
    nodes: RevisionLastNodes
    products: RevisionLastProducts
    catalogues: RevisionLastCatalogues
    booklets: RevisionLastBooklets
    certificates: RevisionLastCertificates
    instructions: RevisionLastInstructions
    salepoints: RevisionLastSalepoints

class GetRevisionLast(BaseModel):
    revision: RevisionLast


class RevisionDrawingsDrawingsUpdatedLinks(BaseModel):
    type: str
    src: str

class RevisionDrawingsDrawingsUpdated(BaseModel):
    id: str
    name: str
    links: list[RevisionDrawingsDrawingsUpdatedLinks]
    node_ids: list[str]
    item_ids: list[str]
    item_full_codes: list[str]

class RevisionDrawingsDrawings(BaseModel):
    updated: list[RevisionDrawingsDrawingsUpdated]
    removed: list[str]

class RevisionDrawings(BaseModel):
    delta: bool
    drawings: RevisionDrawingsDrawings

class GetRevisionDrawings(BaseModel):
    revision: RevisionDrawings


class RevisionCertificatesCertificatesUpdated(BaseModel):
    id: str
    name: str
    src: str
    type: str
    number: str
    start_date: int
    expiration_date: int
    node_ids: list[str]
    item_ids: list[str]
    item_full_codes: list[str]

class RevisionCertificatesCertificates(BaseModel):
    updated: list[RevisionCertificatesCertificatesUpdated]
    removed: list[str]

class RevisionCertificates(BaseModel):
    delta: bool
    certificates: RevisionCertificatesCertificates

class GetRevisionCertificates(BaseModel):
    revision: RevisionCertificates


class RevisionMaterialsMaterialsUpdated(BaseModel):
    id: str
    node_id: str
    name: str
    etim_class_id: str
    type: str
    series: str
    country: str
    unit: str
    volume: int
    weight: int
    code: str
    url: str
    price: int
    barcode: list[str]
    thumbnail_url: Optional[HttpUrl]
    additional_images: Optional[list[str]]
    attributes: dict[str, str]
    etim_attributes: dict[str, str]
    packing: dict[str, int]
    avg_delivery: dict[int, int]
    accessories: list[str]
    accessories_codes: list[str]

class RevisionMaterialsMaterials(BaseModel):
    updated: list[RevisionMaterialsMaterialsUpdated]
    removed: list[str]

class RevisionMaterials(BaseModel):
    delta: bool
    materials: RevisionMaterialsMaterials

class GetRevisionMaterials(BaseModel):
    revision: RevisionMaterials


class GetFile(BaseModel):
    name: str
    value: str


class PostFile(BaseModel):
    id: int

class PostFileContent(BaseModel):
    name: str
    value: str