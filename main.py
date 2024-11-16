
data = load_file()
for sprint in data:
    dates_of_sprint = sprint.dates
    amount_task_todo = 0
    amount_task_throwed = 0
    early_baclog = 0
    not_ravnomer = 0
    strange_close = 0
    for task in sprint.tasks:
        if delta(sprint.end, task.history.close) <= 1_day:
            strange_close += 1

        for histori in task.history:
            if histori.in_work.spend < task.entity / 2:
                not_ravnomer += 1

        if delta(sprint.start, task.history.in_work) < 1_day:
            early_baclog += 1

        if sprint.status == 'завершён':
            if task.status == 'к выполнению':
                amount_task_todo += 1

        if task.status == 'снято':
            amount_task_throwed += 1

    if strange_close >= crit_amount:
        extrim_fast_close = True
    else:
        extrim_fast_close = False

    if not_ravnomer >= crit_amount:
        not_normal_raspred = True
    else:
        not_normal_raspred = False

    if early_baclog / len(sprint.tasks) * 100 < 20:
        bad_baclog = True
    else:
        bad_baclog = False

    if amount_task_todo / len(sprint.tasks) * 100 < 20:
        bad_todo = True
    else:
        bad_todo = False

    if amount_task_throwed / len(sprint.tasks) * 100 < 10:
        throwed = True
    else:
        throwed = False


# curl -X POST -F "file=@sprints-Table-1.csv" -F "file=@history-Table-1.csv" -H "Content-Type: multipart/form-data" http://localhost:8000/sprints/upload
