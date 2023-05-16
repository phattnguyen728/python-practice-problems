def group_cities_by_state(cities):
    output = {}
    for city in cities:
        name, state = city.split(",")
        state = state.strip()
        if state not in output:
            output[state] = []
        output[state].append(name)
    return output


print(group_cities_by_state(["San Antonio, TX"]))