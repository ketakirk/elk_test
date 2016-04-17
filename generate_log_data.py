import datetime as dt
import random
import string 

def random_ts():
    '''
    Random timestamp generator
    '''
    year = "2016"
    month = "03"
    day = "24"
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return "%s-%s-%sT%0.2d:%0.2d:%0.2d" %(year, month, day, hour, minute, second)

def randincr_ts(ts):
    '''
    Add small random amount to ts and return result as a string
    '''
    FMT = "%Y-%m-%dT%H:%M:%S"
    dto = dt.datetime.strptime(ts, FMT)
    ts2 = dto + dt.timedelta(0, random.randint(0, 120))
    return ts2.strftime(FMT)

def randstr():
    '''
    returns a random 8-character string
    '''
    return ''.join(random.sample(string.ascii_letters, 10))

def generate_log_entry(ts, uname, log_type):
    return "date=%s visitor=%s url=/%s" % (ts, uname, log_type)

def main():
    with open("logfile.log", "w") as lf:
        for i in range(1000):     
            ts1 = random_ts()
            uname = randstr()
            log_type = random.choice(["signup", "search?triangles", "practice?skill=180"])  
            log_entry = generate_log_entry(ts1, uname, log_type)
            
            if "search" in log_type and random.random() < 1.0/3.0:
                ts2 = randincr_ts(ts1)
                log_entry += "\n%s" % generate_log_entry(ts2, uname, "signup")
            
            lf.write("%s\n" % log_entry)

if __name__ == '__main__':
    main()



