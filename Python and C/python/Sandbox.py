def parse_log_events(logs):
    info = 0
    error = 0
    warning = 0
    for i in logs:
        if "INFO" in i:
            info += 1
            continue
        elif "ERROR" in i:
            error += 1
            continue
        elif "WARNING" in i:
            warning += 1
            continue
        else:
            continue

    events_counter = {'INFO': {info}, 'ERROR': {error}, 'WARNING': {warning}}
    return events_counter

a_logs = [
    "2026-09-25 10:00:00 INFO User logged in",
    "2026-09-25 10:05:00 ERROR Database connection failed",
    "2026-09-25 10:06:00 WARNING High memory usage",
    "2026-09-25 10:10:00 INFO User logged out",
    "2026-09-25 10:12:00 ERROR Timeout on API call"
]

print(parse_log_events(a_logs))