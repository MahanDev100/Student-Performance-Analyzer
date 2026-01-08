def load_data() :
    records = []
    try:
        with open(path, "r") as file :
            for line in file :
                line = line.strip()
                if not line : 
                    continue

                parts = line.split(",")
                day_subject = parts[0].split(":", 1)
                day = day_subject[0].strip()
                subject = day_subject[1].strip()
                score = int(parts[1])
                hours = int(parts[2].replace("h", ""))

                records.append({
                    "day": day,
                    "subject": subject,
                    "score": score,
                    "hours": hours
                })
    except FileNotFoundError :
        print("no data to analyze")
    return records

def average_score_per_subject(records) :
    result = {}

    for r in records :
        subject = r["subject"]
        score = r["score"]

        if subject not in result :
            result[subject] = []
        result[subject].append(score)

    print("\nAverage score per subject : ")
    for subject in result:
        avg = sum(result[subject]) / len(result[subject])
        print(f"{subject} : {avg:.2f}")

def total_hours_per_subject(records):
    result = {}

    for r in records:
        subject = r["subject"]
        hours = r["hours"]

        if subject not in result:
            result[subject] = 0 
        result[subject] += hours

    print("\nTotal study per subjects : ")
    for subject in result :
        print(f"{subject}: {result[subject]} hours")

def best_and_worst_subject(records):
    scores = {}

    for r in records :
        subject = r["subject"]
        score = r["score"]

        if subject not in scores :
            scores[subject] = []
            scores[subject].append(score)

    averages = {s: sum(scores[s]) / len(scores[s]) for s in scores}
    best = max(averages , key=averages.get)
    worst = min(averages , key=averages.get)

    print(f"\nStrongest subject: {best} ({averages[best]:.2f})")
    print(f"\nWeakest subject: {worst} ({averages[worst]:.2f})")

def efficiency_per_subject(records):
    data = {}

    for r in records:
        subject = r["subject"]
        score = r["score"]
        hours = r["hours"]

        if subject not in data:
            data[subject] = {"score": 0, "hours": 0}
        
        data[subject]["score"] += score
        data[subject]["hours"] += hours

    print("\nEfficiency (score per hour): ")
    for subject in data:
        if data[subject]["hours"] > 0:
            efficiency = data[subject]["score"] / data[subject]["hours"]
        else:
            efficiency = 0
        print(f"{subject}: {efficiency:.2f}")

path = "C:\\Users\\Administrator\\Desktop\\data.csv"

subjects_dict = {"1": "Math", "2": "Science", "3": "Geography"}
hours_dict = {"1": "1h", "2": "2h", "3": "3h", "4": "4h"}
scores_dict = {"20": "20", "19": "19", "18": "18", "17": "17", "16": "16", "15": "15", "14": "14"}
days_dict = {"monday" : "Monday", "tuesday" :"Tuesday", "wednesday" : "Wednesday", "thursday" :"Thursday" , "friday" : "Friday","sunday" : "Sunday","saturday" : "Saturday"}

while True:
    menu = input("_______Student Performance Analyzer_______\nEnter your choice: \n1. Add Student Performance\n2. View Student Performance\n3.Analyze\n0.Exit\n")

    if menu == "1":
        sub_name = input("Select your subject : \n1.Math\n2.Science\n3.Geography\n0.Exit\n")

        if sub_name in subjects_dict:
            sub_time = input("Enter your study time : \n1.1h\n2.2h\n3.3h\n4.4h\n")

            if sub_time in hours_dict:
                sub_score = input("Enter your score : \n20.20\n19.19\n18.18\n17.17\n16.16\n15.15\n14.14\n")
                
                if sub_score in scores_dict :
                    sub_day = input("Day of the week: ").lower()
                    
                    if sub_day in days_dict :
                        with open(path, "a") as file:
                            file.write(f"{days_dict[sub_day]} : {subjects_dict[sub_name]},{scores_dict[sub_score]},{hours_dict[sub_time]}\n")
                            print("Your subject has been added :)")
                    else:
                        print("Invalid day ! ")
                else:
                    print("Invalid score !")
            else:
                print("Invalid time !")
        else:
            print("Invalid subject !")

    elif menu == "2":
        try:
            with open(path, "r") as file:
                data = file.read()
                print(data)
        except FileNotFoundError:
            print("No data yet.")


    elif menu == "3" :
        records = load_data()
        if records:
            average_score_per_subject(records)
            total_hours_per_subject(records)
            best_and_worst_subject(records)
            efficiency_per_subject(records)
        else:
            print("No records found !")

    elif menu == "0" :
        break

    else :
        print("Invalid choice !")