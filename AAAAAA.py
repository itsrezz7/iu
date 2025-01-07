import random
from datetime import datetime

# Define exercise routines based on goals
exercise_routines = {
    'penurunan berat badan': {
        'pemula': ['Berjalan', 'Bodyweight squats', 'Berbasikal', 'Lompat bintang'],
        'pertengahan': ['Joging', 'Lunges', 'HIIT', 'Mountain climbers'],
        'mahir': ['Berlari', 'Burpees', 'Box jumps', 'Plyometric exercises']
    },
    'penambahan otot': {
        'pemula': ['Push-ups', 'Bodyweight squats', 'Dumbbell press', 'Lat pulldowns'],
        'pertengahan': ['Bench press', 'Deadlifts', 'Pull-ups', 'Overhead press'],
        'mahir': ['Squat jumps', 'Clean and press', 'Snatches', 'Barbell deadlift']
    },
    'ketahanan': {
        'pemula': ['Berjalan', 'Jogging ringan', 'Berenang', 'Berbasikal'],
        'pertengahan': ['Berlari', 'latihan litar', 'Rowing', 'Kettlebell swings'],
        'mahir': ['Latihan maraton', 'HIIT', 'CrossFit WODs', 'Spinning classes']
    },
    'kelenturan': {
        'pemula': ['pose yoga', 'Stretching exercises', 'Pilates basics'],
        'pertengahan': ['Yoga flow', 'Dynamic stretching', 'Advanced Pilates'],
        'mahir': ['Acro yoga', 'Ballet flexibility exercises', 'Deep stretching', 'Advanced Pilates']
    }
}

# Define nutrition recommendations based on goals
nutrition_recommendations = {
    'penurunan berat badan': [
        "Sarapan: Oatmeal dengan buah segar",
        "Makan tengah hari: Salad dengan ayam panggang",
        "Makan malam: Ikan kukus dengan sayuran hijau",
        "Snek: Yogurt rendah lemak atau kacang badam"
    ],
    'penambahan otot': [
        "Sarapan: Telur hancur dengan roti gandum",
        "Makan tengah hari: Ayam panggang dengan nasi perang dan brokoli",
        "Makan malam: Daging lembu tanpa lemak dengan kentang manis",
        "Snek: Protein shake atau keju cottage"
    ],
    'ketahanan': [
        "Sarapan: Smoothie dengan pisang, bayam, dan protein",
        "Makan tengah hari: Pasta gandum dengan ayam dan sayuran",
        "Makan malam: Salmon panggang dengan quinoa",
        "Snek: Bar tenaga atau buah segar"
    ],
    'kelenturan': [
        "Sarapan: Roti bakar dengan alpukat",
        "Makan tengah hari: Sup lentil dengan sayuran",
        "Makan malam: Tofu panggang dengan nasi perang",
        "Snek: Campuran kacang dan biji-bijian"
    ]
}

# Helper functions for BMI and BMR calculation
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def calculate_bmr(weight, height, age, gender):
    if gender == 'lelaki':
        return 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)

# User Profile class with BMI and BMR
class UserProfile:
    def __init__(self, name, goals, fitness_level, weight, height, age, gender):
        self.name = name
        self.goals = goals
        self.fitness_level = fitness_level
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.sleep_quality = 'baik'
        self.stress_level = 'rendah'
        self.available_time = 60
        self.slot_duration = 15
        self.multiple_slots = False  # Default to single slot

    def calculate_bmi(self):
        return calculate_bmi(self.weight, self.height)

    def calculate_bmr(self):
        return calculate_bmr(self.weight, self.height, self.age, self.gender)

    def set_multiple_slots(self, multiple):
        self.multiple_slots = multiple  # Enable or disable multiple slots in one

# Define rest time recommendations based on goals
rest_times = {
    'penurunan berat badan': 30,  # Shorter rest for fat loss
    'penambahan otot': 60,  # Longer rest for muscle gain
    'ketahanan': 30,  # Moderate rest for endurance
    'kelenturan': 15  # Short rest for flexibility exercises
}

# Generate dynamic schedule for all selected goals
def generate_dynamic_schedule(user):
    print("\nGenerating your dynamic workout schedule...")
    schedule = []
    total_time = user.available_time
    slot_duration = user.slot_duration
    num_slots = total_time // slot_duration
    remaining_time = total_time % slot_duration
    goal_index = 0

    # Adjust intensity based on BMI
    bmi = user.calculate_bmi()
    if bmi < 18.5:
        adjusted_level = 'pemula'
    elif 18.5 <= bmi < 25:
        adjusted_level = user.fitness_level
    else:
        adjusted_level = 'pertengahan' if user.fitness_level == 'mahir' else user.fitness_level

    # Assigning workouts with multiple slots if enabled
    for slot in range(num_slots):
        current_goal = user.goals[goal_index % len(user.goals)]
        rest_time = rest_times[current_goal]  # Get the rest time for the current goal

        if user.multiple_slots:  # If multiple exercises in one slot are allowed
            workouts = random.sample(exercise_routines[current_goal][adjusted_level], 2)  # Choose 2 exercises
            schedule.append(f"Slot {slot + 1} ({slot_duration} min): {', '.join(workouts)}")
            schedule.append(f"Rehat selepas slot: {rest_time} min")
        else:
            workout = random.choice(exercise_routines[current_goal][adjusted_level])
            schedule.append(f"Slot {slot + 1} ({slot_duration} min): {workout}")
            schedule.append(f"Rehat selepas slot: {rest_time} min")
        
        goal_index += 1

    if remaining_time > 0:
        current_goal = user.goals[goal_index % len(user.goals)]
        rest_time = rest_times[current_goal]  # Get the rest time for the current goal
        
        if user.multiple_slots:
            workouts = random.sample(exercise_routines[current_goal][adjusted_level], 2)
            schedule.append(f"Slot {num_slots + 1} ({remaining_time} min): {', '.join(workouts)}")
            schedule.append(f"Rehat selepas slot: {rest_time} min")
        else:
            workout = random.choice(exercise_routines[current_goal][adjusted_level])
            schedule.append(f"Slot {num_slots + 1} ({remaining_time} min): {workout}")
            schedule.append(f"Rehat selepas slot: {rest_time} min")

    return schedule

