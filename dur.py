"""write a function which formats a duration, given as a number of seconds, in a human-friendly way.
The function must accept a non-negative integer. If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds."""

def format_duration(seconds):
    if seconds == 0:
        return "now"
    years=seconds//31536000
    seconds%= 31536000
    days=seconds//86400
    seconds%=86400
    hours= seconds//3600
    seconds%=3600
    minutes = seconds //60
    seconds %=60
    parts=[]
    if years:
        parts.append(f"{years} year" + ("s" if years > 1 else ""))
    if days:
        parts.append(f"{days} day" + ("s" if days > 1 else ""))
    if hours:
        parts.append(f"{hours} hour" + ("s" if hours > 1 else ""))
    if minutes:
        parts.append(f"{minutes} minute" + ("s" if minutes > 1 else ""))
    if seconds:
        parts.append(f"{seconds} second" + ("s" if seconds > 1 else ""))
    if len(parts) == 1:
        return parts[0]
    return ", ".join(parts[:-1]) + " and " + parts[-1]
