# Ultimate Social Hub
# User's database
users = [
    {
        "profile" : {"name" : "Abdo", "age" : 18, "country" : "USA", "score" : 90},
        "user_name" : "abdo_08", "join_year" : 2018, "acc_type" : "Premium",
        "posts" : ["Coffee in hand, confidence on point. Let’s own this day!",
                    "Sometimes the best therapy is a long walk with good music."],
        "followers" : {"Adham", "Ali", "Bassem", "Gasser", "Omar", "Youssef"}
    },
    {
        "profile" : {"name" : "Adham", "age" : 17, "country" : "Canada", "score" : 95},
        "user_name" : "adham_09", "join_year" : 2019, "acc_type" : "Premium",
        "posts" : ["Sunday vibes: pajamas, snacks, and zero responsibilities.",
                    "Me: I’ll just watch one episode. Also me: finishes entire season."],
        "followers" : {"Abdo", "Ali", "Gasser", "Youssef"}
    },
    {
        "profile" : {"name" : "Ali", "age" : 16, "country" : "Spain", "score" : 100},
        "user_name" : "ali_10", "join_year" : 2020, "acc_type" : "Premium",
        "posts" : ["Why do we press harder on the remote when the batteries are dying?",
                    "Adulting is basically Googling ‘how to cook rice’ every week."],
        "followers" : {"Abdo", "Adham"}
    },
    {
        "profile" : {"name" : "Bassem", "age" : 18, "country" : "France", "score" : 70},
        "user_name" : "bassem_08", "join_year" : 2021, "acc_type" : "Standard",
        "posts" : ["Small progress every day adds up to big results.",
                    "Don’t count the days, make the days count."],
        "followers" : {"Abdo", "Adham", "Ali", "Gasser"}
    },
    {
        "profile" : {"name" : "Gasser", "age" : 19, "country" : "Portugal", "score" : 60},
        "user_name" : "gasser_07", "join_year" : 2022, "acc_type" : "Standard",
        "posts" : ["Your vibe attracts your tribe — stay positive.",
                    "Okay friends, pineapple on pizza: yes or no?"],
        "followers" : {"Abdo", "Adham", "Ali", "Bassem", "Omar", "Youssef"}
    },
    {
        "profile" : {"name" : "Omar", "age" : 21, "country" : "Egypt", "score" : 65},
        "user_name" : "omar_05", "join_year" : 2023, "acc_type" : "Standard",
        "posts" : ["Drop the last photo you took in the comments — no cheating!",
                    "If you could teleport anywhere right now, where would you go?"],
        "followers" : {"Abdo", "Ali", "Gasser", "Youssef"}
    },
    {
        "profile" : {"name" : "Youssef", "age" : 20, "country" : "Brazil", "score" : 80},
        "user_name" : "youssef_06", "join_year" : 2024, "acc_type" : "Standard",
        "posts" : ["Imagine if dogs could text… mine would just send me 100 messages saying ‘walk?’",
                    "If life had a soundtrack, what song would be playing for you today?"],
        "followers" : {"Gasser", "Omar"}
    }
]

# Updating user's database
users[0]["posts"].append("Plot twist: the weekend is just two weekdays in disguise… stay strong, heroes!")
users[1]["posts"].remove("Sunday vibes: pajamas, snacks, and zero responsibilities.")
users[0]["followers"].discard("Youssef")

# Creating functions
def print_report(user) :
    p = user["profile"]

    print("Name : ", p["name"])
    print("User name : ", user["user_name"])
    print("Age : ", p["age"])
    print("Country : ", p["country"])
    print("Score : ", p["score"])
    print("Joined : ", user["join_year"])
    print("Account : ", user["acc_type"])
    print("Followers : ", len(user["followers"]))
    print("Posts:")
    i = 1
    for post in user["posts"]:
        print(i, "- ", post)
        i += 1
    print()

def mutual_followers(userA, userB) :
    return userA["followers"] & userB["followers"]

def print_all_reports(users) :
    print("----------Ultimate Social Hub's Report----------")
    for user in users :
        print_report(user)

# Calling and displaying functions
print(mutual_followers(users[0], users[2]))
print_all_reports(users)
