#!/usr/bin/python3

def run_time():
    t = 0.0
    n = 0
    while True:
        time = input("Enter 10 km run time: ")
        if time.strip().isdigit():
            t += float(time)
            n += 1
        else:
            break
    print(f"Average of {t/n}, over {n} runs")
    return

if __name__=='__main__':
    run_time()
