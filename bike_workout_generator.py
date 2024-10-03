import random as r

# generates values of each rep
def generate_vals():
    rest_dict = {
        1 : "30 sec off",
        2 : "1 min off"
    }
    rest = rest_dict[r.randint(1,2)]
    rpm = str((r.randint(0,3) * 5) + 120)

    resistance = 0
    res_num = r.randint(0,1)
    if(res_num==0):
        resistance = '11-12'
    else:
        resistance = '13'

    return rest, rpm, resistance

# prints duration of reps
def reps_str(duration,rest,resistance,rpm,times):
    for _ in range(times):
        print(duration,"min on",rest,"@ Resistance "+resistance,rpm+"rpm")

def main():
    print("Hi! I'm your fitness coach. Here is a bike workout:\n")
    
    reps = r.randint(16,20)

    # style of workout
    # 1 - repeats each rep twice
    # 2 - repeats each rep four times
    # 3 - pyramid style
    style = r.randint(1,3)
    
    print("10 min warm up")

    # workout will only consist of two durations of 1, 2, or 3 minutes
    rep_duration_to_exclude = r.randint(0,2)
    rep_duration = [1,2,3]
    rep_duration.pop(rep_duration_to_exclude)

    if(style == 1): # every rep happens twice
        for rep in range(reps // 2):

            rest, rpm, resistance = generate_vals()
            
            if rep % 2 == 0:
                reps_str(rep_duration[0],rest,resistance,rpm,2)
            else:
                reps_str(rep_duration[1],rest,resistance,rpm,2)

    elif(style == 2): # every rep happens four times
        for rep in range(reps // 4):

            rest, rpm, resistance = generate_vals()

            if rep % 2 == 0:
                # print each rep four times, every other time rep loop is ran
                reps_str(rep_duration[0],rest,resistance,rpm,4)
            else:
                reps_str(rep_duration[1],rest,resistance,rpm,4)
    elif(style == 3):
        up = True
        for _ in range(reps // 3):

            rest, rpm, resistance = generate_vals()

            if(up):
                for rep_duration in range(1,4): # from one to three
                    reps_str(rep_duration,rest,resistance,rpm,1)
                up = not up
            else:
                for rep_duration in range(3,0,-1): # from three to one
                    reps_str(rep_duration,rest,resistance,rpm,1)
                up = not up
            
    print("10 min cool down")
            
main()