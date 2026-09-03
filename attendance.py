def attendance_percentage(present, total):
    return (present / total) * 100


def eligibility(present, total):
    percentage = attendance_percentage(present, total)

    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"