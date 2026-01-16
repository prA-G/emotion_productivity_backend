def generate_daily_plan(mood: str, tasks: list):
    final_tasks = []

    for task in tasks:
        # Always allow light tasks
        if task.effort == "light":
            final_tasks.append(task)

        # Heavy tasks depend on mood & priority
        elif task.effort == "heavy":
            if mood in ["neutral", "energized"]:
                final_tasks.append(task)
            elif mood in ["low", "overwhelmed"] and task.priority == "high":
                final_tasks.append(task)

    return final_tasks
