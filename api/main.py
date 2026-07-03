from fastapi import FastAPI
from api.services import execute_query

app = FastAPI(
    title="NovaRetail Analytics API",
    description="API para exponer KPIs del Data Warehouse NovaRetail",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "NovaRetail Analytics API",
        "version": "1.0.0"
    }


@app.get("/kpi/total-sales")
def total_sales():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_total_sales`
    """)


@app.get("/kpi/avg-ticket")
def avg_ticket():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_avg_ticket`
    """)


@app.get("/kpi/clv")
def clv():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_clv`
    """)


@app.get("/kpi/retention")
def retention():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_retention`
    """)


@app.get("/kpi/margin-category")
def margin_category():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_margin_category`
    """)


@app.get("/kpi/revenue-channel")
def revenue_channel():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_revenue_channel`
    """)


@app.get("/kpi/revenue-acquisition-channel")
def revenue_acquisition_channel():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_revenue_acquisition_channel`
    """)


@app.get("/kpi/cart-abandonment")
def cart_abandonment():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_cart_abandonment`
    """)


@app.get("/kpi/login-product-view")
def login_product_view():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_login_to_product_view`
    """)


@app.get("/kpi/product-view-checkout")
def product_view_checkout():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_product_view_to_checkout`
    """)


@app.get("/kpi/checkout-purchase")
def checkout_purchase():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_checkout_to_purchase`
    """)


@app.get("/kpi/stock-turnover")
def stock_turnover():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_stock_turnover`
    """)


@app.get("/kpi/shipping-cost")
def shipping_cost():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_shipping_cost`
    """)


@app.get("/kpi/delivery-time")
def delivery_time():
    return execute_query("""
        SELECT *
        FROM `project-d935bc51-c320-4917-9bd.novaretail_semantic.v_kpi_delivery_time`
    """)