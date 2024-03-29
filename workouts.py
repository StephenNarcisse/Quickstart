# Exercises
chest = [
    {"id": 0, "name": "Bench Press", "equipment": "BARBELL", "type": "MAJOR", "training_max": 0},
    {"id": 1, "name": "Incline Bench Press", "equipment": "BARBELL", "type": "MAJOR", "training_max": 0},
    {"id": 2, "name": "Decline Bench Press", "equipment": "BARBELL", "type": "MAJOR", "training_max": 0},
    {"id": 3, "name": "Chest Press", "equipment": "BARBELL", "type": "MAJOR", "training_max": 0},
    {"id": 4, "name": "DB Bench Press", "equipment": "DUMBBELL", "type": "MAJOR", "training_max": 0},
    {"id": 5, "name": "Incline DB Bench Press", "equipment": "DUMBBELL", "type": "MAJOR", "training_max": 0},
    {"id": 6, "name": "Decline DB Bench Press", "equipment": "DUMBBELL", "type": "MAJOR", "training_max": 0},
    {"id": 7, "name": "Machine Fly", "equipment": "MACHINE", "type": "ACCESSORY", "training_max": 0},
    {"id": 8, "name": "Dips", "equipment": "BODYWEIGHT", "type": "MAJOR", "training_max": 0},

]

# Workouts
# "html test": '<div class="p-2"><h2>60 Minutes</h2></div>'

TEMPLATE = [
    {"link": "", "title": "",
     "summary": "",
     "card summary": "",
     "frequency": "", "duration": "", "time": "", "type": "",
     "experience": "",
     "hyperlink": "",
     "index": 0,
     "notes 1": '*For any lift that indicates weight as  "Choose Appropriate" you are expected to be able to choose a weight that you can complete all sets and reps at an RPE of 7 or 8',
     "notes 2": "**RPE stands for rate of perceived exhaustion. 10 is max effort, 9 is 1 in the tank. 8 is 2 in the tank etc.",
     "notes 3": "***AMRAP stands for As Many Reps As Possible. In most programs this typically means as many as you can with good form while leaving 1-2 in the tank. Not absolute failure.",
     },
]

