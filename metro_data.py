metro = {
    # Blue Line
    "Airport": ["Terminal"],
    "Terminal": ["Airport", "City"],
    "City": ["Terminal", "Majestic"],
    "Majestic": ["City", "Museum", "Central Square", "Park"],
    "Museum": ["Majestic"],

    # Green Line
    "Central Square": ["Majestic", "Stadium"],
    "Park": ["Majestic", "Lake"],
    "Lake": ["Park", "Garden"],
    "Garden": ["Lake", "University"],
    "University": ["Garden"],

    # Orange Line
    "Stadium": ["Central Square", "Market"],
    "Market": ["Stadium", "Tech Park"],
    "Tech Park": ["Market"]
}


metro_lines = {
    # Blue Line
    "Airport": ["Blue"],
    "Terminal": ["Blue"],
    "City": ["Blue"],
    "Majestic": ["Blue", "Green"],
    "Museum": ["Blue"],

    # Green Line
    "Central Square": ["Green", "Orange"],
    "Park": ["Green"],
    "Lake": ["Green"],
    "Garden": ["Green"],
    "University": ["Green"],

    # Orange Line
    "Stadium": ["Orange"],
    "Market": ["Orange"],
    "Tech Park": ["Orange"]
}
