
def get_time_string(elapsed_seconds):
    hours = int(elapsed_seconds // 3600)
    minutes = int((elapsed_seconds % 3600) // 60)
    seconds = int(elapsed_seconds % 60)
    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return time_str

def convert_to_seconds(time_value, time_unit):
    if time_unit == "sec":
        return time_value
    elif time_unit == "min":
        return time_value * 60
    elif time_unit == "hour":
        return time_value * 3600