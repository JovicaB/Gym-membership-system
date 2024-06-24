import random
from datetime import datetime, timedelta


class GymVisitSimulation:

    def generate_random_start_training_time(self):

        morning_traning_range = (datetime.strptime(
            '06:00', '%H:%M'), datetime.strptime('08:00', '%H:%M'))
        evening_traning_range = (datetime.strptime(
            '17:00', '%H:%M'), datetime.strptime('21:00', '%H:%M'))
        broader_traning_range = (datetime.strptime(
            '08:00', '%H:%M'), datetime.strptime('17:00', '%H:%M'))

        random_time = None
        probability = random.uniform(0, 1)

        # 40% chance for morning time
        if probability < 0.4:
            random_time = random.uniform(
                morning_traning_range[0], morning_traning_range[1])
        # 40% chance for evening time
        elif probability < 0.8:  # 40% chance for evening time
            random_time = random.uniform(
                evening_traning_range[0], evening_traning_range[1])
        # 20% chance for broader time range
        else:
            random_time = random.uniform(
                broader_traning_range[0], broader_traning_range[1])

        formatted_time = random_time.strftime('%H:%M')
        return formatted_time

    def generate_random_training_duration_time(self):
        # Set the time range
        training_duration_range = (30, 120)

        # Set the probabilities for each training duration
        probabilities = {
            'normal': 0.7,  # Higher probability for durations around the middle
            'short': 0.15,  # Lower probability for short durations
            'long': 0.15    # Lower probability for long durations
        }

        # Choose a training duration based on the probabilities
        chosen_duration = random.choices(
            list(probabilities.keys()), list(probabilities.values()))[0]

        # Generate a random duration using normal distribution based on the chosen type
        if chosen_duration == 'normal':
            mean, stddev = (
                training_duration_range[0] + training_duration_range[1]) / 2, 20
        elif chosen_duration == 'short':
            mean, stddev = training_duration_range[0], 10
        else:
            mean, stddev = training_duration_range[1], 10

        # Ensure the generated duration is within the specified range
        generated_duration = max(training_duration_range[0], min(
            training_duration_range[1], round(random.normalvariate(mean, stddev))))

        return generated_duration


    def generate_gym_user_age(self):
        # Set the time range
        age_range = (18, 60)

        # Set the probabilities for each training duration
        probabilities = {
            'young': 0.6,  # Adjusted probability for young
            'mid_age': 0.3,
            'older': 0.1
        }

        # Choose a training duration based on the probabilities
        # Choose a training duration based on the probabilities
        chosen_age = random.choices(
            list(probabilities.keys()), list(probabilities.values()))[0]

        # Generate a random duration using normal distribution based on the chosen type
        if chosen_age == 'young':
            # Adjust the mean and standard deviation for a distribution centered around 18-30
            mean, stddev = (age_range[0] + 30) / 2, 5
            generated_duration = max(age_range[0], min(round(random.normalvariate(mean, stddev)), 30))
        else:
            mean, stddev = age_range[0] if chosen_age == 'mid_age' else age_range[1], 10
            # Ensure the generated duration is within the specified range
            generated_duration = max(age_range[0], min(
                age_range[1], round(random.normalvariate(mean, stddev))))



        # Ensure the generated duration is within the specified range
        generated_duration = max(age_range[0], min(
            age_range[1], round(random.normalvariate(mean, stddev))))

        return generated_duration

    # Example usage
class_object = GymVisitSimulation()
random_time = class_object.generate_gym_user_age()
print(random_time)

# for _ in range(100):
#     random_time = class_object.generate_random_training_duration()
#     print(random_time)
