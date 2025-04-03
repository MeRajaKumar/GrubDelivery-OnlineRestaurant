# Activity Selection Problem using a Greedy Algorithm

def activity_selection(activities):
    # Sorting activities based on their finishing times
    activities.sort(key=lambda x: x[1])
    
    selected_activities = []
    last_end_time = 0
    
    for start, end in activities:
        if start >= last_end_time:  # If activity starts after or when the last one ended
            selected_activities.append((start, end))
            last_end_time = end
    
    return selected_activities

# Example list of activities (start_time, end_time)
activities = [(1, 3), (2, 5), (3, 9), (6, 8), (5, 7), (8, 9)]

# Get the maximum number of activities that can be selected
selected = activity_selection(activities)

# Print results
print("Selected activities:")
for start, end in selected:
    print(f"({start}, {end})")


