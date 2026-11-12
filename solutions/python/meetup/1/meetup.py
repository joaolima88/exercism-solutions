import calendar
import datetime

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)

def format_calendar(year, month):
    import calendar
    import datetime

    calendar = calendar.month(year, month)
    calendar = calendar.splitlines()

    c1 =[]

    for i in calendar:
        c1.append(i.split(' '))

    c2 = []

    for i in c1:
        t = []
        for j in i:
            if j.isalnum():
                t.append(j)
        c2.append(t)

    zeros = 7-len(c2[2])

    for _ in range(zeros):
        c2[2].insert(0, '0')

    return c2[1:]

def meetup(year, month, week, day_of_week):

    calendar = format_calendar(year,month)

    days_match ={
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }

    mode = {"first": 0,
            'second': 1,
            "third": 2,
            "fourth": 3,
            "last": -1,
            'teenth': ['13','14','15','16','17','18','19'],
            "fifth": 4
    }

    try:
        if week != 'teenth' and week != 'fifth':
            day = int([i[days_match[day_of_week]] for i in calendar[1:] if len(i)>days_match[day_of_week] and i[days_match[day_of_week]] != '0'][mode[week]])
            return datetime.date(year, month, day)

        elif week == 'teenth':
 
            day = int([i[days_match[day_of_week]] for i in calendar[1:] if len(i)>days_match[day_of_week] and i[days_match[day_of_week]] in mode['teenth'] and i != 0][0])
            return datetime.date(year, month, day)

        elif week == 'fifth':
                day = int([i[days_match[day_of_week]] for i in calendar[1:] if len(i)>days_match[day_of_week] and i[days_match[day_of_week]] != '0'][mode['fifth']])
                return datetime.date(year, month, day)

    except IndexError:
        raise MeetupDayException("That day does not exist.")


