def filter_by_type(products, filter_type: str | None = None):
    match filter_type:
        case "expensive":
            products = products.order_by("-price")
        case "cheap":
            products = products.order_by("price")
        case "rating":
            products = products.order_by("-avg_rating")
    return products