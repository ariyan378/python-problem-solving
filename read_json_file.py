import json

Myself = [   {
        "name":"Ariyan Islam hridoy",
        "Grade":[1,2,3],
        "Course":{
            "Data Science ":21,
            "Artificial Intelligence ": 12,
            "Operating System":20,
            "Software Engineering":17
        }
    },
    {
        "Semester":7,
        "University":"Daffodil International University"

    }
]

with open("demo.json" ,'w') as f :
    json.dump(Myself , f ,indent=4)
    
with open("demo.json", 'r') as f:
    data = json.load(f)
    print(data)    