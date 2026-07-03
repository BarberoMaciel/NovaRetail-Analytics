
````md
# NovaRetail Analytics – Backend & Automatización

##  Descripción del Proyecto

NovaRetail Analytics es una solución de analítica de datos end-to-end que expone KPIs de negocio a través de una API desarrollada en FastAPI, utilizando Google BigQuery como Data Warehouse y una capa semántica basada en vistas SQL.

La solución está containerizada con Docker para asegurar portabilidad y reproducibilidad del entorno.

---

##  Arquitectura del Sistema

La arquitectura está compuesta por las siguientes capas:

- **Data Warehouse:** Google BigQuery
- **Capa Semántica:** Vistas SQL (KPIs predefinidos)
- **Backend:** FastAPI (Python)
- **Contenedorización:** Docker + Docker Compose

---

##  KPIs Expuestos

La API expone métricas clave del negocio como:

- Total Sales Volume
- Average Ticket
- Customer Lifetime Value (CLV)
- Retention Rate
- Revenue by Channel
- Cart Abandonment Rate
- Stock Turnover
- Delivery Time
- Shipping Cost

---

##  Cómo ejecutar el proyecto

###  Requisitos previos

- Docker instalado
- Docker Compose instalado

###  Ejecución

Desde la raíz del proyecto:

```bash
docker compose up --build
````

---

##  Acceso a la API

La API quedará disponible en:

[http://localhost:8000](http://localhost:8000)

---

##  Documentación de la API

Swagger UI disponible en:

[http://localhost:8000/docs](http://localhost:8000/docs)

---

##  Endpoint principal

Ejemplo de endpoint disponible:

**GET** `/kpi/total-sales`

### Respuesta:

```json
{
  "total_sales_volume": 180679023
}
```
```