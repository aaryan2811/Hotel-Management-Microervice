# Hotel Management Microservice

## Description
This microservice processes reservation data for a hotel management system. It categorizes rooms into "checked-in" and "checked-out" based on their reservation details, specifically the check-out date and current check-in status.

---

## Communication Contract

### Contact Information
If you have any issues with this microservice, you can reach me via **text**.  
**Availability**: Weekdays 5-9 PM, Weekends anytime.

---

### Example Request
Here is an example `curl` command for the endpoint running on **port 5001**:

**POST Call**:
curl -X POST -H "Content-Type: application/json" -d @sample_input.json http://127.0.0.1:5001/check_rooms

---

## Output Example

[
    {
    "checked-in": ["203"],
    "checked-out": ["102"]
    }
]

---

## UML Sequence Diagram
![Hotel Management Microservice](https://github.com/user-attachments/assets/127764f5-8391-470d-8cda-17b58632d6a1)
