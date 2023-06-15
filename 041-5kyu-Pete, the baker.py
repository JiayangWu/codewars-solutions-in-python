def cakes(recipe, available):
    res = float("inf")
    for key, val in recipe.items():
        if key in available:
            res = min(res, available[key]// val )
        else:
            return 0
    return res