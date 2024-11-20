# Hotel Management Microservice

## Description
This microservice processes reservation data for a hotel management system. It categorizes rooms into "checked-in" and "checked-out" based on their reservation details, specifically the check-out date and current check-in status.

---

## Features
- Accepts JSON input containing reservation data.
- Returns a JSON response categorizing rooms into:
  - `checked-in`: Rooms with a check-out date of today but are still marked as "checked-in."
  - `checked-out`: Rooms with a check-out date of today and are already checked out.

---

## Endpoint
### `/check_rooms`
**Method**: POST  
**Description**: Processes reservation data and categorizes rooms.

---

## Input Example
Send a POST request with the following JSON data:

```json
[
    {
        "_id": "1",
        "lastName": "Doe",
        "firstName": "Jane",
        "checkInDate": "2024-11-07",
        "checkOutDate": "2024-11-17",
        "roomNumber": "102",
        "checkedIn": false
    },
    {
        "_id": "2",
        "lastName": "Smith",
        "firstName": "John",
        "checkInDate": "2024-11-10",
        "checkOutDate": "2024-11-17",
        "roomNumber": "203",
        "checkedIn": true
    }
]
