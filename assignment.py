def stud_details(*args,**kwargs):
    details=1
    for num in args:
        details*=num
        print(details)
    print(f"Hello{kwargs}")