bodybuilding = [
    {"link": "GVT", "title": "German Volume Training",
     "summary": "German Volume Training (GVT) is a hypertrophy program designed by Charles Poliquin to shock the muscles with a significant increase in volume through 10x10 sets. It is designed to be run for a relatively short period of time, about 4 weeks, and is comprised of three different workouts run five days per week. ",
     "card summary": "",
     "frequency": "4x-5x Per Week", "duration": "1 Cycle", "time": "90-120 Minutes", "type": "Bodybuilding",
     "experience": "Intermediate+",
     "index": 0,
     },
    {"link": "531BBB",
     "title": "531 Boring But Big for Bodybuilding",
     "summary": "5/3/1 BBB for bodybuilding is an interpretation of Jim Wendler’s 5/3/1 BBB strength program that is focused on bodybuilding aesthetics and hypertrophy instead of raw strength. It is run for 7 weeks per cycle with 4 training days per week. It was written by /u/GriefandHoz and is not officially endorsed in any way by Jim Wendler. The author did cite 5/3/1 Forever as the primary influence on the program, mixed with some of their own personal training preferences.",
     "card summary": "",
     "frequency": "4x Per Week", "duration": "7 Week Cycles", "time": "60-90 Minutes", "type": "Bodybuilding",
     "experience": "Experience level: Intermediate-Advanced",
     "index": 1,
     },
    {"link": "Mathias", "title": "12 Week Mass Building Hypertrophy Workout for Powerlifters (Mathias Method)",
     "summary": "This mass building workout focuses on stimulating muscular hypertrophy and developing raw strength. It is a 12 week powerlifting program built on 4 high volume training sessions per week and was developed by Ryan Mathias at Mathias Method. It is a peaking program that is designed to build your one rep max in the squat, bench press, and deadlift for meet day.",
     "card summary": "",
     "frequency": "4x Per Week", "duration": "12 Week Cycles", "time": "60-90 Minutes", "type": "Bodybuilding",
     "experience": "Intermediate+",
     "index": 2,
     },
    {"link": "GoldenSix", "title": "Arnold Schwarzenegger's Golden Six",
     "summary": "Arnold Schwarzenegger’s workout routine known as “Golden Six” is a 3 day beginner bodybuilding routine that can be run indefinitely. It was used in the early days of Schwarzenegger’s training before he started higher volume training programs.",
     "card summary": "",
     "frequency": "3x Per Week", "duration": "Single Routine Repeating", "time": "40-60 Minutes",
     "type": "Bodybuilding",
     "experience": "Beginner",
     "index": 3,
     },
    {"link": "Metallicadpa", "title": "Metallicadpa Linear PPL for Beginners",
     "summary": "A 6 day linear progression program that has you increasing weights week to week. The program itself is customizable and the progression scheme can be changed when you feel is necessary or when you're more advanced.  This is the basic version which focuses on progressing compounds week to week, and accessories whenever you hit the double progression scheme.",
     "card summary": "",
     "frequency": "6x Per Week", "duration": "", "time": "60-90 Minutes", "type": "Bodybuilding",
     "experience": "Beginner",
     "index": 4,
     },
    {"link": "Ronnie", "title": "Ronnie Coleman Workout Program",
     "summary": "The man, the myth, the legend: 8 time Mr. Olympia Ronnie Coleman. The Ronnie Coleman workout routine is an intermediate/advanced level workout routine with 6 training days per week, high volume, and a large number of movements – it is not for the faint of heart. \n This is a brutal bodybuilding program inspired by the man some consider to be the GOAT bodybuilder.",
     "card summary": "",
     "frequency": "6x Per Week", "duration": "Single Routine Repeating", "time": "90-120 Minutes",
     "type": "Bodybuilding",
     "experience": "Intermediate/Advanced",
     "index": 5,
     },
    {"link": "PHAT", "title": "PHAT By Dr. Layne Norton",
     "summary": "The PHAT (Power Hypertrophy Adaptive Training) workout routine is a 5 day powerbuilding program for athletes seeking strength and hypertrophy development. \n Developed by Dr. Layne Norton, the PHAT workout routine blends power and hypertrophy work, making it ideal for bodybuilders looking to gain size and lifters that want to look aesthetic without being weak.",
     "card summary": "",
     "frequency": "5x Per Week", "duration": "", "time": "90 Minutes", "type": "Powerbuilding",
     "experience": "",
     "index": 6,
     },
    {"link": "JoeDelaney6Day", "title": "Joe Delaney Ibiza Shreds 6 Day Upper/Lower Split Workout Routine",
     "summary": "Joe Delaney’s Ibiza Shreds program is a 6 day upper/lower split workout routine focused on bodybuilding and hypertrophy. It runs for 3 blocks spread across 10 weeks, each week comprised of two upper body training days, two lower body training days, and two isolation exercise + abs training days. ",
     "card summary": "",
     "frequency": "6x Per Week", "duration": "10 Weeks", "time": "60-90 Minutes", "type": "Bodybuilding",
     "experience": "Intermediate+",
     "index": 7,
     },
    {"link": "JoeDelaney5Day", "title": "Joe Delaney 5 Day Full Body Split ",
     "summary": "Joe Delaney’s 5 day full body split is a bodybuilding workout routine focused on aesthetic goals and having fun in the gym. This workout was birthed from Joey D’s personal training experience with different workout splits and represents how he has been training as of January 2020.",
     "card summary": "",
     "frequency": "5x Per Week", "duration": "6 Weeks", "time": "60-90 Minutes", "type": "Bodybuilding",
     "experience": "Intermediate/Advanced",
     "hyperlink": "https://liftvault.com/programs/bodybuilding/joe-delaney-5-day-full-body-split-spreadsheet/",
     "index": 8,
     },

]

powerlifting = [

    {"title": "Sheiko",
     "summary": "Sheiko programs are powerlifting programs attributed to Boris Sheiko, renowned Russian powerlifting coach. His programs are known for their high volume and great results for those who can complete them.",
     "frequency": "5x Per Week", "time": "60 Minutes", "type": "Bodybuilding", },
    {"title": "MadCow",
     "summary": "Another spinoff of Bill Starr’s 5×5, Madcow 5×5 incorporates bodybuilder-friendly assistance work (along with lots of rows) with the fundamental Big 3 compound movements to create a simple but effective strength program. Though originally designed with bodybuilding in mind, this can be effectively utilized for off-season (read: not peaking) powerlifting training, as the linear progression and rep range complement strength gains nicely.",
     "frequency": "5x Per Week", "time": "60 Minutes", "type": "Powerlifting", },
]
