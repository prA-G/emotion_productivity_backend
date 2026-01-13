def generate_daily_plan(mood: str, tasks: list):
    if mood in ["low", "overwhelmed"]:
        return [task for task in tasks if task.effort == "light"]
    return tasks