# Suggest nutrition plan based on goals and BMR
def suggest_nutrition(user):
    print("\nSaranan Pemakanan Anda Berdasarkan Matlamat:")
    bmr = user.calculate_bmr()
    print(f"Keperluan Kalori Harian Anggaran: {bmr:.2f} kcal")
    for goal in user.goals:
        print(f"\nMatlamat: {goal.capitalize()}")
        recommendations = nutrition_recommendations[goal]
        for item in recommendations:
            print(f"- {item}")

# Calculate daily water intake recommendation
def calculate_water_intake(weight, exercise_time):
    # Basic water intake: 35 ml per kg of body weight
    basic_intake = weight * 35  # in ml
    # Additional intake: 350 ml for every 30 min of exercise
    additional_intake = (exercise_time / 30) * 350  # in ml
    total_intake = basic_intake + additional_intake
    return total_intake / 1000  # Convert to liters

# Suggest hydration plan
def suggest_hydration(user):
    print("\nSaranan Pengambilan Air:")
    water_intake = calculate_water_intake(user.weight, user.available_time)
    print(f"Anda disarankan untuk minum sekitar {water_intake:.2f} liter air setiap hari, termasuk waktu latihan.")


# Main function to simulate interaction
def fitness_system():
    print("""
               __      _                       _         _       _
              / _\ ___| | __ _ _ __ ___   __ _| |_    __| | __ _| |_ __ _ _ __   __ _ 
              \ \ / _ \ |/ _` | '_ ` _ \ / _` | __|  / _` |/ _` | __/ _` | '_ \ / _` |
               \ \  __/ | (_| | | | | | | (_| | |_  | (_| | (_| | || (_| | | | | (_| |
              \__/\___|_|\__,_|_| |_| |_|\__,_|\__|  \__,_|\__,_|\__\__,_|_| |_|\__, |
                                                                                |___/
                                                                                """)
    input("Press enter to continue")
    print("Selamat datang ke Sistem Saranan Kecergasan!")
    name = input("Masukkan nama anda: ").strip()
    weight = float(input("Masukkan berat badan anda (kg): ").strip())
    height = float(input("Masukkan tinggi anda (m): ").strip())
    age = int(input("Masukkan umur anda: ").strip())
    gender = input("Masukkan jantina anda (lelaki/perempuan): ").strip().lower()
    
    goals_input = input(
        "Masukkan matlamat kecergasan anda, pisahkan dengan koma (penambahan otot, penurunan berat badan, ketahanan, kelenturan): "
    ).strip().lower()
    goals = [goal.strip() for goal in goals_input.split(",")]
    
    fitness_level = input("Masukkan tahap kecergasan anda (pemula, pertengahan, mahir): ").strip().lower()

    # Create user profile
    user = UserProfile(name, goals, fitness_level, weight, height, age, gender)

    # Set multiple slots (allowing two exercises per slot)
    multiple_input = input("Adakah anda ingin melakukan slot berganda dalam satu sesi senaman? (ya/tidak): ").strip().lower()
    user.set_multiple_slots(multiple_input == "ya")

    # Simulate sleep and stress levels
    sleep_quality = input("Bagaimanakah kualiti tidur anda semalam? (baik, teruk): ").strip().lower()
    user.sleep_quality = sleep_quality
    
    stress_level = input("Bagaimana tahap tekanan stres anda hari ini? (rendah, tinggi): ").strip().lower()
    user.stress_level = stress_level

    # Set available time for workout
    available_time = int(input("Berapa banyak masa yang anda ada untuk bersenam hari ini (dalam minit)? ").strip())
    user.available_time = available_time

    # Set slot duration
    slot_duration = int(input("Berapa lama durasi untuk setiap slot senaman (dalam minit)? ").strip())
    user.slot_duration = slot_duration

    # Generate and display the dynamic schedule
    dynamic_schedule = generate_dynamic_schedule(user)
    print("\nBerikut ialah jadual senaman dinamik anda untuk hari ini:")
    for slot in dynamic_schedule:
        print(slot)

    # Suggest hydration plan
    suggest_hydration(user)
    
    # Suggest nutrition plan
    suggest_nutrition(user)
    

if __name__ == "__main__":
    fitness_system()
