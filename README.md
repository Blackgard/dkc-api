<h3 align="center">DKC API v1</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Connector to DKC API v1 (<a href="https://www.dkc.ru/ru/">dkc.ru</a>)
    <br>
</p>

## 📚 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Available models](#available_models)
- [Usage](#usage)

## 💬 About <a name = "about"></a>

Connector for connecting via api to DKC. Allows you to easily retrieve product and news data.

## 🧵 Getting Started <a name = "getting_started"></a>

For download use pip:

```cmd
python -m pip install dkc-api
```

### Init

To get started, you need to import the main class DkcAPI.

```python
from dkc_api.v1.dkc_api import DkcAPI
```

Next, we pass the initialization parameters to the class. If you want to use environment variables, then the file [.env.example](https://github.com/Blackgard/dkc-api/blob/master/.env.example) is prepared for this.

```python
dkc_api = DkcAPI(
    master_key=os.getenv("TOKEN"),
    debug=True,
    storage=storage.FileTokenStorage(),
    logger=logger
)
```

## 📌 Available models <a name="available_models"></a>

So far, only five DkcAPI models are available for work:

1. Catalog
2. Content
3. Delivery
4. News
5. Project (In developing)

## 🧰 Usage <a name="usage"></a>

### 🪑 Methods Catalog

Catalog object name:

```python
>>> dkc_api.Catalog.*
```

#### GetMaterialStock

This method retrieves data on stock balances.

Args:
- code (list[str], str, int, None): Material code list. If present, ‘Material ID’ is not taken into account. Defaults to [].
- id (list[str], str, int, None): Material id list. Defaults to [].

```python
>>> resolve = dkc_api.Catalog.getMaterialStock()
>>> resolve
GetMaterialStock({create: datetime, materials: [{ id: 81, status: true, code: 1200, warehouse: [{code: 2765, ...]}, ...]}, ...] })
```

#### GetMaterial

This method returns all data for the specified material.

Args:
- code (str): Material code.

```python
>>> resolve = dkc_api.Catalog.getMaterial(code=1200)
>>> resolve
GetMaterial({material: {id: 81, node_id: 1234, etim_class_id: "ETIM", name: "Product name", type: "Type", ...})
```

#### getMaterialAnalogs

This method returns a list of product analogues. 

Args:
- code (str, None): Material code.

```python
>>> resolve = dkc_api.Catalog.getMaterialAnalogs(code=1200)
>>> resolve
GetMaterialAnalogs({analogs: { "1200": [ *product_analogue_codes* ]}})
```

You can get a list of all analogs for all products, for this you need to leave the "code" parameter empty.

```python
>>> resolve = dkc_api.Catalog.getMaterialAnalogs()
>>> resolve
GetMaterialAnalogs({analogs: { *product_codes*: [ *product_analogue_codes* ]}})
```


#### getMaterialAccessories

This method returns a list of product accessories. 

Args:
- code (str, None): Material code.

```python
>>> resolve = dkc_api.Catalog.getMaterialAccessories(code=1200)
>>> resolve
GetMaterialAccessories({accessories: { "1200": [ *product_analogue_codes* ]}})
```

You can get a list of all accessories for all products, for this you need to leave the "code" parameter empty.

```python
>>> resolve = dkc_api.Catalog.getMaterialAccessories()
>>> resolve
GetMaterialAccessories({accessories: { *product_codes*: [ *product_analogue_codes* ]}})
```

#### getMaterialCertificates

This method returns a list of product certificates. 

Args:
- code (str): Material code.

```python
>>> resolve = dkc_api.Catalog.getMaterialCertificates(code=1200)
>>> resolve
GetMaterialCertificates({certificates: { "1200": [ *product_analogue_codes* ]}})
```

#### List other methods 

- getMaterialRelated
- getMaterialVideo
- getMaterialDrawingsSketch
- getMaterialDescription
- getMaterialSpecification

### 🏢 Methods Content

Content object name:

```python
>>> dkc_api.Content.*
```

#### getRevisionDrawings

The method allows you to get editorial drawings by product code

Args:
- last_updated (datetime, None): if specified, only processes changes from the specified date. Timestamp format.

```python
>>> resolve = dkc_api.Content.getRevisionDrawings(code=1200)
>>> resolve
GetRevisionDrawings({revision: { delta: bool, drawings: { updated: [id: 1200, name: "Name", links: { type: "Type", ...}], removed: [...]}})
```


#### getRevisionMaterials

The method allows you to get editorial materials by product code

Args:
- last_updated (datetime, optional): if specified, only processes changes from the specified date. Timestamp format.

```python
>>> resolve = dkc_api.Content.getRevisionMaterials(code=1200)
>>> resolve
GetRevisionMaterials({revision: { delta: bool, materials: { updated: [id: 1200, name: "Name", links: { type: "Type", ...}], removed: [...]}})
```


#### postFile

This method allows you to upload files to the dkc api repository

Args:
- file_content (PostFileContent): file content

```python
>>> post_file_content = PostFileContent(name="name_file", value="value_file")
>>> resolve = dkc_api.Content.postFile(file_content=post_file_content)
>>> resolve
PostFile({revision: { id: 872} })
```

#### getFile

This method allows you to get files from the dkc api repository

Args:
- file_id (int): file id

```python
>>> resolve = dkc_api.Content.getFile(file_id=872)
>>> resolve
PostFile({revision: { name: "name_file", value: "value_file" } })
```

#### List other methods 

- getRevisionCertificates
- getRevisionsLastSize
- getRevisionsLast

### 🏃 Methods Delivery

Delivery object name:

```python
>>> dkc_api.Delivery.*
```

#### getDeliveryTime

The method returns the date of shipment of goods

Args:
- delivery_time_content (DeliveryTimeContent): delivery time content. Work how filter.

```python
>>> delivery_time_content = DeliveryTimeContent(company_warehouse="test", items=[])
>>> resolve = dkc_api.Delivery.getDeliveryTime(delivery_time_content=delivery_time_content)
>>> resolve
GetDeliveryTime({items: [{ code: 172, status: true, date_last: {date: *datetime*, amount: 1689030}, date_detail: [...]}, ...] })
```

### 📰 Methods News

News object name:

```python
>>> dkc_api.News.*
```

#### getNewsCompany

The method returns company news.

Args:
- page_index (int): Page index how need load. Default first (0) page.
- length (int): Count news on page. Default 10 news.

```python
>>> resolve = dkc_api.News.getNewsCompany()
>>> resolve
GetNewsCompany({news: [{title: "Title", text: "Text", thumbnail_url: "Url", images: ["URL", ...], timestamp: *datetime*}, ...]})
```


#### getNewsProducts

The method returns products news.

Args:
- page_index (int): Page index how need load. Default first (0) page.
- length (int): Count news on page. Default 10 news.

```python
>>> resolve = dkc_api.News.getNewsProducts()
>>> resolve
GetNewsProducts({news: [{title: "Title", text: "Text", thumbnail_url: "Url", images: ["URL", ...], timestamp: *datetime*}, ...]})
```

#### getNewsCommunity

The method returns community news.

Args:
- page_index (int): Page index how need load. Default first (0) page.
- length (int): Count news on page. Default 10 news.

```python
>>> resolve = dkc_api.News.getNewsCommunity()
>>> resolve
GetNewsCommunity({news: [{text: "Text", timestamp: "08.08.2021"}, ...]})
```
